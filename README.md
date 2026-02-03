---

# Chicago Taxi Trips Dashboard

An interactive data visualization dashboard built using **Streamlit** to explore taxi trip patterns in **Chicago**.
The dashboard focuses on trip duration, distance–fare relationships, payment methods, and spatial pickup hotspots.

**Deployed on Hugging Face Spaces**
**Built with Python, Altair, Folium, and Streamlit**

---

## Project Structure

```
chicago-taxi-dashboard/
│
├── app.py              # Streamlit dashboard application
├── dashboard.csv       # Preprocessed dataset
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
```

---

## Project Overview

This project analyzes Chicago taxi trip data to uncover:

* Typical trip durations
* How fare relates to distance and time
* Differences across payment types
* High-density taxi pickup locations across the city

The goal is to present **clear, interpretable insights** through interactive visualizations while maintaining **data integrity**.

---

## Dashboard Features

### 1. Trip Duration Distribution

* Histogram showing the spread of taxi trip durations (in minutes)
* Highlights that most trips are short, intra-city rides

### 2. Trip Miles vs Fare

* Scatter plot visualizing how fares increase with distance
* Helps identify outliers and pricing dispersion

### 3. Trip Duration vs Fare

* Examines the relationship between trip length (time) and fare
* Reveals how traffic and route variability affect pricing

### 4. Pickup Hotspots in Chicago

* Heatmap showing areas with high taxi pickup density
* Uses an orange–red color scale for clear hotspot identification
* Spatially constrained to the Chicago city boundary

### 5. Interactive Filters

* **Payment Type filter** allows users to explore patterns by payment method
* All visualizations update dynamically based on selected filters

---

## Tech Stack

* **Python**
* **Streamlit** – dashboard framework
* **Altair** – interactive charts
* **Folium** – geospatial visualization
* **Pandas / NumPy** – data processing
* **Hugging Face Spaces** – deployment

---

## Data Source

Chicago Taxi Trips dataset from the **City of Chicago Open Data Portal**:

🔗 [https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew)

---

## Deployment

The dashboard is deployed on **Hugging Face Spaces** using GitHub integration

---

## Author

**Sravya Adapa**
Master’s student in Information Management
Interests: Data Analytics, Visualization, Applied Data Science

---
