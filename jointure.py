import pandas as pd

# Charger les deux fichiers CSV avec un encodage différent
df_2017 = pd.read_csv('cleanfinal_pres2017.csv', encoding='ISO-8859-1')
df_2022 = pd.read_csv('cleanfinal_pres2022.csv', encoding='ISO-8859-1')

# Normaliser les valeurs de la colonne 'codegeo' pour avoir deux caractères
df_2017['codegeo'] = df_2017['codegeo'].apply(lambda x: x.zfill(2))
df_2022['codegeo'] = df_2022['codegeo'].apply(lambda x: x.zfill(2))

# Effectuer la jointure sur la colonne 'codegeo'
df_merged = pd.merge(df_2017, df_2022, on='codegeo', suffixes=('_2017', '_2022'))

# Écrire le résultat dans un nouveau fichier CSV
df_merged.to_csv('jointure.csv', index=False, encoding='utf-8')

print("La jointure a été effectuée avec succès et enregistrée dans 'jointure.csv'.")
