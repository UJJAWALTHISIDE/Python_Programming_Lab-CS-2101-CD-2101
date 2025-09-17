import matplotlib.pyplot as plt

# Sales data (in thousands)
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Calculate total sales using loop
total_sales = 0
for sale in sales_data:
    total_sales += sale

# Calculate average sales
average_sales = total_sales / len(sales_data)

# Find month with highest sales using loop
max_sales = sales_data[0]
max_month_index = 0
for i in range(len(sales_data)):
    if sales_data[i] > max_sales:
        max_sales = sales_data[i]
        max_month_index = i

print(f"Total sales: {total_sales} thousand")
print(f"Average sales: {average_sales:.2f} thousand")
print(f"Highest sales: {max_sales} thousand in {months[max_month_index]}")

# Create the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(months, sales_data, color='skyblue')

# Highlight the month with highest sales
bars[max_month_index].set_color('red')

plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales (in thousands)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, value in enumerate(sales_data):
    plt.text(i, value + 1, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()