import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Load your dataset (replace this with your actual data loading code)
@st.cache_data
def load_data():
    # Replace this with your actual data fetching/processing function
    df = pd.read_csv('./data/benin-malanville.csv')
    return df

df = load_data()

# Dashboard Title
st.title("Solar Radiation Dashboard")

# Display DataFrame
st.subheader("Dataset Overview")
st.write(df.head())

# Interactive Widgets (e.g., sliders, buttons)
st.sidebar.header("Adjustable Filters")

# Slider to select a range of values for 'GHI' (Global Horizontal Irradiance)
ghi_range = st.sidebar.slider("Select GHI Range", float(df['GHI'].min()), float(df['GHI'].max()), (float(df['GHI'].min()), float(df['GHI'].max())))

# Filter the data based on the GHI range
filtered_df = df[(df['GHI'] >= ghi_range[0]) & (df['GHI'] <= ghi_range[1])]

# Display the filtered dataset
st.write(f"Filtered Data (GHI range: {ghi_range[0]} to {ghi_range[1]})")
st.write(filtered_df)

# Visualization: Plotting the data
st.subheader("Global Horizontal Irradiance (GHI) Over Time")

# Create a line plot
fig, ax = plt.subplots()
ax.plot(filtered_df['Timestamp'], filtered_df['GHI'], label="GHI", color='orange')
ax.set_xlabel("Timestamp")
ax.set_ylabel("GHI (W/m²)")
ax.set_title("GHI Over Time")
ax.legend()

# Display plot in Streamlit
st.pyplot(fig)

# Additional visualizations like bar plots, histograms, etc.
st.subheader("Correlation between GHI and Temperature (Tamb)")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x='GHI', y='Tamb', ax=ax)
ax.set_title("GHI vs Tamb (Temperature)")
st.pyplot(fig)

# Optional: More visualizations and data insights

