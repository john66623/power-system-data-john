# Kode for øving 6

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.linspace(0, 23, 500) # Lager tidsakse med 24 timer

# Setter verdier for innstråling
maks_straling = 800
bredde_straling = 3
tid_straling = 13

# Modellerer solstråling
modell_straling = maks_straling * np.exp(-(((t - tid_straling)**2) / (2 * bredde_straling**2)))

# Plotter
plt.plot(t, modell_straling, label = "Stråling i W/m^2")
plt.xlabel("Tid i timer")
plt.ylabel("Stråling")
plt.title("Modell for solstråling over et døgn")
plt.grid(True)
plt.show()
