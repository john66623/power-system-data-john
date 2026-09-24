# Kode for øving 6

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leser inn soldata, gjør om til datetime index
soldata = pd.read_csv("oving6/soldata_2023.csv", skiprows=8, nrows=8760)

soldata["time"] = pd.to_datetime(
    soldata["time"], 
    format = "%Y%m%d:%H%M").dt.round("h")

soldata = soldata.set_index("time")

print(soldata.head())

print(soldata["G(i)"].idxmax())

t = np.linspace(0, 23, 500) # Lager tidsakse med 24 timer
t_lowres = np.linspace(0, 23, 24)

# Setter verdier for innstråling
maks_straling = soldata.loc["2023-05-23", "G(i)"].max()
bredde_straling = 3
tid_straling = 12

print(maks_straling)

# Modellerer solstråling
modell_straling = maks_straling * np.exp(-(((t - tid_straling)**2) / (2 * bredde_straling**2)))

# Plotter modellen
plt.plot(t, modell_straling, label = "Stråling i W/m^2")
plt.xlabel("Tid i timer")
plt.ylabel("Stråling")
plt.title("Modell for solstråling over et døgn")
plt.grid(True)
plt.legend()

# Plotter PVgis data alene
plt.figure()
plt.plot(soldata.loc["2023-05-23", "G(i)"], label = "Solstråling i W/m^2")
plt.grid(True)
plt.xlabel("Tid i timer")
plt.ylabel("Stråling")
plt.title("Solstråling for 23. mai 2023 for hytta")
plt.legend()

# Plotter kurvene sammen
plt.figure()
plt.plot(t_lowres, soldata.loc["2023-05-23", "G(i)"], label = "Solstråling PVgis")
plt.plot(t, modell_straling, label = "Solstråling modell")
plt.grid(True)
plt.xlabel("Tid i timer")
plt.ylabel("Stråling")
plt.title("Solstråling og modell plottet sammen")
plt.legend()
plt.show()