import pandas as pd

path_file_excel = './data/liste_communes.xlsx'

data_frame = pd.read_excel(path_file_excel)

print(data_frame['test'])

