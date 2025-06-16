import numpy as np

def k_iz(Te):
    return 5e-14 * np.exp(-15.76 / Te)  # m³/s