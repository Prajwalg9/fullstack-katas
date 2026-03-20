"""
Reports and Charts Module for FinTrace Desktop
Handles summary calculations and chart generation
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from config import CHART_COLORS, COLORS
import calendar


class ReportGenerator:
    """Generates reports and charts for financial data"""

    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.setup_matplotlib_style()

    def setup_matplotlib_style(self):
        """Configure matplotlib for dark theme"""
        plt.style.use('dark_background')
        plt.rcParams['figure.facecolor'] = COLORS['bg_darker']
        plt.rcParams['axes.facecolor'] = COLORS['bg_dark']
        plt.rcParams['axes.edgecolor'] = COLORS['border']
        plt.rcParams['text.color'] = COLORS['fg_primary']
        plt.rcParams['axes.labelcolor'] = COLORS['fg_primary']
        plt.rcParams['xtick.color'] = COLORS['fg_secondary']
        plt.rcParams['ytick.color'] = COLORS['fg_secondary']
        plt.rcParams['grid.color'] = COLORS['border']
        plt.rcParams['grid.alpha'] = 0.3

    def create_category_pie_chart(self, year, month):
        """Create pie chart of expenses by category"""
        fig = Figure(figsize=(6, 4), facecolor=COLORS['bg_darker'])
        ax = fig.add_subplot(111)

        try:
            monthly_data = self.data_manager.get_monthly_summary(year, month)
            expenses_df = monthly_data['data']

            # Check if we have data and Type column exists
            if len(expenses_df) == 0 or 'Type' not in expenses_df.columns:
                ax.text(0.5, 0.5, 'No expense data available\nAdd your first transaction!', 
                       ha='center', va='center', fontsize=12, 
                       color=COLORS['fg_secondary'])
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')
                return fig

            # Filter for expenses
            expenses_df = expenses_df[expenses_df['Type'] == 'Expense']

            if len(expenses_df) == 0:
                ax.text(0.5, 0.5, 'No expense data for this month\nAdd some expenses to see the chart', 
                       ha='center', va='center', fontsize=12, 
                       color=COLORS['fg_secondary'])
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')
                return fig

            category_totals = expenses_df.groupby('Category')['Amount'].sum()

            colors = CHART_COLORS[:len(category_totals)]
            wedges, texts, autotexts = ax.pie(
                category_totals.values,
                labels=category_totals.index,
                autopct='%1.1f%%',
                startangle=90,
                colors=colors
            )

            for text in texts:
                text.set_color(COLORS['fg_primary'])
                text.set_fontsize(9)

            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontsize(8)
                autotext.set_weight('bold')

            ax.set_title(f'Expenses by Category ({calendar.month_name[month]} {year})', 
                        color=COLORS['fg_primary'], fontsize=11, pad=10)

        except Exception as e:
            print(f"Error creating pie chart: {e}")
            ax.text(0.5, 0.5, 'No data available yet\nStart by adding transactions!', 
                   ha='center', va='center', fontsize=12, 
                   color=COLORS['fg_secondary'])
            ax.axis('off')

        fig.tight_layout()
        return fig

    def create_monthly_bar_chart(self, year, month):
        """Create bar chart of weekly spending"""
        fig = Figure(figsize=(6, 4), facecolor=COLORS['bg_darker'])
        ax = fig.add_subplot(111)

        try:
            monthly_data = self.data_manager.get_monthly_summary(year, month)
            df = monthly_data['data']

            if len(df) == 0:
                ax.text(0.5, 0.5, 'No data available for this month\nAdd transactions to see weekly trends', 
                       ha='center', va='center', fontsize=12, 
                       color=COLORS['fg_secondary'])
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')
                return fig

            # Group by week
            df['Week'] = df['Date'].dt.isocalendar().week
            weekly_income = df[df['Type'] == 'Income'].groupby('Week')['Amount'].sum()
            weekly_expense = df[df['Type'] == 'Expense'].groupby('Week')['Amount'].sum()

            all_weeks = sorted(set(weekly_income.index) | set(weekly_expense.index))

            if len(all_weeks) == 0:
                ax.text(0.5, 0.5, 'No data available', 
                       ha='center', va='center', fontsize=12, 
                       color=COLORS['fg_secondary'])
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')
                return fig

            income_values = [weekly_income.get(w, 0) for w in all_weeks]
            expense_values = [weekly_expense.get(w, 0) for w in all_weeks]

            x = range(len(all_weeks))
            width = 0.35

            ax.bar([i - width/2 for i in x], income_values, width, 
                  label='Income', color=COLORS['income'], alpha=0.8)
            ax.bar([i + width/2 for i in x], expense_values, width, 
                  label='Expense', color=COLORS['expense'], alpha=0.8)

            ax.set_xlabel('Week', color=COLORS['fg_primary'])
            ax.set_ylabel('Amount', color=COLORS['fg_primary'])
            ax.set_title(f'Weekly Income vs Expense ({calendar.month_name[month]} {year})', 
                        color=COLORS['fg_primary'], fontsize=11)
            ax.set_xticks(x)
            ax.set_xticklabels([f'W{w}' for w in all_weeks])
            ax.legend(facecolor=COLORS['bg_lighter'], edgecolor=COLORS['border'])
            ax.grid(True, alpha=0.2)

        except Exception as e:
            print(f"Error creating bar chart: {e}")
            ax.text(0.5, 0.5, 'No data available yet', 
                   ha='center', va='center', fontsize=12, 
                   color=COLORS['fg_secondary'])
            ax.axis('off')

        fig.tight_layout()
        return fig

    def create_income_expense_line_chart(self, start_date, end_date):
        """Create line chart of income vs expense over time"""
        fig = Figure(figsize=(8, 4), facecolor=COLORS['bg_darker'])
        ax = fig.add_subplot(111)

        try:
            filters = {
                'date_from': start_date,
                'date_to': end_date
            }
            df = self.data_manager.filter_transactions(filters)

            if len(df) == 0:
                ax.text(0.5, 0.5, 'No data available for selected period\nAdd transactions to see trends', 
                       ha='center', va='center', fontsize=12, 
                       color=COLORS['fg_secondary'])
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')
                return fig

            # Group by date
            df['DateOnly'] = df['Date'].dt.date
            daily_income = df[df['Type'] == 'Income'].groupby('DateOnly')['Amount'].sum()
            daily_expense = df[df['Type'] == 'Expense'].groupby('DateOnly')['Amount'].sum()

            # Create complete date range
            date_range = pd.date_range(start=start_date, end=end_date, freq='D')
            dates = [d.date() for d in date_range]

            income_values = [daily_income.get(d, 0) for d in dates]
            expense_values = [daily_expense.get(d, 0) for d in dates]

            ax.plot(dates, income_values, marker='o', linestyle='-', 
                   color=COLORS['income'], label='Income', linewidth=2, markersize=4)
            ax.plot(dates, expense_values, marker='s', linestyle='-', 
                   color=COLORS['expense'], label='Expense', linewidth=2, markersize=4)

            ax.set_xlabel('Date', color=COLORS['fg_primary'])
            ax.set_ylabel('Amount', color=COLORS['fg_primary'])
            ax.set_title('Income vs Expense Over Time', 
                        color=COLORS['fg_primary'], fontsize=11)
            ax.legend(facecolor=COLORS['bg_lighter'], edgecolor=COLORS['border'])
            ax.grid(True, alpha=0.2)

            # Rotate x-axis labels
            fig.autofmt_xdate()

        except Exception as e:
            print(f"Error creating line chart: {e}")
            ax.text(0.5, 0.5, 'No data available', 
                   ha='center', va='center', fontsize=12, 
                   color=COLORS['fg_secondary'])
            ax.axis('off')

        fig.tight_layout()
        return fig

    def get_dashboard_stats(self, year, month):
        """Get statistics for dashboard"""
        try:
            monthly_data = self.data_manager.get_monthly_summary(year, month)

            # Handle empty data
            if len(monthly_data['data']) == 0 or 'Type' not in monthly_data['data'].columns:
                return {
                    'total_income': 0,
                    'total_expense': 0,
                    'net_balance': 0,
                    'top_categories': {},
                    'avg_daily_spending': 0,
                    'transaction_count': 0
                }

            # Top 3 categories by spending
            expenses_df = monthly_data['data'][monthly_data['data']['Type'] == 'Expense']

            if len(expenses_df) > 0:
                top_categories = expenses_df.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(3)
            else:
                top_categories = pd.Series(dtype='float64')

            # Calculate average daily spending
            days_in_month = calendar.monthrange(year, month)[1]
            avg_daily = monthly_data['total_expense'] / days_in_month if days_in_month > 0 else 0

            return {
                'total_income': monthly_data['total_income'],
                'total_expense': monthly_data['total_expense'],
                'net_balance': monthly_data['net_balance'],
                'top_categories': top_categories.to_dict(),
                'avg_daily_spending': avg_daily,
                'transaction_count': monthly_data['transaction_count']
            }
        except Exception as e:
            print(f"Error getting dashboard stats: {e}")
            import traceback
            traceback.print_exc()
            return {
                'total_income': 0,
                'total_expense': 0,
                'net_balance': 0,
                'top_categories': {},
                'avg_daily_spending': 0,
                'transaction_count': 0
            }
