import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Données simulées sur la performance fournisseurs
data = {
    'fournisseur': ['SUP-A', 'SUP-B', 'SUP-C', 'SUP-D', 'SUP-E', 'SUP-F', 'SUP-G'],
    'nb_commandes': [120, 75, 90, 130, 110, 80, 100],
    'delai_moyen': [3.2, 6.5, 4.1, 2.8, 3.9, 6.8, 4.5],
    'taux_conformite': [0.98, 0.81, 0.88, 0.97, 0.90, 0.76, 0.85],
    'taux_service': [0.97, 0.78, 0.89, 0.95, 0.91, 0.72, 0.86],
    'taux_retard': [0.05, 0.22, 0.14, 0.03, 0.08, 0.25, 0.16],
    'cout_non_conformite': [1200, 3900, 2300, 900, 1800, 4500, 2700]
}
df = pd.DataFrame(data)

# Standardisation
features = ['delai_moyen', 'taux_conformite', 'taux_service', 'taux_retard', 'cout_non_conformite']
X_scaled = StandardScaler().fit_transform(df[features])

# Réduction de dimension (PCA)
X_pca = PCA(n_components=2).fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

# Clustering KMeans
df['cluster'] = KMeans(n_clusters=3, random_state=42).fit_predict(X_scaled)

# Score de risque pondéré
df['score_risque'] = (
    0.25 * df['delai_moyen'] +
    0.3 * (1 - df['taux_service']) +
    0.2 * (1 - df['taux_conformite']) +
    0.15 * df['taux_retard'] +
    0.1 * df['cout_non_conformite'] / 1000
)

# Visualisation des clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='cluster', palette='Set2', s=100)
for i, row in df.iterrows():
    plt.text(row['PCA1'] + 0.05, row['PCA2'], row['fournisseur'], fontsize=9)
plt.title("Clustering des fournisseurs")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.grid(True)
plt.tight_layout()
plt.show()

# Résultats finaux
df_final = df[['fournisseur', 'score_risque', 'cluster']].sort_values(by='score_risque', ascending=False)
print("Classement des fournisseurs par score de risque :")
print(df_final.reset_index(drop=True))
