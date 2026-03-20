"""
Main UI Module for FinTrace Desktop
Contains all frames, widgets, and theme setup
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import calendar
from config import *
from data_manager import DataManager
from reports import ReportGenerator


class DarkTheme:
    """Setup dark theme for the application"""

    @staticmethod
    def setup(root):
        style = ttk.Style(root)
        style.theme_use('clam')

        # Configure colors
        style.configure('TFrame', background=COLORS['bg_dark'])
        style.configure('TLabel', background=COLORS['bg_dark'], 
                       foreground=COLORS['fg_primary'], 
                       font=(FONTS['family'], FONTS['size_normal']))
        style.configure('Header.TLabel', font=(FONTS['family'], FONTS['size_large'], 'bold'))
        style.configure('Title.TLabel', font=(FONTS['family'], FONTS['size_xlarge'], 'bold'))

        style.configure('TButton', background=COLORS['accent'], 
                       foreground='white', 
                       borderwidth=0, 
                       focuscolor='none',
                       font=(FONTS['family'], FONTS['size_normal']))
        style.map('TButton',
                 background=[('active', COLORS['accent_hover'])],
                 foreground=[('active', 'white')])

        style.configure('TEntry', fieldbackground=COLORS['bg_lighter'], 
                       foreground=COLORS['fg_primary'],
                       borderwidth=1,
                       insertcolor=COLORS['fg_primary'])

        style.configure('TCombobox', fieldbackground=COLORS['bg_lighter'],
                       background=COLORS['bg_lighter'],
                       foreground=COLORS['fg_primary'],
                       borderwidth=1,
                       arrowcolor=COLORS['fg_primary'])

        style.map('TCombobox',
                 fieldbackground=[('readonly', COLORS['bg_lighter'])],
                 selectbackground=[('readonly', COLORS['bg_lighter'])],
                 selectforeground=[('readonly', COLORS['fg_primary'])])

        style.configure('Treeview', background=COLORS['bg_lighter'],
                       foreground=COLORS['fg_primary'],
                       fieldbackground=COLORS['bg_lighter'],
                       borderwidth=0,
                       font=(FONTS['family'], FONTS['size_normal']))
        style.configure('Treeview.Heading', background=COLORS['bg_darker'],
                       foreground=COLORS['fg_primary'],
                       borderwidth=1,
                       font=(FONTS['family'], FONTS['size_normal'], 'bold'))
        style.map('Treeview', background=[('selected', COLORS['accent'])],
                 foreground=[('selected', 'white')])

        style.configure('Vertical.TScrollbar', background=COLORS['bg_lighter'],
                       troughcolor=COLORS['bg_darker'],
                       borderwidth=0,
                       arrowcolor=COLORS['fg_primary'])

        style.configure('Nav.TButton', background=COLORS['bg_lighter'],
                       foreground=COLORS['fg_primary'],
                       borderwidth=0,
                       padding=10,
                       font=(FONTS['family'], FONTS['size_medium']))
        style.map('Nav.TButton',
                 background=[('active', COLORS['accent'])],
                 foreground=[('active', 'white')])


class DashboardFrame(ttk.Frame):
    """Dashboard screen with stats and charts"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='TFrame')
        self.canvas_widget = None
        self.setup_ui()

    def setup_ui(self):
        # Title
        title = ttk.Label(self, text="Dashboard", style='Title.TLabel')
        title.pack(pady=20, padx=20, anchor='w')

        # Stats container
        stats_frame = ttk.Frame(self)
        stats_frame.pack(fill='x', padx=20, pady=10)

        self.income_label = self.create_stat_box(stats_frame, "Total Income", "₹0", COLORS['income'], 0)
        self.expense_label = self.create_stat_box(stats_frame, "Total Expenses", "₹0", COLORS['expense'], 1)
        self.balance_label = self.create_stat_box(stats_frame, "Net Balance", "₹0", COLORS['accent'], 2)

        # Top categories
        top_cat_frame = ttk.Frame(self)
        top_cat_frame.pack(fill='x', padx=20, pady=10)

        ttk.Label(top_cat_frame, text="Top 3 Spending Categories", 
                 style='Header.TLabel').pack(anchor='w', pady=5)

        self.top_cat_text = tk.Text(top_cat_frame, height=4, width=50,
                                    bg=COLORS['bg_lighter'], fg=COLORS['fg_primary'],
                                    font=(FONTS['family'], FONTS['size_normal']),
                                    relief='flat', padx=10, pady=5)
        self.top_cat_text.pack(fill='x')

        # Chart area
        chart_frame = ttk.Frame(self)
        chart_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.chart_container = ttk.Frame(chart_frame)
        self.chart_container.pack(fill='both', expand=True)

        # Refresh button
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill='x', padx=20, pady=10)
        ttk.Button(btn_frame, text="Refresh Dashboard", 
                  command=self.refresh_dashboard).pack(side='left')

    def create_stat_box(self, parent, title, value, color, col):
        frame = tk.Frame(parent, bg=COLORS['bg_lighter'], padx=20, pady=15)
        frame.grid(row=0, column=col, padx=10, sticky='ew')
        parent.columnconfigure(col, weight=1)

        tk.Label(frame, text=title, bg=COLORS['bg_lighter'], 
                fg=COLORS['fg_secondary'], 
                font=(FONTS['family'], FONTS['size_normal'])).pack()

        value_label = tk.Label(frame, text=value, bg=COLORS['bg_lighter'], 
                              fg=color, font=(FONTS['family'], FONTS['size_xlarge'], 'bold'))
        value_label.pack()

        return value_label

    def refresh_dashboard(self):
        """Refresh dashboard with current month data"""
        now = datetime.now()
        stats = self.controller.report_gen.get_dashboard_stats(now.year, now.month)

        # Update stat boxes
        currency = self.controller.settings.get('currency_symbol', '₹')
        self.income_label.config(text=f"{currency}{stats['total_income']:,.2f}")
        self.expense_label.config(text=f"{currency}{stats['total_expense']:,.2f}")

        balance_color = COLORS['income'] if stats['net_balance'] >= 0 else COLORS['expense']
        self.balance_label.config(text=f"{currency}{stats['net_balance']:,.2f}", 
                                 fg=balance_color)

        # Update top categories
        self.top_cat_text.delete('1.0', 'end')
        if stats['top_categories']:
            for i, (cat, amount) in enumerate(stats['top_categories'].items(), 1):
                self.top_cat_text.insert('end', f"{i}. {cat}: {currency}{amount:,.2f}\n")
        else:
            self.top_cat_text.insert('end', "No expense data yet")

        # Update chart
        self.update_chart(now.year, now.month)

    def update_chart(self, year, month):
        """Update the dashboard chart"""
        # Clear existing chart
        for widget in self.chart_container.winfo_children():
            widget.destroy()

        # Create new chart
        fig = self.controller.report_gen.create_category_pie_chart(year, month)

        self.canvas_widget = FigureCanvasTkAgg(fig, self.chart_container)
        self.canvas_widget.draw()
        self.canvas_widget.get_tk_widget().pack(fill='both', expand=True)


