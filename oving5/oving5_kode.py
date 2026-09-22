# Kode for øving 5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leser inn csv fil, henter døgnprofil
lastdata = pd.read_csv("oving5/lastdata2019.csv")

lastdata["Time(Local)"] = pd.to_datetime(
    lastdata["Time(Local)"], 
    utc = True, 
    format = "%d.%m.%Y %H:%M:%S %z")

lastdata = lastdata.set_index("Time(Local)")

dognprofil = lastdata.loc["2019-01-15"]

# Implementerer Gauss-modell
t = np.linspace(0, 23, 24) # Lager numpy array med 24 timer
t_highres = np.linspace(0, 23, 500) # Lager tilsvarende array med høyere oppløsning 

# Definerer variabler til modellen
grunnlast = dognprofil["Consumption"].min()

morgenprofil = dognprofil.loc[
    "2019-01-15 07:00" : "2019-01-15 10:00", 
    "Consumption"]
morgen_amp = morgenprofil.max() - grunnlast # Amplitude for morgen
morgen_tid = morgenprofil.idxmax().hour # Tidspunkt for morgentopp
morgen_bredde = 2 # Bredde for morgen

kveldsprofil = dognprofil.loc[
    "2019-01-15 14:00" : "2019-01-15 20:00", 
    "Consumption"]
kveld_amp = kveldsprofil.max() - grunnlast
kveld_tid = kveldsprofil.idxmax().hour
kveld_bredde = 4

natt_amp = kveld_amp
natt_tid = kveld_tid - 24
natt_bredde = kveld_bredde

# Definerer modellen med ligninger
morgen_peak = morgen_amp * np.exp(-(((t_highres - morgen_tid)**2) / (2 * morgen_bredde**2)))
kveld_peak = kveld_amp * np.exp(-(((t_highres - kveld_tid)**2) / (2 * kveld_bredde**2)))
natt_peak = natt_amp * np.exp(-(((t_highres - natt_tid)**2) / (2 * natt_bredde**2)))
modell = grunnlast + morgen_peak + kveld_peak + natt_peak

# Skriver ut parameterverdier
print("Amplitude for morgenen er ", morgen_peak, "Ved time ", morgen_tid, "og bredde ", morgen_bredde)
print("Amplitude for kvelden er ", kveld_peak, "Ved time ", kveld_tid, "og bredde ", kveld_bredde)
print("Amplitude for natten er ", natt_peak, "Ved time ", natt_tid, "og bredde ", natt_bredde)


# Plotter døgnprofilen med observerte data
plt.plot(t, dognprofil["Consumption"], label = "Døgnprofil")
plt.grid(True)
plt.legend()
plt.xlabel("Time i døgnet")
plt.ylabel("Forbruk i MW")
plt.title("Observerte data for forbruk 15. januar 2019")

# Plotter modellen
plt.figure()
plt.plot(t_highres, modell, label = "Modellen")
plt.plot(t_highres, morgen_peak + grunnlast, linestyle = "--", linewidth = 0.7, label = f"Morgen, A = {morgen_amp:.1f}, tid = {morgen_tid:.1f}, bredde = {morgen_bredde:.1f}")
plt.plot(t_highres, kveld_peak + grunnlast, linestyle = "--", linewidth = 0.7, label = f"Kveld, A = {kveld_amp:.1f}, tid = {kveld_tid:.1f}, bredde = {kveld_bredde:.1f}")
plt.plot(t_highres, natt_peak + grunnlast, linestyle = "--", linewidth = 0.7, label = f"Natt, A = {natt_amp:.1f}, tid = {natt_tid:.1f}, bredde = {natt_bredde:.1f}")
plt.legend()
plt.ylim(dognprofil["Consumption"].min() - 1000, dognprofil["Consumption"].max() + 1000)
plt.xlabel("Time i døgnet")
plt.ylabel("Forbruk i MW")
plt.title("Modell for forbruk 15. januar 2019")
plt.grid(True)

# Plotter modellen sammen med døgnprofilen
plt.figure()
plt.plot(t, dognprofil["Consumption"], label = "Døgnprofil")
plt.plot(t_highres, modell, label = "Modellen")
plt.plot(t_highres, morgen_peak + grunnlast, linestyle = "--", linewidth = 0.7, label = f"Morgen, A = {morgen_amp:.1f}, tid = {morgen_tid:.1f}, bredde = {morgen_bredde:.1f}")
plt.plot(t_highres, kveld_peak + grunnlast, linestyle = "--", linewidth = 0.7, label = f"Kveld, A = {kveld_amp:.1f}, tid = {kveld_tid:.1f}, bredde = {kveld_bredde:.1f}")
plt.plot(t_highres, natt_peak + grunnlast, linestyle = "--", linewidth = 0.7, label = f"Natt, A = {natt_amp:.1f}, tid = {natt_tid:.1f}, bredde = {natt_bredde:.1f}")
plt.legend()
plt.ylim(dognprofil["Consumption"].min() - 1000, dognprofil["Consumption"].max() + 1000)
plt.xlabel("Time i døgnet")
plt.ylabel("Forbruk i MW")
plt.title("Modell og observerte data for forbruk 15. januar 2019")
plt.grid(True)
plt.show()
