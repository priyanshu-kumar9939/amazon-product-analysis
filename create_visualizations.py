#!/usr/bin/env python3
"""
Create Power BI-style visualizations for GitHub display
This script generates professional charts and saves them as images
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set Power BI style
plt.style.use('default')
sns.set_palette("husl")

# Read the data
df = pd.read_csv('order_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Create the images directory if it doesn't exist
import os
os.makedirs('images', exist_ok=True)

print("🎨 Creating Power BI-style visualizations...")

# 1. Order Type Distribution (Pie Chart)
plt.figure(figsize=(10, 8))
order_counts = df['Order_Type'].value_counts()
colors = ['#4472C4', '#70AD47', '#FFC000', '#E74C3C']
plt.pie(order_counts.values, labels=order_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'fontsize': 12})
plt.title('Order Type Distribution', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('images/order_type_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Order Type Distribution chart saved")

# 2. Revenue by Order Type (Bar Chart)
plt.figure(figsize=(12, 8))
revenue_by_type = df.groupby('Order_Type')['Value'].sum().sort_values(ascending=True)
bars = plt.barh(revenue_by_type.index, revenue_by_type.values, color=colors)
plt.title('Revenue by Order Type', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Revenue ($)', fontsize=12)
plt.ylabel('Order Type', fontsize=12)

# Add value labels on bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 20, bar.get_y() + bar.get_height()/2, 
             f'${width:,.0f}', ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('images/revenue_by_order_type.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Revenue by Order Type chart saved")

# 3. Customer Segment Analysis (Donut Chart)
plt.figure(figsize=(10, 8))
segment_counts = df['Customer_Segment'].value_counts()
colors_segment = ['#FF6B6B', '#4ECDC4']
wedges, texts, autotexts = plt.pie(segment_counts.values, labels=segment_counts.index, 
                                   autopct='%1.1f%%', colors=colors_segment, 
                                   startangle=90, pctdistance=0.85)
# Create donut chart
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Customer Segment Distribution', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('images/customer_segment_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Customer Segment Analysis chart saved")

# 4. Daily Revenue Trend (Line Chart)
plt.figure(figsize=(14, 8))
daily_revenue = df.groupby('Date')['Value'].sum().reset_index()
plt.plot(daily_revenue['Date'], daily_revenue['Value'], marker='o', linewidth=3, 
         markersize=8, color='#2E86AB')
plt.title('Daily Revenue Trend', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('images/daily_revenue_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Daily Revenue Trend chart saved")

# 5. Regional Performance (Horizontal Bar Chart)
plt.figure(figsize=(12, 8))
regional_revenue = df.groupby('Region')['Value'].sum().sort_values(ascending=True)
bars = plt.barh(regional_revenue.index, regional_revenue.values, 
                color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
plt.title('Regional Performance', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Revenue ($)', fontsize=12)
plt.ylabel('Region', fontsize=12)

# Add value labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 20, bar.get_y() + bar.get_height()/2, 
             f'${width:,.0f}', ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('images/regional_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Regional Performance chart saved")

# 6. Average Order Value by Category (Bar Chart)
plt.figure(figsize=(12, 8))
avg_order_value = df.groupby('Order_Type')['Value'].mean().sort_values(ascending=False)
bars = plt.bar(avg_order_value.index, avg_order_value.values, color=colors)
plt.title('Average Order Value by Category', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Order Type', fontsize=12)
plt.ylabel('Average Order Value ($)', fontsize=12)
plt.xticks(rotation=45)

# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 10,
             f'${height:.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('images/avg_order_value_by_category.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Average Order Value chart saved")

# 7. Dashboard Overview (Multiple Charts)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# Top Left: Order Type Distribution
order_counts = df['Order_Type'].value_counts()
ax1.pie(order_counts.values, labels=order_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
ax1.set_title('Order Type Distribution', fontweight='bold')

# Top Right: Revenue by Segment
segment_revenue = df.groupby('Customer_Segment')['Value'].sum()
bars = ax2.bar(segment_revenue.index, segment_revenue.values, color=colors_segment)
ax2.set_title('Revenue by Customer Segment', fontweight='bold')
ax2.set_ylabel('Revenue ($)')
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 50,
             f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')

# Bottom Left: Daily Orders
daily_orders = df.groupby('Date').size()
ax3.plot(daily_orders.index, daily_orders.values, marker='o', linewidth=2, color='#2E86AB')
ax3.set_title('Daily Order Count', fontweight='bold')
ax3.set_ylabel('Number of Orders')
ax3.tick_params(axis='x', rotation=45)

# Bottom Right: Regional Distribution
regional_counts = df['Region'].value_counts()
bars = ax4.bar(regional_counts.index, regional_counts.values, 
               color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
ax4.set_title('Orders by Region', fontweight='bold')
ax4.set_ylabel('Number of Orders')
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.suptitle('Amazon Product Analysis - Dashboard Overview', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('images/dashboard_overview.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Dashboard Overview saved")

# 8. Power BI Style KPI Cards
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Remove axes for KPI cards
for ax in [ax1, ax2, ax3, ax4]:
    ax.axis('off')

# KPI 1: Total Revenue
total_revenue = df['Value'].sum()
ax1.text(0.5, 0.5, f'${total_revenue:,.0f}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#2E86AB')
ax1.text(0.5, 0.3, 'Total Revenue', ha='center', va='center', 
         fontsize=14, color='#666666')

# KPI 2: Total Orders
total_orders = len(df)
ax2.text(0.5, 0.5, f'{total_orders}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#E74C3C')
ax2.text(0.5, 0.3, 'Total Orders', ha='center', va='center', 
         fontsize=14, color='#666666')

# KPI 3: Average Order Value
avg_order_value = df['Value'].mean()
ax3.text(0.5, 0.5, f'${avg_order_value:.0f}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#27AE60')
ax3.text(0.5, 0.3, 'Avg Order Value', ha='center', va='center', 
         fontsize=14, color='#666666')

# KPI 4: Premium Customers
premium_customers = len(df[df['Customer_Segment'] == 'Premium'])
ax4.text(0.5, 0.5, f'{premium_customers}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#8E44AD')
ax4.text(0.5, 0.3, 'Premium Customers', ha='center', va='center', 
         fontsize=14, color='#666666')

plt.suptitle('Key Performance Indicators', fontsize=16, fontweight='bold', y=0.95)
plt.tight_layout()
plt.savefig('images/kpi_cards.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ KPI Cards saved")

print("\n🎉 All visualizations created successfully!")
print("📁 Images saved in the 'images' folder")
print("📊 Total charts created: 8")