class TransactionFormFrame(ttk.Frame):
    """Add/Edit transaction form"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='TFrame')
        self.current_id = None
        self.setup_ui()

    def setup_ui(self):
        # Title
        self.title_label = ttk.Label(self, text="Add Transaction", style='Title.TLabel')
        self.title_label.pack(pady=20, padx=20, anchor='w')

        # Form container
        form_frame = ttk.Frame(self)
        form_frame.pack(fill='both', expand=True, padx=40, pady=10)

        row = 0

        # Date
        ttk.Label(form_frame, text="Date *").grid(row=row, column=0, sticky='w', pady=5)
        self.date_entry = DateEntry(form_frame, width=30, background=COLORS['accent'],
                                    foreground='white', borderwidth=2, 
                                    date_pattern='dd-mm-yyyy')
        self.date_entry.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        row += 1

        # Type
        ttk.Label(form_frame, text="Type *").grid(row=row, column=0, sticky='w', pady=5)
        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(form_frame, textvariable=self.type_var, 
                                       values=TRANSACTION_TYPES, state='readonly', width=28)
        self.type_combo.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        self.type_combo.current(1)  # Default to Expense
        row += 1

        # Category
        ttk.Label(form_frame, text="Category *").grid(row=row, column=0, sticky='w', pady=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(form_frame, textvariable=self.category_var, 
                                          values=CATEGORIES, width=28)
        self.category_combo.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        row += 1

        # Subcategory
        ttk.Label(form_frame, text="Subcategory").grid(row=row, column=0, sticky='w', pady=5)
        self.subcategory_var = tk.StringVar()
        self.subcategory_entry = ttk.Entry(form_frame, textvariable=self.subcategory_var, width=30)
        self.subcategory_entry.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        row += 1

        # Amount
        ttk.Label(form_frame, text="Amount *").grid(row=row, column=0, sticky='w', pady=5)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(form_frame, textvariable=self.amount_var, width=30)
        self.amount_entry.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        row += 1

        # Tax
        ttk.Label(form_frame, text="Tax (%)").grid(row=row, column=0, sticky='w', pady=5)
        self.tax_var = tk.StringVar(value=str(self.controller.settings.get('default_tax', 5.0)))
        self.tax_entry = ttk.Entry(form_frame, textvariable=self.tax_var, width=30)
        self.tax_entry.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        row += 1

        # Payment Method
        ttk.Label(form_frame, text="Payment Method").grid(row=row, column=0, sticky='w', pady=5)
        self.payment_var = tk.StringVar()
        self.payment_combo = ttk.Combobox(form_frame, textvariable=self.payment_var, 
                                         values=PAYMENT_METHODS, state='readonly', width=28)
        self.payment_combo.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        self.payment_combo.current(0)
        row += 1

        # Description
        ttk.Label(form_frame, text="Description").grid(row=row, column=0, sticky='nw', pady=5)
        self.description_text = tk.Text(form_frame, height=4, width=30,
                                       bg=COLORS['bg_lighter'], fg=COLORS['fg_primary'],
                                       font=(FONTS['family'], FONTS['size_normal']),
                                       relief='solid', borderwidth=1)
        self.description_text.grid(row=row, column=1, sticky='ew', pady=5, padx=10)
        row += 1

        # Buttons
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=row, column=0, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Save", command=self.save_transaction).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_form).pack(side='left', padx=5)

        form_frame.columnconfigure(1, weight=1)

    def save_transaction(self):
        """Validate and save transaction"""
        # Validate required fields
        if not self.type_var.get():
            messagebox.showerror("Error", "Please select transaction type")
            return

        if not self.category_var.get():
            messagebox.showerror("Error", "Please select a category")
            return

        if not self.amount_var.get():
            messagebox.showerror("Error", "Please enter an amount")
            return

        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number")
            return

        try:
            tax = float(self.tax_var.get()) if self.tax_var.get() else 0
        except ValueError:
            messagebox.showerror("Error", "Invalid tax percentage")
            return

        # Prepare transaction data
        transaction_data = {
            'Date': self.date_entry.get_date().strftime("%Y-%m-%d"),
            'Type': self.type_var.get(),
            'Category': self.category_var.get(),
            'Subcategory': self.subcategory_var.get(),
            'Amount': amount,
            'Tax (%)': tax,
            'Payment Method': self.payment_var.get(),
            'Description': self.description_text.get('1.0', 'end-1c')
        }

        # Save or update
        if self.current_id:
            success = self.controller.data_manager.update_transaction(self.current_id, transaction_data)
            msg = "Transaction updated successfully"
        else:
            success = self.controller.data_manager.add_transaction(transaction_data)
            msg = "Transaction added successfully"

        if success:
            messagebox.showinfo("Success", msg)
            self.clear_form()
            self.controller.refresh_all()
        else:
            messagebox.showerror("Error", "Failed to save transaction")

    def clear_form(self):
        """Clear all form fields"""
        self.current_id = None
        self.title_label.config(text="Add Transaction")
        self.date_entry.set_date(datetime.now())
        self.type_combo.current(1)
        self.category_var.set('')
        self.subcategory_var.set('')
        self.amount_var.set('')
        self.tax_var.set(str(self.controller.settings.get('default_tax', 5.0)))
        self.payment_combo.current(0)
        self.description_text.delete('1.0', 'end')

    def load_transaction(self, transaction_id):
        """Load transaction for editing"""
        transaction = self.controller.data_manager.get_transaction_by_id(transaction_id)
        if not transaction:
            return

        self.current_id = transaction_id
        self.title_label.config(text="Edit Transaction")

        # Load values
        try:
            self.date_entry.set_date(pd.to_datetime(transaction['Date']))
        except:
            pass

        self.type_var.set(transaction['Type'])
        self.category_var.set(transaction['Category'])
        self.subcategory_var.set(transaction.get('Subcategory', ''))
        self.amount_var.set(str(transaction['Amount']))
        self.tax_var.set(str(transaction.get('Tax (%)', 0)))
        self.payment_var.set(transaction.get('Payment Method', 'Cash'))
        self.description_text.delete('1.0', 'end')
        self.description_text.insert('1.0', transaction.get('Description', ''))


class TransactionsTableFrame(ttk.Frame):
    """Transaction table view with filters"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='TFrame')
        self.current_filters = {}
        self.setup_ui()

    def setup_ui(self):
        # Title
        ttk.Label(self, text="Transactions", style='Title.TLabel').pack(pady=20, padx=20, anchor='w')

        # Filter frame
        filter_frame = ttk.Frame(self)
        filter_frame.pack(fill='x', padx=20, pady=10)

        # Row 1
        row1 = ttk.Frame(filter_frame)
        row1.pack(fill='x', pady=5)

        ttk.Label(row1, text="From:").pack(side='left', padx=5)
        self.date_from = DateEntry(row1, width=12, background=COLORS['accent'],
                                   foreground='white', borderwidth=2)
        self.date_from.pack(side='left', padx=5)

        ttk.Label(row1, text="To:").pack(side='left', padx=5)
        self.date_to = DateEntry(row1, width=12, background=COLORS['accent'],
                                foreground='white', borderwidth=2)
        self.date_to.pack(side='left', padx=5)

        ttk.Label(row1, text="Type:").pack(side='left', padx=5)
        self.type_filter = ttk.Combobox(row1, values=['All'] + TRANSACTION_TYPES, 
                                       state='readonly', width=10)
        self.type_filter.current(0)
        self.type_filter.pack(side='left', padx=5)

        ttk.Label(row1, text="Category:").pack(side='left', padx=5)
        self.category_filter = ttk.Combobox(row1, values=['All'] + CATEGORIES, 
                                           state='readonly', width=12)
        self.category_filter.current(0)
        self.category_filter.pack(side='left', padx=5)

        # Row 2
        row2 = ttk.Frame(filter_frame)
        row2.pack(fill='x', pady=5)

        ttk.Label(row2, text="Search:").pack(side='left', padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(row2, textvariable=self.search_var, width=30)
        search_entry.pack(side='left', padx=5)

        ttk.Button(row2, text="Apply Filters", command=self.apply_filters).pack(side='left', padx=5)
        ttk.Button(row2, text="Reset", command=self.reset_filters).pack(side='left', padx=5)
        ttk.Button(row2, text="Export CSV", command=self.export_csv).pack(side='left', padx=5)

        # Table frame
        table_frame = ttk.Frame(self)
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)

        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical")
        vsb.pack(side='right', fill='y')

        hsb = ttk.Scrollbar(table_frame, orient="horizontal")
        hsb.pack(side='bottom', fill='x')

        # Treeview
        columns = ('ID', 'Date', 'Type', 'Category', 'Amount', 'Tax Amount', 
                  'Total With Tax', 'Payment Method', 'Description')

        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings',
                                yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        # Configure columns
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Date', width=100, anchor='center')
        self.tree.column('Type', width=80, anchor='center')
        self.tree.column('Category', width=100, anchor='w')
        self.tree.column('Amount', width=100, anchor='e')
        self.tree.column('Tax Amount', width=100, anchor='e')
        self.tree.column('Total With Tax', width=120, anchor='e')
        self.tree.column('Payment Method', width=120, anchor='center')
        self.tree.column('Description', width=200, anchor='w')

        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by_column(c))

        self.tree.pack(fill='both', expand=True)

        # Context menu
        self.context_menu = tk.Menu(self.tree, tearoff=0, 
                                    bg=COLORS['bg_lighter'], fg=COLORS['fg_primary'])
        self.context_menu.add_command(label="Edit", command=self.edit_selected)
        self.context_menu.add_command(label="Delete", command=self.delete_selected)

        self.tree.bind('<Button-3>', self.show_context_menu)
        self.tree.bind('<Double-1>', lambda e: self.edit_selected())

        # Button frame
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill='x', padx=20, pady=10)

        ttk.Button(btn_frame, text="Edit Selected", command=self.edit_selected).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_table).pack(side='left', padx=5)

    def refresh_table(self, filters=None):
        """Refresh table with current data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get data
        if filters:
            df = self.controller.data_manager.filter_transactions(filters)
        else:
            df = self.controller.data_manager.get_all_transactions()

        # Populate table
        for _, row in df.iterrows():
            date_str = row['Date'].strftime('%d-%m-%Y') if pd.notna(row['Date']) else ''
            values = (
                int(row['ID']) if pd.notna(row['ID']) else '',
                date_str,
                row['Type'],
                row['Category'],
                f"{row['Amount']:.2f}" if pd.notna(row['Amount']) else '',
                f"{row['Tax Amount']:.2f}" if pd.notna(row['Tax Amount']) else '',
                f"{row['Total With Tax']:.2f}" if pd.notna(row['Total With Tax']) else '',
                row['Payment Method'],
                row['Description']
            )

            # Color code by type
            tag = 'income' if row['Type'] == 'Income' else 'expense'
            self.tree.insert('', 'end', values=values, tags=(tag,))

        # Configure tags
        self.tree.tag_configure('income', foreground=COLORS['income'])
        self.tree.tag_configure('expense', foreground=COLORS['expense'])

    def apply_filters(self):
        """Apply filters to table"""
        filters = {
            'date_from': self.date_from.get_date().strftime("%Y-%m-%d"),
            'date_to': self.date_to.get_date().strftime("%Y-%m-%d"),
            'type': self.type_filter.get(),
            'category': self.category_filter.get(),
            'search_text': self.search_var.get()
        }
        self.current_filters = filters
        self.refresh_table(filters)

    def reset_filters(self):
        """Reset all filters"""
        self.date_from.set_date(datetime.now() - timedelta(days=30))
        self.date_to.set_date(datetime.now())
        self.type_filter.current(0)
        self.category_filter.current(0)
        self.search_var.set('')
        self.current_filters = {}
        self.refresh_table()

    def sort_by_column(self, col):
        """Sort table by column"""
        # Get current data
        data = [(self.tree.set(item, col), item) for item in self.tree.get_children('')]

        # Sort data
        try:
            data.sort(key=lambda t: float(t[0].replace(',', '')))
        except:
            data.sort()

        # Rearrange items
        for index, (val, item) in enumerate(data):
            self.tree.move(item, '', index)

    def show_context_menu(self, event):
        """Show context menu on right-click"""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)

    def edit_selected(self):
        """Edit selected transaction"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a transaction")
            return

        item = selection[0]
        transaction_id = int(self.tree.item(item)['values'][0])

        # Switch to form and load transaction
        self.controller.show_frame('TransactionFormFrame')
        self.controller.frames['TransactionFormFrame'].load_transaction(transaction_id)

    def delete_selected(self):
        """Delete selected transaction"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a transaction")
            return

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this transaction?"):
            item = selection[0]
            transaction_id = int(self.tree.item(item)['values'][0])

            if self.controller.data_manager.delete_transaction(transaction_id):
                messagebox.showinfo("Success", "Transaction deleted successfully")
                self.controller.refresh_all()
            else:
                messagebox.showerror("Error", "Failed to delete transaction")

    def export_csv(self):
        """Export current view to CSV"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if file_path:
            if self.current_filters:
                df = self.controller.data_manager.filter_transactions(self.current_filters)
            else:
                df = self.controller.data_manager.get_all_transactions()

            if self.controller.data_manager.export_to_csv(file_path):
                messagebox.showinfo("Success", f"Data exported to {file_path}")
            else:
                messagebox.showerror("Error", "Failed to export data")


