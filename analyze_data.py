#!/usr/bin/env python3
"""
Amazon Product Analysis - Data Explorer
This script analyzes the order_type.xlsx file and generates insights
"""

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from datetime import datetime
    import warnings
    warnings.filterwarnings('ignore')
    
    # Read the Excel file
    print("📊 Loading data from order_type.xlsx...")
    df = pd.read_excel('order_type.xlsx')
    
    print(f"\n📈 Dataset Overview:")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Columns: {list(df.columns)}")
    
    print(f"\n📋 First 5 rows:")
    print(df.head().to_string())
    
    print(f"\n🔍 Data Types:")
    print(df.dtypes.to_string())
    
    print(f"\n📊 Basic Statistics:")
    print(df.describe().to_string())
    
    print(f"\n🔍 Missing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0].to_string() if missing.sum() > 0 else "No missing values found!")
    
    # Generate insights
    print(f"\n💡 Key Insights:")
    
    # If there are numeric columns, show some basic analysis
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print(f"📊 Numeric columns found: {list(numeric_cols)}")
        for col in numeric_cols:
            print(f"  - {col}: min={df[col].min()}, max={df[col].max()}, mean={df[col].mean():.2f}")
    
    # If there are categorical columns, show value counts
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        print(f"📝 Categorical columns found: {list(categorical_cols)}")
        for col in categorical_cols:
            print(f"  - {col}: {df[col].nunique()} unique values")
            print(f"    Top values: {df[col].value_counts().head(3).to_dict()}")
    
    # Save data as CSV for better GitHub display
    print(f"\n💾 Saving data as CSV for GitHub display...")
    df.to_csv('order_data.csv', index=False)
    print("✅ Data saved as order_data.csv")
    
    # Create a summary report
    with open('data_summary.txt', 'w') as f:
        f.write("AMAZON PRODUCT ANALYSIS - DATA SUMMARY\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Dataset: order_type.xlsx\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
        f.write(f"Columns: {list(df.columns)}\n\n")
        f.write("Data Types:\n")
        f.write(df.dtypes.to_string())
        f.write("\n\nBasic Statistics:\n")
        f.write(df.describe().to_string())
        f.write("\n\nMissing Values:\n")
        f.write(missing.to_string())
    
    print("✅ Summary report saved as data_summary.txt")
    
except ImportError as e:
    print(f"❌ Missing required packages: {e}")
    print("Please install: pip install pandas openpyxl matplotlib seaborn")
except Exception as e:
    print(f"❌ Error analyzing data: {e}")
    print("Please check if order_type.xlsx exists and is readable")
