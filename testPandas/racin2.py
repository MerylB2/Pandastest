import pandas as pd
import numpy as np

# Supposons que votre DataFrame ressemble à ceci
data = {'country': ['A', 'B', 'C'], 'population': [100, 400, 900]}
countries = pd.DataFrame(data)


# Appliquer la fonction racine carrée à la colonne 'population'
countries["population_sqrt"] = countries["population"].apply(np.sqrt)

# Afficher le DataFrame
print(countries)
