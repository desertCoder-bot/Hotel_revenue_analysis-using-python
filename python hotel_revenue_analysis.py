# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Step 1: Load data using pandas
df = pd.read_csv('hotel_bookings.csv')

# Step 2: Clean data (remove cancellations, fill missing values)
df = df[df['is_canceled'] == 0]  # Remove cancelled bookings
df.fillna(0, inplace=True)  # Fill missing values with 0

# Step 3: Show monthly revenue as bar chart
monthly_income = df.groupby('arrival_date_month')['adr'].sum().reindex([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])

plt.figure(figsize=(10, 6))
plt.bar(monthly_income.index, monthly_income.values, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Monthly Revenue')
plt.xticks(rotation=45)
plt.savefig('monthly_revenue.png')  # Save the plot as an image
plt.show()

# Step 4: Compare City vs Resort hotel income via pie chart
hotel_income = df.groupby('hotel')['adr'].sum()

plt.figure(figsize=(8, 8))
plt.pie(hotel_income, labels=hotel_income.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('City vs Resort Hotel Income')
plt.savefig('hotel_income_comparison.png')  # Save the plot as an image
plt.show()

# Step 5: Create boxplot of room prices by customer type
plt.figure(figsize=(10, 6))
sns.boxplot(x='customer_type', y='adr', data=df)
plt.xlabel('Customer Type')
plt.ylabel('Room Price (ADR)')
plt.title('Room Prices by Customer Type')
plt.savefig('room_prices_boxplot.png')  # Save the plot as an image
plt.show()

# Step 6: Make interactive Plotly dashboard with 3 graphs
fig1 = px.bar(monthly_income, title='Monthly Revenue', labels={'index': 'Month', 'value': 'Total Revenue'})
fig2 = px.pie(hotel_income, values='adr', names=hotel_income.index, title='City vs Resort Hotel Income')
fig3 = px.box(df, x='customer_type', y='adr', title='Room Prices by Customer Type')

# Create the dashboard layout
fig_dashboard = go.Figure()
fig_dashboard.add_trace(fig1.data[0])
fig_dashboard.add_trace(fig2.data[0])
fig_dashboard.add_trace(fig3.data[0])

fig_dashboard.update_layout(
    title='Hotel Revenue Analysis Dashboard',
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            buttons=list([
                dict(label="Monthly Revenue",
                     method="update",
                     args=[{"visible": [True, False, False]}]),
                dict(label="Hotel Income Comparison",
                     method="update",
                     args=[{"visible": [False, True, False]}]),
                dict(label="Room Prices by Customer Type",
                     method="update",
                     args=[{"visible": [False, False, True]}]),
            ]),
        )
    ]
)

fig_dashboard.show()

# Save the dashboard as an HTML file
fig_dashboard.write_html('hotel_revenue_dashboard.html')