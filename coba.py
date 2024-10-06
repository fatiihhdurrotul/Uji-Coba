import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Buat data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Buat plot
plt.plot(x, y)

# Tampilkan plot dalam Streamlit
st.pyplot(plt)