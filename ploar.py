# Import the Polars library
import polars as pl

# Create a Polars DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pl.DataFrame(data)

# Select and filter data
filtered_df = df.select(['Name', 'Age']).filter(df['Age'] > 30)

# Perform aggregation
agg_df = df.groupby('City').agg(pl.sum('Age').alias('Total_Age'))

# Display the data
print("Original DataFrame:")
print(df)
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)
print("\nAggregated DataFrame:")
print(agg_df)