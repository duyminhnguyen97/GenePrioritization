import pandas as pd
import numpy as np


'''
#	import snp
snp_data = pd.read_csv('Rice_Association.csv', dtype = 'str', engine = 'python')
snp_data['Chr'] = snp_data['Chr'].replace({'chr':''}, regex=True)
int_head = ['Chr', '#GaP_id', 'Chr_Pos']
snp_data[int_head] = snp_data[int_head].astype(int)

print(len(snp_data['Trait_ontology'].unique()))

g = snp_data.groupby('Trait_ontology')['Trait'].apply(lambda x: list(np.unique(x)))
for i in range(len(g)):
	print(len(g[i]))
print(g['plant morphology trait'])
'''


data = pd.read_csv('input.csv', engine = 'python')
print(data)
headers1 = ['biochemical_character', 'vegetative_organ', 'reproductive_organ','coloration' , 'seed', 'tolerance_resistance', 'QTL']
data.dropna(axis = 'index', subset = headers1, how = 'all')
print(data)