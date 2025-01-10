x = 100 # biljettpris
y = 200 # pengar på fickan

print("Det blir ", (y-x), " kronor över.")
z = 200 - 100 / 2
print("hälften är: ", z)

# Koden ville först addera (y-x) till strängen, detta funkade ej då (y-x) var en float.
# En sträng kan bara addera en sträng, inte float, därför byter vi + mot komma i koden.