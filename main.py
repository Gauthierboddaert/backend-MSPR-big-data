import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = ''
fileName = 'Data_2022.xlsx'

def readfile(path):
    return pd.read_excel(path)

def get_data_from_file(index):
    global fileName
    global data

    path = './data/'+fileName
    data = readfile(path)
        
    
    return data[index]


def createCloudOfPoint():
    global data
    
    communes = getDataInFile('Nom commune')
    politicien_plus_vote = getDataInFile('Canditats')
    pourcentages = getDataInFile('Votes')  # Assurez-vous de définir ou récupérer les données de votes

   # Création du graphique à barres
    plt.figure(figsize=(10, 6))
    plt.bar(communes, pourcentages, color='blue')

    # Ajout des labels et du titre
    plt.xlabel('Communes')
    plt.ylabel('Pourcentage de Votes')
    plt.title('Pourcentage du politicien le plus voté dans chaque commune')

    # Rotation des labels des communes pour une meilleure lisibilité
    plt.xticks(rotation=45, ha='right')

     # Afficher le nuage de points
    plt.tight_layout()
    plt.show()

    # Enregistrer le graphique avant de l'afficher
    plt.savefig('./graph/pointOfCloud_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.png')


def getDataInFile(index):
    communes = []

    for index, valeur in enumerate(get_data_from_file(index)):
        communes.append(valeur)

    return communes



def creategraph():
    fig, ax = plt.subplots(figsize=(20, 10))
    candidats = ['arthaud', 'roussel', 'macron', 'lassalle', 'le pen', 'zemmour', 'melenchon', 'hidalgo', 'jadot', 'pecresse', 'poutou','nda']

    data = [
        get_data_from_file('pourcentage_arthaud').sum(),
        get_data_from_file('pourcentage_roussel').sum(),
        get_data_from_file('pourcentage_macron').sum(),
        get_data_from_file('pourcentage_lassalle').sum(),
        get_data_from_file('pourcentage_le_pen').sum(),
        get_data_from_file('pourcentage_zemmour').sum(),
        get_data_from_file('pourcentage_melenchon').sum(),
        get_data_from_file('pourcentage_hidalgo').sum(),
        get_data_from_file('pourcentage_jadot').sum(),
        get_data_from_file('pourcentage_pecresse').sum(),
        get_data_from_file('pourcentage_poutou').sum(),
        get_data_from_file('pourcentage_nda').sum()
    ]

    bar_labels = ['arthaud', 'roussel', 'macron', 'lassalle', 'le pen', 'zemmour', 'melenchon', 'hidalgo', 'jadot', 'pecresse', 'poutou','nda']
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange','tab:brown','tab:purple','tab:cyan','tab:grey','tab:pink','tab:olive','tab:red','tab:gray']

    ax.bar(candidats, data, label=bar_labels, color=bar_colors)

    ax.set_ylabel('nombre de voix')
    ax.set_title('Résultats des élections')
    
    plt.savefig('./graph/graph_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.png')



if __name__ == "__main__":
    createCloudOfPoint()
    



