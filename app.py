import pandas as pd
from robo import download_Dae

df = pd.read_excel("IPVA 2024.xlsx", sheet_name='Planilha4')

for indice, linha in df.iterrows():
  placa = linha['PLACA']
  renavam = linha['RENAVAM']
  download_Dae(placa, renavam)