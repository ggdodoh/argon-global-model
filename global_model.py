import numpy as np
from scipy.integrate import solve_ivp
from reaction_rates import k_iz
import pandas as pd
import io

def model(t, y, V, A, Pabs):
    n_Ar, n_Arp, n_e, Te = y
    kiz = k_iz(Te)
    R_iz = kiz * n_Ar * n_e

    m_Ar = 6.63e-26  # Ar 질량 (kg)
    kB = 1.381e-23
    v_th = np.sqrt(8 * kB * Te * 1.602e-19 / (np.pi * m_Ar))
    Gamma_loss = (1/4) * n_Arp * v_th * A / V

    dn_Ar = -R_iz
    dn_Arp = R_iz - Gamma_loss
    dn_e = R_iz - Gamma_loss
    dTe = (Pabs - R_iz * 15.76 * 1.602e-19 - Gamma_loss * Te * 1.602e-19) / (1.5 * n_e * kB)

    return [dn_Ar, dn_Arp, dn_e, dTe]

def run_simulation(P_mTorr, Pabs, Te0, ne0, tmax):
    T_gas = 300
    kB = 1.381e-23
    mTorr_to_Pa = 133.3 / 1000
    P_Pa = P_mTorr * mTorr_to_Pa
    n_Ar0 = P_Pa / (kB * T_gas)

    # 챔버 조건
    diameter = 0.3048  # 12 inch
    radius = diameter / 2
    height = 0.15  # 15 cm
    V = np.pi * radius**2 * height
    A = np.pi * diameter**2 / 4

    y0 = [n_Ar0, 0, ne0, Te0]
    sol = solve_ivp(model, [0, tmax], y0, args=(V, A, Pabs), method='RK45', max_step=1e-5)

    df = pd.DataFrame({
        "Time (s)": sol.t,
        "n_Ar (m^-3)": sol.y[0],
        "n_Ar+ (m^-3)": sol.y[1],
        "n_e (m^-3)": sol.y[2],
        "T_e (eV)": sol.y[3],
    })

    csv = df.to_csv(index=False)
    return sol.t, np.transpose(sol.y), csv