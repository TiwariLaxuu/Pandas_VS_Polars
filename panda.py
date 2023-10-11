# Import the Pandas library
import pandas as pd

# Create a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

# Select and filter data
filtered_df = df[['Name', 'Age']][df['Age'] > 30]

# Perform aggregation
agg_df = df.groupby('City')['Age'].sum().reset_index()
agg_df.rename(columns={'Age': 'Total_Age'}, inplace=True)

# Display the data
print("Original DataFrame:")
print(df)
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)
print("\nAggregated DataFrame:")
print(agg_df)
