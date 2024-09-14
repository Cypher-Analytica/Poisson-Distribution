import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Title of the app
st.title("Poisson Distribution Visualizer")

# Input for the mean (lambda)
lambda_ = st.slider("Select the mean (λ) of the Poisson distribution", 1, 20, 5)

# Generate Poisson distribution data
x = np.arange(0, 20)
pmf = poisson.pmf(x, lambda_)

# Plot the distribution
fig, ax = plt.subplots()
ax.bar(x, pmf, width=0.6, color='skyblue', edgecolor='black')
ax.set_xlabel('Number of events')
ax.set_ylabel('Probability')
ax.set_title(f'Poisson Distribution (λ = {lambda_})')

# Display the plot in the Streamlit app
st.pyplot(fig)
streamlit run app.py
