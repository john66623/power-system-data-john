import pandas as pd
import matplotlib.pyplot as plt

# Leser inn data med pandas
forbruk = pd.read_csv("load/forbruk_2025.csv")
dato_kolonne = forbruk.columns[0]

# Gjør om til datetime objekter
forbruk[dato_kolonne] = pd.to_datetime(forbruk[dato_kolonne], utc=True)

# Sjekker at data er lest inn korrekt, og at tidsstemplene tolkes som dato og klokkeslett
print(forbruk)

# Setter første kolonne som index for å lettere gruppere data
forbruk = forbruk.set_index(dato_kolonne)

# Beregner månedlig gjennomsnitt
maanedlig = forbruk.resample("ME").mean()

# Sjekker resultat
print(maanedlig)

# # Skriver månedlig gjennomsnitt til ny .csv fil
# maanedlig.to_csv("results/maanedlig_forbruk.csv")

# Plotter månedlig gjennomsnitt
maanedlig.plot()
plt.grid()
plt.xlabel("Periode")
plt.ylabel("Gjennomsnittlig forbruk i MW")

# Lagrer figuren
# plt.savefig("results/manedlig_last_2025.png")

# Finner høyeste, laveste og standardavvik på last
statistikk = forbruk.resample("ME").agg(["max", "min", "std"])

# Lagrer resultat
statistikk.to_csv("results/manedlig_last_statistikk_2025.csv")