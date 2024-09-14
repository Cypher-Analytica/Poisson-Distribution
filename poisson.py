import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Streamlit app title
st.title("Poisson Distribution PMF")

# User input for lambda (mean of the distribution)
lambda_value = st.slider("Select the value of λ (rate parameter)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)

# User input for range of x values (number of events)
max_x = st.slider("Select the maximum number of events", min_value=10, max_value=50, value=20, step=1)

# Generate x values (0 to max_x)
x = np.arange(0, max_x+1)

# Calculate Poisson PMF for each x value
pmf = poisson.pmf(x, mu=lambda_value)

# Plot the Poisson PMF
fig, ax = plt.subplots()
ax.bar(x, pmf, color='skyblue')
ax.set_title(f'Poisson Distribution PMF (λ = {lambda_value})')
ax.set_xlabel('Number of Events (x)')
ax.set_ylabel('PMF')
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Show the values of PMF
st.write("PMF values:")
st.write(dict(zip(x, pmf)))
