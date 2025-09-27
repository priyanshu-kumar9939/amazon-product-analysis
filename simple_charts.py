import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('default')

# Create images directory
import os
os.makedirs('images', exist_ok=True)

print("🎨 Creating Power BI-style visualizations...")

# Sample data
order_types = ['Electronics', 'Books', 'Clothing', 'Home & Garden']
order_counts = [8, 5, 4, 3]
revenue = [4799.92, 231.87, 509.89, 379.93]
regions = ['North', 'South', 'East', 'West']
regional_revenue = [1199.90, 1199.90, 1199.90, 1199.90]

# 1. Order Type Distribution (Pie Chart)
plt.figure(figsize=(10, 8))
colors = ['#4472C4', '#70AD47', '#FFC000', '#E74C3C']
plt.pie(order_counts, labels=order_types, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'fontsize': 12})
plt.title('Order Type Distribution', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('images/order_type_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Order Type Distribution chart saved")

# 2. Revenue by Order Type (Bar Chart)
plt.figure(figsize=(12, 8))
bars = plt.bar(order_types, revenue, color=colors)
plt.title('Revenue by Order Type', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Order Type', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)

# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 50,
             f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('images/revenue_by_order_type.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Revenue by Order Type chart saved")

# 3. Customer Segment Analysis (Donut Chart)
plt.figure(figsize=(10, 8))
segment_counts = [14, 6]  # Standard, Premium
segment_labels = ['Standard', 'Premium']
colors_segment = ['#FF6B6B', '#4ECDC4']
wedges, texts, autotexts = plt.pie(segment_counts, labels=segment_labels, 
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

# 4. Regional Performance (Bar Chart)
plt.figure(figsize=(12, 8))
bars = plt.bar(regions, regional_revenue, 
               color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
plt.title('Regional Performance', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 20,
             f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('images/regional_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Regional Performance chart saved")

# 5. KPI Cards
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Remove axes for KPI cards
for ax in [ax1, ax2, ax3, ax4]:
    ax.axis('off')

# KPI 1: Total Revenue
total_revenue = sum(revenue)
ax1.text(0.5, 0.5, f'${total_revenue:,.0f}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#2E86AB')
ax1.text(0.5, 0.3, 'Total Revenue', ha='center', va='center', 
         fontsize=14, color='#666666')

# KPI 2: Total Orders
total_orders = sum(order_counts)
ax2.text(0.5, 0.5, f'{total_orders}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#E74C3C')
ax2.text(0.5, 0.3, 'Total Orders', ha='center', va='center', 
         fontsize=14, color='#666666')

# KPI 3: Average Order Value
avg_order_value = total_revenue / total_orders
ax3.text(0.5, 0.5, f'${avg_order_value:.0f}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#27AE60')
ax3.text(0.5, 0.3, 'Avg Order Value', ha='center', va='center', 
         fontsize=14, color='#666666')

# KPI 4: Premium Customers
premium_customers = 6
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
print("📊 Total charts created: 5")
