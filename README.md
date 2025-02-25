# Hotel Revenue Analysis

## Project Aim

The aim of this project is to analyze hotel revenue data and provide visual insights using Python libraries such as pandas, matplotlib, seaborn, and Plotly. The project focuses on understanding revenue patterns, comparing income between different types of hotels, and examining room prices by customer type.

## Project Overview

This project involves the following steps:
1. **Loading Data**: Importing the hotel bookings data using pandas.
2. **Data Cleaning**: Removing cancelled bookings and filling missing values.
3. **Visualizing Monthly Revenue**: Creating a bar chart to show monthly revenue.
4. **Comparing Hotel Income**: Using a pie chart to compare income between City and Resort hotels.
5. **Room Price Analysis**: Creating a boxplot to visualize room prices by customer type.
6. **Interactive Dashboard**: Building an interactive Plotly dashboard to combine the above visualizations.

## Steps to Run the Project

1. **Clone the Repository**: Clone this repository to your local machine.
    ```bash
    git clone https://github.com/desertCoder-bot/Hotel_revenue_analysis-using-python.git
    cd Hotel_revenue_analysis-using-python
    ```

2. **Install Dependencies**: Make sure you have the necessary libraries installed.
    ```bash
    pip install pandas matplotlib seaborn plotly
    ```

3. **Prepare Data**: Place the `hotel_bookings.csv` file in the same directory as the script.

4. **Run the Script**: Execute the script to generate visualizations and the dashboard.
    ```bash
    python hotel_revenue_analysis.py
    ```

## Visualizations

1. **Monthly Revenue**: Bar chart showing total revenue for each month.
2. **City vs Resort Hotel Income**: Pie chart comparing income from City and Resort hotels.
3. **Room Prices by Customer Type**: Boxplot showing room prices by different customer types.
4. **Interactive Dashboard**: A Plotly dashboard with all the above visualizations for interactive analysis.

## Example Data

You can download the example dataset from Kaggle: [Hotel Bookings Dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand)

## Dashboard

The interactive dashboard will be saved as `hotel_revenue_dashboard.html` in the same directory. Open this file in any web browser to explore the data interactively.

## Insights

- **Monthly Revenue**: Helps in identifying peak and off-peak seasons.
- **City vs Resort Hotel Income**: Provides a comparative analysis of revenue from different hotel types.
- **Room Prices by Customer Type**: Shows how room prices vary across different customer types, useful for pricing strategies.

## Project Structure

```plaintext
hotel-revenue-analysis/
├── hotel_bookings.csv      # Dataset file
├── hotel_revenue_analysis.py  # Main analysis script
├── monthly_revenue.png     # Bar chart of monthly revenue
├── hotel_income_comparison.png # Pie chart of hotel income comparison
├── room_prices_boxplot.png # Boxplot of room prices by customer type
├── hotel_revenue_dashboard.html # Interactive Plotly dashboard
├── README.md               # Project documentation
```

## Enjoy Analyzing! 😎

Enjoy analyzing your hotel revenue data and gaining valuable insights! If you have any questions or suggestions, feel free to open an issue or submit a pull request.
