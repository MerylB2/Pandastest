# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Pour afficher les graphiques dans le notebook
#%matplotlib inline

# # Charger les données depuis un fichier CSV
df = pd.read_csv('diabetes.csv')

# Afficher les premières lignes du DataFrame
print(df.head())

# apercu des donnees

print(df.info())
print(df.describe())

# verification des valeurs manquantes

print(df.isnull().sum())

# Distribution des classes

print(df['Outcome'].value_counts())
sns.countplot(x='Outcome', data=df)
plt.show()

# distribution des caracteristiques

df.hist(figsize=(10, 10))
plt.show()

# Matrice de correlation

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# paires de Parcelles
sns.pairplot(df, hue='Outcome')
plt.show()

#***** Pretraitement des donnees ****#

#  gestion des valeurs manquantes 
df.replace(0, np.nan, inplace=True)
df.fillna(df.mean(), inplace=True)

# separation des carac et de la variable cible
X = df.drop('Outcome', axis=1)
y = df['Outcome']


# Normalisation des donnees
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#**** Modelisation
# Séparation des données en ensembles d'entraînement et de test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Entraînement d'un modèle de classification

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = LogisticRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Évaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
