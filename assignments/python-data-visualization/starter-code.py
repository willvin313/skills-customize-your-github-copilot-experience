import matplotlib.pyplot as plt
import pandas as pd

# Sample data for demonstration
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [23, 45, 12, 36]
}
df = pd.DataFrame(data)

# Bar chart
plt.figure(figsize=(6,4))
plt.bar(df['Category'], df['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart Example')
plt.show()

# Line chart
plt.figure(figsize=(6,4))
plt.plot(df['Category'], df['Value'], marker='o')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Line Chart Example')
plt.show()

# You can add more visualizations below for Task 2
