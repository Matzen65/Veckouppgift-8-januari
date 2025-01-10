
# 3 använda variabler och datatyper
# uppgift 2a och 2b

pris = int(input("pris på jackan "))

# fråga om rabatt i procent och räkna ut vad jackan kostar
rabatt = int(input("ange rabatt i procent "))
nytt_pris = 0
nytt_pris = pris - (pris * rabatt/100)
print ("nytt rabatterat pris blir", nytt_pris)

