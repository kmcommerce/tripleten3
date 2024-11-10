import streamlit as st
import plotly.express as px
import pandas as pd
df = pd.read_csv('c:\\users\\kmcom\\tripleten3\\vehicles_us.csv')
st.write("Data Preview:")
st.write(df.head())
# Header
st.header('Streamlit with Plotly and Interactive Checkbox using Vehicle Data')
st.write("Missing Values in the Dataset:")
st.write(df_clean.isnull().sum())

if 'price' in df.columns and 'cylinders' in df.columns:
    # Plotly Express Scatter Plot (Price vs Cylinders)
    fig_scatter = px.scatter(df, x='price', y='cylinders', title="Price vs Cylinders")
    st.plotly_chart(fig_scatter)
else:
    st.write("Columns 'price' or 'cylinders' not found in dataset.")

if 'odometer' in df.columns:
    # Plotly Express Histogram for Odometer (Mileage)
    fig_hist = px.histogram(df, x='odometer', title="Distribution of Car Mileage (Odometer)")
    st.plotly_chart(fig_hist)
else:
    st.write("Column 'odometer' not found in dataset.")

# Checkbox to filter the data by price
filter_price = st.checkbox('Filter Vehicles by Price', value=False)

if filter_price:
    max_price = st.slider("Select Maximum Price", min_value=0, max_value=int(df['price'].max()), value=50000)
    filtered_df = df[df['price'] <= max_price]
    st.write(f"Showing vehicles with price <= ${max_price}")
    st.write(filtered_df)
       # Replot the scatter plot with the filtered data
    fig_scatter_filtered = px.scatter(filtered_df, x='price', y='cylinders', title=f"Price vs Cylinders (up to ${max_price})")
    st.plotly_chart(fig_scatter_filtered)
else:
    st.write("Displaying all vehicles.")