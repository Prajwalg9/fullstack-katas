"""
Configuration file for FinTrace Desktop
Contains constants, categories, colors, and paths
"""
import os

# Application Info
APP_NAME = "FinTrace Desktop"
APP_VERSION = "1.0.0"

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "Expenses.xlsx")
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

# Excel Column Headers
EXCEL_COLUMNS = [
    "ID", "Date", "Category", "Subcategory", "Type", "Amount", 
    "Tax (%)", "Tax Amount", "Total With Tax", "Payment Method", 
    "Description", "Created At", "Last Updated"
]

# Categories
CATEGORIES = [
    "Food", "Transport", "Rent", "Utilities", "Shopping", 
    "Salary", "Business", "Health", "Entertainment", "Education", "Other"
]

# Transaction Types
TRANSACTION_TYPES = ["Income", "Expense"]

# Payment Methods
PAYMENT_METHODS = ["Cash", "UPI", "Card", "NetBanking", "Wallet", "Other"]

# Dark Theme Colors
COLORS = {
    "bg_dark": "#1e1e1e",
    "bg_darker": "#121212",
    "bg_lighter": "#2d2d2d",
    "fg_primary": "#ffffff",
    "fg_secondary": "#e0e0e0",
    "fg_tertiary": "#b0b0b0",
    "accent": "#00bcd4",
    "accent_hover": "#00acc1",
    "success": "#4caf50",
    "warning": "#ff9800",
    "error": "#f44336",
    "income": "#4caf50",
    "expense": "#f44336",
    "border": "#3d3d3d"
}

# Font Settings
FONTS = {
    "family": "Segoe UI",
    "size_small": 9,
    "size_normal": 10,
    "size_medium": 11,
    "size_large": 14,
    "size_xlarge": 18
}

# Default Settings
DEFAULT_SETTINGS = {
    "default_tax": 5.0,
    "currency_symbol": "₹",
    "theme": "dark",
    "data_file": DATA_FILE,
    "window_width": 1200,
    "window_height": 700
}

# Chart Colors
CHART_COLORS = [
    "#00bcd4", "#ff9800", "#4caf50", "#f44336", "#9c27b0",
    "#ffeb3b", "#3f51b5", "#e91e63", "#00bcd4", "#8bc34a"
]
