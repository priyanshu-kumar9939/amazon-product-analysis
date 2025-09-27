import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and data
fig, ax = plt.subplots(figsize=(10, 6))

# Sample data for demonstration
categories = ['Electronics', 'Books', 'Clothing', 'Home & Garden']
values = [8, 5, 4, 3]
colors = ['#4472C4', '#70AD47', '#FFC000', '#E74C3C']

# Create bar chart
bars = ax.bar(categories, values, color=colors)
ax.set_title('Order Type Distribution', fontsize=16, fontweight='bold')
ax.set_ylabel('Number of Orders')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('images/sample_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print("Chart created successfully!")
