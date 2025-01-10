
pris = 100 # biljettpris
fickpengar = 200 # pengar på fickan
halva_pris = 0 #hälften av priset

print("Det blir ", (fickpengar - pris), " kronor över.")
halva_pris = (fickpengar - pris / 2)
print("hälften är: ", halva_pris)

# Koden ville först addera (y-x) till strängen, detta funkade ej då (y-x) var en float.
# En sträng kan bara addera en sträng, inte float, därför byter vi + mot komma i koden.