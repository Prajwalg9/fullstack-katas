# FinTrace Desktop - Personal Finance Tracker

A modern, feature-rich desktop application for tracking personal finances built with Python and Tkinter.

## Features

### 💰 Financial Tracking
- Track income and expenses with detailed categorization
- Add subcategories for better organization
- Automatic tax calculation
- Multiple payment method support
- Rich transaction descriptions

### 📊 Dashboard & Insights
- Quick summary of current month finances
- Visual charts (pie charts, bar charts, line graphs)
- Top spending categories
- Net balance calculation
- Average daily spending

### 📋 Transaction Management
- Complete transaction history in table view
- Advanced filtering (date range, category, type, amount, text search)
- Sort by any column
- Edit and delete transactions
- Export to CSV

### 📈 Reports & Analytics
- Monthly summary reports
- Category-wise expense breakdown
- Income vs Expense trends over time
- Visual charts with matplotlib integration
- Customizable date ranges

### ⚙️ Settings & Customization
- Configurable default tax percentage
- Custom currency symbol
- Dark theme UI (default)
- Persistent window size and position
- Changeable data file location

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Required Packages

```bash
pip install pandas openpyxl matplotlib tkcalendar
```

## Usage

1. Navigate to the application directory
2. Run the main file:

```bash
python main.py
```

3. On first run, the application will create an `Expenses.xlsx` file in the same directory

## Project Structure

```
FinTrace Desktop/
├── main.py              # Application entry point
├── ui_main.py           # Main UI with all frames
├── data_manager.py      # Excel/Pandas data operations
├── reports.py           # Chart generation and calculations
├── config.py            # Configuration and constants
├── Expenses.xlsx        # Data storage (created on first run)
└── settings.json        # User settings (created on first run)
```

## Keyboard Shortcuts

- `Ctrl+N` - New transaction (opens Add Transaction screen)
- `Ctrl+F` - Focus on Transactions screen
- `Ctrl+Q` - Quit application

## Data Storage

- **Primary Storage**: Excel file (`Expenses.xlsx`)
- **Format**: Structured with proper columns and data types
- **Architecture**: Designed for easy migration to SQLite with minimal code changes

### Excel Columns
- ID (auto-increment)
- Date
- Category
- Subcategory
- Type (Income/Expense)
- Amount
- Tax (%)
- Tax Amount (calculated)
- Total With Tax (calculated)
- Payment Method
- Description
- Created At
- Last Updated

## Default Categories

**Expense Categories:**
- Food
- Transport
- Rent
- Utilities
- Shopping
- Health
- Entertainment
- Education
- Other

**Income Categories:**
- Salary
- Business
- Other

## Payment Methods
- Cash
- UPI
- Card
- NetBanking
- Wallet
- Other

## Screenshots

### Dashboard
- Clean, modern dark theme interface
- Quick stats cards showing income, expenses, and balance
- Visual pie chart of expense categories
- Top 3 spending categories

### Add Transaction
- Simple, intuitive form
- Calendar date picker
- Dropdown selections for categories and payment methods
- Automatic tax calculation
- Multi-line description field

### Transactions Table
- Complete transaction history
- Advanced filtering options
- Sort by any column
- Right-click context menu for edit/delete
- Color-coded by type (green for income, red for expense)

### Reports
- Multiple report types
- Interactive charts
- Statistical summaries
- Export capabilities

## Technical Details

### Architecture
- **GUI Layer**: Tkinter with ttk for modern widgets
- **Data Layer**: Pandas and openpyxl for Excel operations
- **Logic Layer**: Separate modules for calculations and reports
- **Theme**: Custom dark theme with configurable colors

### Design Patterns
- Object-oriented structure
- Separation of concerns
- Controller pattern for app management
- Frame-based navigation

### Future Enhancements
- SQLite database migration option
- Budget planning and tracking
- Recurring transaction support
- Data backup and restore
- PIN lock for privacy
- Export charts as images
- Light theme option
- Multi-currency support

## Contributing

This is a personal finance tracker designed for individual use. Feel free to fork and customize for your needs.

## License

This project is open source and available for personal and educational use.

## Support

For issues or questions, refer to the code comments and documentation within each module.

---

**Version**: 1.0.0  
**Author**: FinTrace Desktop Development Team  
**Last Updated**: December 2024
