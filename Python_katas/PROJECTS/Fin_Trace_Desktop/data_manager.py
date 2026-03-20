"""
Data Manager for FinTrace Desktop
Handles all Excel/Pandas operations
"""
import pandas as pd
import os
from datetime import datetime
import openpyxl
from config import DATA_FILE, EXCEL_COLUMNS


class DataManager:
    """Manages all data operations for the expense tracker"""

    def __init__(self, file_path=DATA_FILE):
        self.file_path = file_path
        self.df = None
        self.next_id = 1
        self.initialize_data()

    def initialize_data(self):
        """Initialize or load the Excel file"""
        if not os.path.exists(self.file_path):
            # Create new file with headers and proper dtypes
            self.df = pd.DataFrame(columns=EXCEL_COLUMNS)
            # Set proper data types for empty DataFrame
            self.df['ID'] = self.df['ID'].astype('Int64')
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df['Amount'] = self.df['Amount'].astype('float64')
            self.df['Tax (%)'] = self.df['Tax (%)'].astype('float64')
            self.df['Tax Amount'] = self.df['Tax Amount'].astype('float64')
            self.df['Total With Tax'] = self.df['Total With Tax'].astype('float64')
            self.save_data()
        else:
            # Load existing file
            try:
                self.df = pd.read_excel(self.file_path, engine='openpyxl')

                # Ensure all required columns exist
                for col in EXCEL_COLUMNS:
                    if col not in self.df.columns:
                        self.df[col] = None

                # Convert data types
                if len(self.df) > 0:
                    self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
                    self.df['Amount'] = pd.to_numeric(self.df['Amount'], errors='coerce')
                    self.df['Tax (%)'] = pd.to_numeric(self.df['Tax (%)'], errors='coerce')
                    self.df['Tax Amount'] = pd.to_numeric(self.df['Tax Amount'], errors='coerce')
                    self.df['Total With Tax'] = pd.to_numeric(self.df['Total With Tax'], errors='coerce')
                    self.df['ID'] = pd.to_numeric(self.df['ID'], errors='coerce').fillna(0).astype(int)

                    # Set next ID
                    if 'ID' in self.df.columns and len(self.df) > 0:
                        self.next_id = int(self.df['ID'].max()) + 1
                    else:
                        self.df['ID'] = range(1, len(self.df) + 1)
                        self.next_id = len(self.df) + 1
                else:
                    # Empty DataFrame - set proper types
                    self.next_id = 1
                    self.df['ID'] = self.df['ID'].astype('Int64')
                    self.df['Date'] = pd.to_datetime(self.df['Date'])
                    self.df['Amount'] = self.df['Amount'].astype('float64')
                    self.df['Tax (%)'] = self.df['Tax (%)'].astype('float64')
                    self.df['Tax Amount'] = self.df['Tax Amount'].astype('float64')
                    self.df['Total With Tax'] = self.df['Total With Tax'].astype('float64')

            except Exception as e:
                print(f"Error loading file: {e}")
                self.df = pd.DataFrame(columns=EXCEL_COLUMNS)
                # Set proper types for empty DataFrame
                self.df['ID'] = self.df['ID'].astype('Int64')
                self.df['Date'] = pd.to_datetime(self.df['Date'])
                self.df['Amount'] = self.df['Amount'].astype('float64')
                self.df['Tax (%)'] = self.df['Tax (%)'].astype('float64')
                self.df['Tax Amount'] = self.df['Tax Amount'].astype('float64')
                self.df['Total With Tax'] = self.df['Total With Tax'].astype('float64')
                self.save_data()

    def save_data(self):
        """Save dataframe to Excel"""
        try:
            with pd.ExcelWriter(self.file_path, engine='openpyxl', mode='w') as writer:
                self.df.to_excel(writer, index=False, sheet_name='Transactions')
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def add_transaction(self, transaction_data):
        """Add a new transaction"""
        try:
            # Add ID and timestamps
            transaction_data['ID'] = self.next_id
            transaction_data['Created At'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_data['Last Updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Calculate tax
            amount = float(transaction_data['Amount'])
            tax_percent = float(transaction_data.get('Tax (%)', 0))
            tax_amount = amount * tax_percent / 100
            total_with_tax = amount + tax_amount

            transaction_data['Tax Amount'] = round(tax_amount, 2)
            transaction_data['Total With Tax'] = round(total_with_tax, 2)

            # Convert date to datetime
            if isinstance(transaction_data['Date'], str):
                transaction_data['Date'] = pd.to_datetime(transaction_data['Date'])

            # Append to dataframe
            new_row = pd.DataFrame([transaction_data])
            self.df = pd.concat([self.df, new_row], ignore_index=True)

            self.next_id += 1
            self.save_data()
            return True
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return False

    def update_transaction(self, transaction_id, transaction_data):
        """Update an existing transaction"""
        try:
            idx = self.df[self.df['ID'] == transaction_id].index
            if len(idx) == 0:
                return False

            # Calculate tax
            amount = float(transaction_data['Amount'])
            tax_percent = float(transaction_data.get('Tax (%)', 0))
            tax_amount = amount * tax_percent / 100
            total_with_tax = amount + tax_amount

            transaction_data['Tax Amount'] = round(tax_amount, 2)
            transaction_data['Total With Tax'] = round(total_with_tax, 2)
            transaction_data['Last Updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Convert date to datetime
            if isinstance(transaction_data['Date'], str):
                transaction_data['Date'] = pd.to_datetime(transaction_data['Date'])

            # Update row
            for key, value in transaction_data.items():
                if key in self.df.columns:
                    self.df.at[idx[0], key] = value

            self.save_data()
            return True
        except Exception as e:
            print(f"Error updating transaction: {e}")
            return False

    def delete_transaction(self, transaction_id):
        """Delete a transaction"""
        try:
            self.df = self.df[self.df['ID'] != transaction_id]
            self.save_data()
            return True
        except Exception as e:
            print(f"Error deleting transaction: {e}")
            return False

    def get_all_transactions(self):
        """Get all transactions as dataframe"""
        return self.df.copy()

    def get_transaction_by_id(self, transaction_id):
        """Get a specific transaction"""
        result = self.df[self.df['ID'] == transaction_id]
        if len(result) > 0:
            return result.iloc[0].to_dict()
        return None

    def filter_transactions(self, filters):
        """Filter transactions based on criteria"""
        filtered_df = self.df.copy()

        # Return empty df if no data
        if len(filtered_df) == 0:
            return filtered_df

        try:
            # Date range filter
            if filters.get('date_from'):
                date_from = pd.to_datetime(filters['date_from'])
                filtered_df = filtered_df[filtered_df['Date'] >= date_from]

            if filters.get('date_to'):
                date_to = pd.to_datetime(filters['date_to'])
                filtered_df = filtered_df[filtered_df['Date'] <= date_to]

            # Category filter
            if filters.get('category') and filters['category'] != 'All':
                filtered_df = filtered_df[filtered_df['Category'] == filters['category']]

            # Type filter
            if filters.get('type') and filters['type'] != 'All':
                filtered_df = filtered_df[filtered_df['Type'] == filters['type']]

            # Amount range filter
            if filters.get('min_amount'):
                filtered_df = filtered_df[filtered_df['Amount'] >= float(filters['min_amount'])]

            if filters.get('max_amount'):
                filtered_df = filtered_df[filtered_df['Amount'] <= float(filters['max_amount'])]

            # Text search filter
            if filters.get('search_text'):
                search_text = filters['search_text'].lower()
                filtered_df = filtered_df[
                    filtered_df['Description'].str.lower().str.contains(search_text, na=False)
                ]

            return filtered_df
        except Exception as e:
            print(f"Error filtering transactions: {e}")
            return self.df.copy()

    def get_monthly_summary(self, year, month):
        """Get summary for a specific month"""
        try:
            # Return empty summary if no data
            if len(self.df) == 0:
                return {
                    'total_income': 0,
                    'total_expense': 0,
                    'net_balance': 0,
                    'transaction_count': 0,
                    'data': pd.DataFrame(columns=EXCEL_COLUMNS)
                }

            monthly_df = self.df[
                (self.df['Date'].dt.year == year) & 
                (self.df['Date'].dt.month == month)
            ]

            total_income = monthly_df[monthly_df['Type'] == 'Income']['Amount'].sum()
            total_expense = monthly_df[monthly_df['Type'] == 'Expense']['Amount'].sum()
            net_balance = total_income - total_expense

            return {
                'total_income': total_income,
                'total_expense': total_expense,
                'net_balance': net_balance,
                'transaction_count': len(monthly_df),
                'data': monthly_df
            }
        except Exception as e:
            print(f"Error getting monthly summary: {e}")
            return {
                'total_income': 0,
                'total_expense': 0,
                'net_balance': 0,
                'transaction_count': 0,
                'data': pd.DataFrame(columns=EXCEL_COLUMNS)
            }

    def get_category_summary(self, transaction_type='Expense'):
        """Get summary by category"""
        try:
            if len(self.df) == 0:
                return pd.Series(dtype='float64')

            filtered_df = self.df[self.df['Type'] == transaction_type]
            category_summary = filtered_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
            return category_summary
        except Exception as e:
            print(f"Error getting category summary: {e}")
            return pd.Series(dtype='float64')

    def export_to_csv(self, file_path):
        """Export data to CSV"""
        try:
            self.df.to_csv(file_path, index=False)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
