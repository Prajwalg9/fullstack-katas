"""
FinTrace Desktop - Personal Finance Tracker
Entry point for the application

Installation Instructions:
---------------------------
Before running this application, install required packages:

pip install pandas openpyxl matplotlib tkcalendar

Requirements:
- Python 3.7+
- pandas: Data manipulation and Excel operations
- openpyxl: Excel file reading/writing
- matplotlib: Chart generation
- tkcalendar: Calendar date picker widget

Usage:
------
Run this file to start the application:
    python main.py

Features:
---------
- Track income and expenses with detailed categorization
- Dark theme UI with modern design
- Dashboard with visual charts and statistics
- Filter and search transactions
- Generate reports and export data
- Configurable settings (tax, currency, etc.)
- Excel-based storage (easy to migrate to SQLite later)
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Check for required packages
try:
    import pandas
    import openpyxl
    import matplotlib
    import tkcalendar
    import tkinter
except ImportError as e:
    print("\n" + "="*60)
    print("ERROR: Missing required package!")
    print("="*60)
    print(f"\nMissing: {e.name}\n")
    print("Please install required packages using:")
    print("\n    pip install pandas openpyxl matplotlib tkcalendar\n")
    print("="*60)
    sys.exit(1)

# Import the main app
from ui_main import main

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Starting FinTrace Desktop...")
    print("="*60 + "\n")

    # Check if this is first run
    from config import DATA_FILE
    if not os.path.exists(DATA_FILE):
        print("First run detected!")
        print(f"Creating data file: {DATA_FILE}")
        print("\nwelcome to FinTrace Desktop!")
        print("Start by adding your first transaction.\n")

    # Run the application
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication closed by user.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()

    print("\nThank you for using FinTrace Desktop!")
