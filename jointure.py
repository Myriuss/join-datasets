import pandas as pd

# Charger les fichiers CSV dans des DataFrames
chomage_df = pd.read_csv("chomageNet.csv", sep=";", encoding='ISO-8859-1')
pres2017_df = pd.read_csv("cleanfinal_pres2017.csv", sep=";", encoding='ISO-8859-1')
pres2022_df = pd.read_csv("cleanfinal_pres2022.csv", sep=";", encoding='ISO-8859-1')
population_df = pd.read_csv("CleanPopulation1.csv", sep=";", encoding='ISO-8859-1')

# Effectuer la jointure entre les DataFrames
result = chomage_df.merge(pres2017_df, on=["codegeo", "Libelle_departement"], how="inner") \
                   .merge(pres2022_df, on=["codegeo", "Libelle_departement"], how="inner") \
                   .merge(population_df, on=["codegeo", "Libelle_departement"], how="inner")

# Afficher un aperçu du résultat
print(result.head())


# Enregistrer le résultat dans un nouveau fichier CSV
result.to_csv("resultat_jointure.csv", index=False)
