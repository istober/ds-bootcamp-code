import pandas as pd

# Requerimiento 1

datos = {"Jugador": ["Lionel Messi", "Cristiano Ronaldo", "Kevin De Bruyne", "Kylian Mbappé", "Luka Modric" ],
         "Posición": ["Delantero", "Delantero", "Mediocampista", "Delantero","Mediocampista"],
         "Edad": [35, 38, 31, 24, 37],
         "Goles": [20, 18, 8, 25, 3],
         "Asistencias": [10, 5, 15, 12, 8]
         }

df = pd.DataFrame(datos)

# Requerimiento 2

df['Jugador']

# Requerimiento 3

df[df['Goles'] > 10]
df2 = df[df['Goles'] > 10]
df2[['Jugador', 'Goles']]

# Requerimiento 4

df['Puntos'] = 4*df['Goles'] + 2*df['Asistencias']

# Requerimiento 5

df['Goles'].mean()

# Requerimiento 6

print(df['Asistencias'].min())
print(df['Asistencias'].max())

# Requerimiento 7

df.groupby('Posición').size()

# Requerimiento 8

df.sort_values(by = 'Goles', ascending = False)

# Requerimiento 9

df.describe()

# Requerimiento 10

df['Posición'].value_counts()