class ReportsFrame(ttk.Frame):
    """Reports and charts screen"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='TFrame')
        self.canvas_widget = None
        self.setup_ui()

    def setup_ui(self):
        # Title
        ttk.Label(self, text="Reports & Charts", style='Title.TLabel').pack(pady=20, padx=20, anchor='w')

        # Control frame
        control_frame = ttk.Frame(self)
        control_frame.pack(fill='x', padx=20, pady=10)

        ttk.Label(control_frame, text="Report Type:").pack(side='left', padx=5)
        self.report_type = ttk.Combobox(control_frame, 
                                       values=['Monthly Summary', 'Category Summary', 'Income vs Expense'],
                                       state='readonly', width=20)
        self.report_type.current(0)
        self.report_type.pack(side='left', padx=5)

        ttk.Label(control_frame, text="Month:").pack(side='left', padx=5)
        months = list(range(1, 13))
        self.month_combo = ttk.Combobox(control_frame, values=months, state='readonly', width=5)
        self.month_combo.current(datetime.now().month - 1)
        self.month_combo.pack(side='left', padx=5)

        ttk.Label(control_frame, text="Year:").pack(side='left', padx=5)
        current_year = datetime.now().year
        years = list(range(current_year - 5, current_year + 1))
        self.year_combo = ttk.Combobox(control_frame, values=years, state='readonly', width=8)
        self.year_combo.set(current_year)
        self.year_combo.pack(side='left', padx=5)

        ttk.Button(control_frame, text="Generate Report", 
                  command=self.generate_report).pack(side='left', padx=10)

        # Stats frame
        stats_frame = ttk.Frame(self)
        stats_frame.pack(fill='x', padx=20, pady=10)

        self.stats_label = tk.Label(stats_frame, text="", bg=COLORS['bg_lighter'],
                                    fg=COLORS['fg_primary'], 
                                    font=(FONTS['family'], FONTS['size_normal']),
                                    padx=20, pady=15, anchor='w', justify='left')
        self.stats_label.pack(fill='x')

        # Chart frame
        chart_frame = ttk.Frame(self)
        chart_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.chart_container = ttk.Frame(chart_frame)
        self.chart_container.pack(fill='both', expand=True)

    def generate_report(self):
        """Generate selected report"""
        report_type = self.report_type.get()
        month = int(self.month_combo.get())
        year = int(self.year_combo.get())

        # Clear existing chart
        for widget in self.chart_container.winfo_children():
            widget.destroy()

        currency = self.controller.settings.get('currency_symbol', '₹')

        if report_type == 'Monthly Summary':
            # Get monthly stats
            summary = self.controller.data_manager.get_monthly_summary(year, month)

            stats_text = f"""
            Month: {calendar.month_name[month]} {year}
            Total Income: {currency}{summary['total_income']:,.2f}
            Total Expense: {currency}{summary['total_expense']:,.2f}
            Net Savings: {currency}{summary['net_balance']:,.2f}
            Transactions: {summary['transaction_count']}
            """

            self.stats_label.config(text=stats_text)

            # Create chart
            fig = self.controller.report_gen.create_monthly_bar_chart(year, month)

        elif report_type == 'Category Summary':
            # Get category summary
            category_summary = self.controller.data_manager.get_category_summary('Expense')

            if len(category_summary) > 0:
                stats_text = f"Top Expense Categories ({calendar.month_name[month]} {year}):\n\n"
                for cat, amount in category_summary.head(5).items():
                    stats_text += f"{cat}: {currency}{amount:,.2f}\n"
            else:
                stats_text = "No expense data available"

            self.stats_label.config(text=stats_text)

            # Create chart
            fig = self.controller.report_gen.create_category_pie_chart(year, month)

        else:  # Income vs Expense
            # Date range for last 30 days
            end_date = datetime(year, month, calendar.monthrange(year, month)[1])
            start_date = datetime(year, month, 1)

            filters = {
                'date_from': start_date.strftime("%Y-%m-%d"),
                'date_to': end_date.strftime("%Y-%m-%d")
            }

            df = self.controller.data_manager.filter_transactions(filters)

            total_income = df[df['Type'] == 'Income']['Amount'].sum() if len(df) > 0 else 0
            total_expense = df[df['Type'] == 'Expense']['Amount'].sum() if len(df) > 0 else 0

            stats_text = f"""
            Period: {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')}
            Total Income: {currency}{total_income:,.2f}
            Total Expense: {currency}{total_expense:,.2f}
            Net Balance: {currency}{total_income - total_expense:,.2f}
            """

            self.stats_label.config(text=stats_text)

            # Create chart
            fig = self.controller.report_gen.create_income_expense_line_chart(
                start_date.strftime("%Y-%m-%d"), 
                end_date.strftime("%Y-%m-%d")
            )

        # Display chart
        self.canvas_widget = FigureCanvasTkAgg(fig, self.chart_container)
        self.canvas_widget.draw()
        self.canvas_widget.get_tk_widget().pack(fill='both', expand=True)


class SettingsFrame(ttk.Frame):
    """Settings screen"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='TFrame')
        self.setup_ui()

    def setup_ui(self):
        # Title
        ttk.Label(self, text="Settings", style='Title.TLabel').pack(pady=20, padx=20, anchor='w')

        # Settings container
        settings_frame = ttk.Frame(self)
        settings_frame.pack(fill='both', expand=True, padx=40, pady=10)

        row = 0

        # Default Tax
        ttk.Label(settings_frame, text="Default Tax (%):").grid(row=row, column=0, sticky='w', pady=10)
        self.tax_var = tk.StringVar(value=str(self.controller.settings.get('default_tax', 5.0)))
        ttk.Entry(settings_frame, textvariable=self.tax_var, width=20).grid(row=row, column=1, sticky='w', padx=10)
        row += 1

        # Currency Symbol
        ttk.Label(settings_frame, text="Currency Symbol:").grid(row=row, column=0, sticky='w', pady=10)
        self.currency_var = tk.StringVar(value=self.controller.settings.get('currency_symbol', '₹'))
        ttk.Entry(settings_frame, textvariable=self.currency_var, width=20).grid(row=row, column=1, sticky='w', padx=10)
        row += 1

        # Data File Path
        ttk.Label(settings_frame, text="Data File Path:").grid(row=row, column=0, sticky='w', pady=10)
        path_frame = ttk.Frame(settings_frame)
        path_frame.grid(row=row, column=1, sticky='ew', padx=10)

        self.path_var = tk.StringVar(value=self.controller.settings.get('data_file', DATA_FILE))
        ttk.Entry(path_frame, textvariable=self.path_var, width=40).pack(side='left', padx=(0, 5))
        ttk.Button(path_frame, text="Browse", command=self.browse_file).pack(side='left')
        row += 1

        # Theme
        ttk.Label(settings_frame, text="Theme:").grid(row=row, column=0, sticky='w', pady=10)
        self.theme_var = tk.StringVar(value=self.controller.settings.get('theme', 'dark'))
        theme_combo = ttk.Combobox(settings_frame, textvariable=self.theme_var, 
                                   values=['dark', 'light'], state='readonly', width=17)
        theme_combo.grid(row=row, column=1, sticky='w', padx=10)
        row += 1

        # Buttons
        btn_frame = ttk.Frame(settings_frame)
        btn_frame.grid(row=row, column=0, columnspan=2, pady=30)

        ttk.Button(btn_frame, text="Save Settings", command=self.save_settings).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Reset to Defaults", command=self.reset_defaults).pack(side='left', padx=5)

        settings_frame.columnconfigure(1, weight=1)

    def browse_file(self):
        """Browse for data file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if file_path:
            self.path_var.set(file_path)

    def save_settings(self):
        """Save settings"""
        try:
            self.controller.settings['default_tax'] = float(self.tax_var.get())
            self.controller.settings['currency_symbol'] = self.currency_var.get()
            self.controller.settings['data_file'] = self.path_var.get()
            self.controller.settings['theme'] = self.theme_var.get()

            self.controller.save_settings()
            messagebox.showinfo("Success", "Settings saved successfully")
        except ValueError:
            messagebox.showerror("Error", "Invalid tax percentage")

    def reset_defaults(self):
        """Reset to default settings"""
        if messagebox.askyesno("Confirm Reset", "Reset all settings to defaults?"):
            self.controller.settings = DEFAULT_SETTINGS.copy()
            self.controller.save_settings()

            # Update UI
            self.tax_var.set(str(DEFAULT_SETTINGS['default_tax']))
            self.currency_var.set(DEFAULT_SETTINGS['currency_symbol'])
            self.path_var.set(DEFAULT_SETTINGS['data_file'])
            self.theme_var.set(DEFAULT_SETTINGS['theme'])

            messagebox.showinfo("Success", "Settings reset to defaults")


class FinTraceApp:
    """Main application controller"""

    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME + " v" + APP_VERSION)

        # Load settings
        self.settings = self.load_settings()

        # Set window size and position
        window_width = self.settings.get('window_width', 1200)
        window_height = self.settings.get('window_height', 700)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg=COLORS['bg_dark'])

        # Setup theme
        DarkTheme.setup(root)

        # Initialize data manager and report generator
        self.data_manager = DataManager(self.settings.get('data_file', DATA_FILE))
        self.report_gen = ReportGenerator(self.data_manager)

        # Setup UI
        self.setup_ui()

        # Setup keyboard shortcuts
        self.setup_shortcuts()

        # Show initial screen
        self.show_frame('DashboardFrame')
        self.frames['DashboardFrame'].refresh_dashboard()

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_settings(self):
        """Load settings from file"""
        if os.path.exists(SETTINGS_FILE):
            try:
                import json
                with open(SETTINGS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return DEFAULT_SETTINGS.copy()
        return DEFAULT_SETTINGS.copy()

    def save_settings(self):
        """Save settings to file"""
        try:
            import json
            with open(SETTINGS_FILE, 'w') as f:
                json.dump(self.settings, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False

    def setup_ui(self):
        """Setup main UI structure"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill='both', expand=True)

        # Navigation sidebar
        nav_frame = tk.Frame(main_container, bg=COLORS['bg_darker'], width=200)
        nav_frame.pack(side='left', fill='y')
        nav_frame.pack_propagate(False)

        # App title in sidebar
        title_label = tk.Label(nav_frame, text=APP_NAME, 
                              bg=COLORS['bg_darker'], fg=COLORS['accent'],
                              font=(FONTS['family'], FONTS['size_large'], 'bold'))
        title_label.pack(pady=30, padx=10)

        # Navigation buttons
        nav_buttons = [
            ("📊 Dashboard", 'DashboardFrame'),
            ("➕ Add Transaction", 'TransactionFormFrame'),
            ("📋 Transactions", 'TransactionsTableFrame'),
            ("📈 Reports", 'ReportsFrame'),
            ("⚙️ Settings", 'SettingsFrame')
        ]

        self.nav_btn_refs = {}
        for text, frame_name in nav_buttons:
            btn = tk.Button(nav_frame, text=text, 
                          bg=COLORS['bg_lighter'], fg=COLORS['fg_primary'],
                          font=(FONTS['family'], FONTS['size_medium']),
                          bd=0, padx=20, pady=15, anchor='w',
                          activebackground=COLORS['accent'],
                          activeforeground='white',
                          cursor='hand2',
                          command=lambda f=frame_name: self.show_frame(f))
            btn.pack(fill='x', padx=10, pady=2)
            self.nav_btn_refs[frame_name] = btn

        # Content area
        self.content_frame = ttk.Frame(main_container)
        self.content_frame.pack(side='right', fill='both', expand=True)

        # Initialize frames
        self.frames = {}

        for FrameClass in (DashboardFrame, TransactionFormFrame, 
                          TransactionsTableFrame, ReportsFrame, SettingsFrame):
            frame = FrameClass(self.content_frame, self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

    def show_frame(self, frame_name):
        """Show a specific frame"""
        frame = self.frames[frame_name]
        frame.tkraise()

        # Update nav button highlights
        for name, btn in self.nav_btn_refs.items():
            if name == frame_name:
                btn.config(bg=COLORS['accent'], fg='white')
            else:
                btn.config(bg=COLORS['bg_lighter'], fg=COLORS['fg_primary'])

    def refresh_all(self):
        """Refresh all frames with updated data"""
        # Refresh dashboard
        self.frames['DashboardFrame'].refresh_dashboard()

        # Refresh transactions table
        self.frames['TransactionsTableFrame'].refresh_table()

    def setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.root.bind('<Control-n>', lambda e: self.show_frame('TransactionFormFrame'))
        self.root.bind('<Control-f>', lambda e: self.show_frame('TransactionsTableFrame'))
        self.root.bind('<Control-q>', lambda e: self.on_closing())

    def on_closing(self):
        """Handle window close event"""
        # Save window size
        self.settings['window_width'] = self.root.winfo_width()
        self.settings['window_height'] = self.root.winfo_height()
        self.save_settings()

        # Close application
        self.root.destroy()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = FinTraceApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
