import pandas as pd
import numpy as np

#	import GWAS
df_gwas = pd.read_csv("Rice_Association.csv", na_values=['-'])
df_gwas = df_gwas.drop(columns = ['QTL'])
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].replace(' ',np.nan)
df_gwas['Gene_Symbol'] = df_gwas['Gene_Symbol'].replace(' ',np.nan)
print(df_gwas)


#	Input Data
df_input = df_gwas[df_gwas['Reported_Gene(S)'].isnull() & df_gwas['Gene_Symbol'].isnull()]
df_input = df_input.drop(columns = ['Reported_Gene(S)','Gene_Symbol'])
print(df_input)
export_csv = df_input.to_csv('SNP_Input.csv', index = None, header = True)


#	check gwas head
head = np.array(df_gwas.columns)
print(head, '\n')


#	training dataset
df_gwas = df_gwas.dropna(axis = 'index', how = 'all',subset = ['Reported_Gene(S)','Gene_Symbol'])
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace('/',';')
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace('-',';')
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace(',',';')
df_gwas['Reported_Gene(S)'] = df_gwas['Reported_Gene(S)'].str.replace(',',';')
df_gwas['Gene_Symbol'] = df_gwas['Gene_Symbol'].str.replace('/',';')
print(df_gwas['Reported_Gene(S)'].dtypes)


#	Test code
#	Reported Gene
df_gwas1 = df_gwas.dropna(axis = 'index', how = 'all',subset = ['Reported_Gene(S)'])

test1 = pd.concat([pd.Series(row['#GaP_id'], row['Reported_Gene(S)'].split(';'))
	for _, row in df_gwas1.iterrows()]).reset_index()
print(test1)

export_csv = test1.to_csv('Reported Gene.csv', index = None, header = True)


#	Gene Symbol
df_gwas2 = df_gwas.dropna(axis = 'index', how = 'all',subset = ['Gene_Symbol'])
df_gwas2 = df_gwas2[df_gwas2['Reported_Gene(S)'].isnull()]
test2 = pd.concat([pd.Series(row['#GaP_id'], row['Gene_Symbol'].split(';'))
	for _, row in df_gwas2.iterrows()]).reset_index()
print(test2)

export_csv = test2.to_csv('Gene Symbol.csv', index = None, header = True)


'''
#	split extra data
spl_ID = df_gwas['Reported_Gene(S)'].str.split(';', expand = False)
df_gwas = df_gwas['Reported_Gene(S)'].str.split(';', n=1, expand = True)
print(spl_ID)
'''

#export_csv = df_gwas.to_csv('gwas_training.csv', index = None, header = True)

