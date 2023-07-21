import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

path_file_excel = './data/data.xlsx'

data_frame = pd.read_excel(path_file_excel)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Données à tracer
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Créer le graphe
plt.plot(x, y, label='Ligne de données')

# Ajouter des étiquettes aux axes
plt.xlabel('Axe des abscisses')
plt.ylabel('Axe des ordonnées')

# Ajouter un titre
plt.title('Mon premier graphe avec matplotlib')

# Afficher le graphe
plt.show()
 
plt.savefig('./graph/graph'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.png')
