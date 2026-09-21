# Kode for øving 5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Implementerer Gauss-modell

t = np.linspace(0, 23, 500) # Lager numpy liste med 24 timer

grunnlast = 1

morgen_amp = 1 # Amplitude for morgen
morgen_tid = 7 # Tidspunkt for topp
morgen_bredde = 1 # Bredde

kveld_amp = 1
kveld_tid = 18
kveld_bredde = 1

natt_amp = 1
natt_tid = 23
natt_bredde = 1

morgen_peak = morgen_amp * np.exp(-(((t - morgen_tid)**2) / (2 * morgen_bredde**2)))
kveld_peak = kveld_amp * np.exp(-(((t - kveld_tid)**2) / (2 * kveld_bredde**2)))
natt_peak = natt_amp * np.exp(-(((t - natt_tid)**2) / (2 * natt_bredde**2)))
modell = morgen_peak + kveld_peak + natt_peak

plt.plot(t, modell, linestyle = "--")
plt.plot(t, morgen_peak, linestyle = "--", linewidth = 0.7)
plt.plot(t, kveld_peak, linestyle = "--", linewidth = 0.7)
plt.plot(t, natt_peak, linestyle = "--", linewidth = 0.7)
plt.legend()
plt.grid(True)  
plt.show()
