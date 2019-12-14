import pandas as pd
import numpy as np

#	import GWAS
df_gwas = pd.read_csv("Rice_Association.csv", na_values=['-'])
df_gwas = df_gwas.drop(columns = ['QTL'])
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace(' ','')
df_gwas['Gene_Symbol'] = df_gwas['Gene_Symbol'].str.replace(' ','')
print(df_gwas)

#	check gwas head
head = np.array(df_gwas.columns)
print(head, '\n')


#	training dataset
df_gwas = df_gwas.dropna(axis = 'index', how = 'all',subset = ['Reported_Gene(S)','Gene_Symbol'])
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace('/',';')
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace('-',';')
df_gwas['Gene_Symbol'] = df_gwas['Gene_Symbol'].str.replace('/',';')
print(df_gwas)

export_csv = df_gwas.to_csv('gwas_training.csv', index = None, header = True)