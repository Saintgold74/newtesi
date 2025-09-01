import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dati correlazione downtime
data = {
    'AWS': [1.00, 0.12, 0.09],
    'Azure': [0.12, 1.00, 0.14],
    'GCP': [0.09, 0.14, 1.00]
}

df = pd.DataFrame(data, index=['AWS', 'Azure', 'GCP'])

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', center=0.5, 
            vmin=0, vmax=1, square=True, linewidths=1)
plt.title('Matrice di Correlazione Downtime Cloud Provider')
plt.tight_layout()
plt.savefig('cloud_correlation.pdf')