import numpy as np

# Defino variables y constantes
N = 100000
means = [3, 4, 5]
percent = [0, 0.4, 0.72, 1]
perc_caja = [0, 0, 0]
count = 0

for i in range(N):
    x = np.random.uniform()
    r = -1
    for i in range(len(means)):
        if percent[i] <= x <= percent[i+1]:
            r = np.random.exponential(means[i])
            if r < 4:
                count += 1
            else:
                perc_caja[i] += 1
            break

# Imprimo resultados
print(f"a) Menos de 4 min: {count/N}")
print("b) Probabilidad de cada caja si tardo más de 4")
N_perc_caja = sum(perc_caja)
for i in range(len(perc_caja)):
    percentaje = int(perc_caja[i]/N_perc_caja*100)
    print(f"    Caja {i+1}: {percentaje}%")


'''
En numpy:
np.random.exponential(b)
b es 1/lambda (la media)
o sea, es una variable exponencial de parametro 1/b
'''