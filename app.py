import streamlit as st
import numpy as np
from global_model import run_simulation
import matplotlib.pyplot as plt

st.set_page_config(page_title="Argon Plasma Global Model", layout="wide")
st.title("Argon Plasma Global Model Simulator")

st.sidebar.header("Simulation Parameters")
P_mTorr = st.sidebar.slider("Gas Pressure (mTorr)", 10, 1000, 100)
Pabs = st.sidebar.slider("Absorbed Power (W)", 0, 500, 300)
Te0 = st.sidebar.number_input("Initial Electron Temperature (eV)", 0.1, 10.0, 3.0)
ne0 = st.sidebar.number_input("Initial Electron Density (m⁻³)", 1e14, 1e17, 5.7e15, format="%e")
tmax = st.sidebar.number_input("Simulation Time (s)", 1e-6, 1e-2, 5e-3, format="%e")

st.write("### Simulation Running...")
t, result, csv_buffer = run_simulation(P_mTorr, Pabs, Te0, ne0, tmax)

fig, ax = plt.subplots()
ax.plot(t, result[:,2], label='Electron Density [m⁻³]')
ax.set_ylabel("n_e")
ax2 = ax.twinx()
ax2.plot(t, result[:,3], label='Electron Temperature [eV]', color='orange')
ax2.set_ylabel("T_e")
ax.set_xlabel("Time [s]")
fig.legend(loc='upper right')
st.pyplot(fig)

st.download_button(
    label="📥 Download Results as CSV",
    data=csv_buffer,
    file_name="simulation_results.csv",
    mime="text/csv"
)