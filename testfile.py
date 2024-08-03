

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (exemple)
df = pd.read_csv('diabetes.csv')

# Calculer la matrice de corrélation
correlation_matrix = df.corr()

# Afficher la matrice de corrélation
print(correlation_matrix)

# Visualiser la matrice de corrélation
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap de la Matrice de Corrélation')
plt.show()

#df.hist(figsize=(10, 10))
df.hist(bins=50, figsize=(20, 15))
plt.show()
