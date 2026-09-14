# kode for øving 4
import pandas as pd
import matplotlib.pyplot as plt

# Leser inn csv fil til dataframe
load = pd.read_csv("oving4/load_data.csv", decimal = ",") 

# Gjør om til datetimeindex
load["Time(Local)"] = pd.to_datetime(
    load["Time(Local)"], 
    utc = True, 
    format = "%d.%m.%Y %H:%M:%S %z")

load = load.set_index("Time(Local)")

# print(load.head())

# print(load.index[0])

# Skrive ut verdier fra spesifikt klokkeslett
# print(load.loc["2026-01-01 03:00"])

# Plotter lastprofil fra helt døgn
lastprofil = load.loc["2026-01-15"]
lastprofil.plot()
plt.grid()
plt.xlabel("Tidspunkt")
plt.ylabel("Produksjon og forbruk")
# plt.savefig("oving4/lastprofil_plot")

# Lager netto kolonne
load["Netto"] = load["Production"] - load["Consumption"]

# Finner maks, min og gjennomsnittlig produksjon
max_prod = max(load["Production"])
min_prod = min(load["Production"])
mean_prod = load["Production"].mean()

print("Maks produksjon er: ",max_prod)
print("Minimum produksjon er: ",min_prod)
print("Gjennomsnittlig produksjon er: ", round(mean_prod, 2))

# Finner maks og min netto produksjon
max_netto = max(load["Netto"])
min_netto = min(load["Netto"])
max_netto_tid = load["Netto"].idxmax()
min_netto_tid = load["Netto"].idxmin()

print("Maks nettoproduksjon er: ", round(max_netto, 2), " ved tidspunkt ", max_netto_tid)
print("Minimum nettoproduskjon er: ", round(min_netto, 2), " ved tidspunkt", min_netto_tid)
