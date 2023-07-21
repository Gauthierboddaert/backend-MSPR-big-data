import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def readfile(path):
    return pd.read_excel(path)

def get_data_from_file(index):
    path = './data/data.xlsx'
    data = readfile(path)
    
    return data[index]

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
    creategraph()




