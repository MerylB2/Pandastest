import pandas as pd
import numpy as np

# Charger les données depuis un fichier CSV
df = pd.read_csv('diabetes.csv')

# Afficher les premières lignes pour vérifier
print("Avant l'application de la racine carrée:")
print(df.head())

# Appliquer la fonction racine carrée à la colonne 'population'
df['population_sqrt'] = np.sqrt(df['population'])

# Afficher les premières lignes pour vérifier
print("\nAprès l'application de la racine carrée:")
print(df[['population', 'population_sqrt']].head())
