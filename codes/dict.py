import pandas as pd
import numpy as np


#	import locus
headers = ['Chr', '1','2', 'Chr_start', 'Chr_end', '3', '4', '5', 'RAP ID', 'Name', 'Note', 'TV', '6', '7', '8','9','10','11']
dtypes = 'str'
df_locus = pd.read_csv("locus.csv", header = None, names = headers, dtype = dtypes, engine = 'python')

#	simplify locus
df_locus = df_locus.drop(columns = ['1','2','3','4','5','6','7','8','9','10','11','TV', 'Note'])
df_locus['RAP ID'] = df_locus['RAP ID'].map(lambda x: x.lstrip('ID='))
df_locus['Name'] = df_locus['Name'].map(lambda x: x.lstrip('Name='))
print(df_locus)


'''
#	search for chr info
term = 'Os12g0641300'
locate = df_locus.loc[df_locus['ID'] == ('ID='+term), ['ID', 'Chr', 'Chr_start', 'Chr_end']]
print(locate)
'''

# 	import oryzadata
df_oryza = pd.read_csv("oryzadata.csv")
print(df_oryza, '\n')
head1 = np.array(df_oryza.columns)
print(head1)
print(df_oryza['RAP ID'])


#	join locus and oryzadata
df_genedata = pd.merge(df_oryza, df_locus, how='inner', on=['RAP ID'])
print(df_genedata)
df_genedata = df_genedata.drop(columns = ['Name'])

export_csv = df_genedata.to_csv('genedata.csv', index = None, header = True)