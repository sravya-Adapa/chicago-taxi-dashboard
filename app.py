import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium .plugins import HeatMap
from streamlit_folium import st_folium


st.set_page_config(layout="wide")
st.title("Chicago Taxi Trips Analysis")

df = pd.read_csv("dashboard.csv")

st.sidebar.header("Payment Filter")
payment_options = sorted(df["payment_type"].unique())
selected_payment_type = st.sidebar.multiselect(
    "Select Payment Type",
    options = payment_options,
    default=payment_options)
filtered_df = df[df["payment_type"].isin(selected_payment_type)]

filtered_df['trip_minutes'] = filtered_df['trip_seconds']/60


# Plot 1
st.subheader("Trip Duration Distribution")
histogram = (
    alt.Chart(filtered_df)
    .mark_bar()
    .encode(
        x=alt.X("trip_minutes:Q",bin= alt.Bin(maxbins = 40) ,title="Trip Duration (Minutes)"),
        y=alt.Y("count()",title="Number of Trips")
    )
    .properties(height=300)
    .interactive()
)
st.altair_chart(histogram, use_container_width=True)
st.caption(
    "This histogram shows the distribution of taxi trip durations in minutes. "
    "Most trips are short, indicating high demand for quick, intra-city travel."
)


# Plot 2
st.subheader("Trip Miles vs Fare")
scatter = (
    alt.Chart(filtered_df)
    .mark_circle(size=60, opacity=0.4)
    .encode(
        x=alt.X("trip_miles:Q", title="Trip Miles"),
        y=alt.Y("fare:Q", title="Fare in USD"),
        tooltip=["trip_miles", "fare"]
    )
    .properties(height=500)
    .interactive()
)
st.altair_chart(scatter, use_container_width=True)
st.caption(
    "This scatter plot illustrates the relationship between trip distance and fare. "
    "Fares generally increase with distance, while outliers may indicate surcharges or longer routes."
)


# Plot 3
st.subheader("Trip Duration Vs Fare")
scatter = (
    alt.Chart(filtered_df)
    .mark_circle(size=60, opacity=0.4)
    .encode(
        x = alt.X("trip_minutes:Q", title="Trip Duration (Minutes)"),
        y = alt.Y("fare:Q", title="Fare in USD"),
        tooltip=["trip_miles", "fare"]
    )
    .properties(height=500)
    .interactive()
)
st.altair_chart(scatter, use_container_width=True)
st.caption(
    "This visualization highlights how trip duration impacts fare. "
    "Longer travel times tend to result in higher fares, though traffic and route variations create dispersion."
)

#plot 4
st.subheader("Pickup Hotspots in Chicago")
pickup_df = filtered_df[["pickup_centroid_latitude", "pickup_centroid_longitude"]].dropna()

pickup_agg = (pickup_df.value_counts().reset_index(name="count"))

chicago_center = [41.8781, -87.6298]
chicago_bounds = [
    [41.6445, -87.9401],  # Southwest Chicago
    [42.0230, -87.5237]   # Northeast Chicago
]

m = folium.Map(
    location=chicago_center,
    zoom_start=11,
    tiles="cartodbpositron"
)

m.fit_bounds(chicago_bounds)

heat_data = pickup_agg[
    ["pickup_centroid_latitude", "pickup_centroid_longitude", "count"]
].values.tolist()

HeatMap(
    heat_data,
    radius=10,
    blur=18,
    min_opacity=0.8,
    max_zoom=13,
    gradient={
        0.2: "yellow",
        0.4: "orange",
        0.6: "red",
        1.0: "darkred"
    }
).add_to(m)
st_folium(m, width=700, height=500)
st.caption("Heatmap shows the spatial density of taxi pickup locations. Brighter areas indicate higher trip volume. ")



