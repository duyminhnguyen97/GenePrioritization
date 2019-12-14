import pandas as pd
import numpy as np

#	import oryzabase database
df_oryza = pd.read_csv("oryzabase.csv")
#print(df_oryza, '\n')
head = np.array(df_oryza.columns)
print(head)


#	drop all no RAP ID genes
df_oryza = df_oryza.dropna(axis = 'index',subset = ['RAP ID'])
df_oryza = df_oryza.reset_index(drop=True)
print(df_oryza, '\n')


#	resolve extra data
#df_oryza[['RAP ID', 'RAP ID2', 'RAP ID3']] = df_oryza['RAP ID'].str.split('/', expand = True)
spl_ID = df_oryza['RAP ID'].str.split('/', expand = True)
df_oryza['RAP ID'] = df_oryza['RAP ID'].str.split('/', expand = True)
spl_ID.columns = ['ID1','ID2','ID3']


#	split for 1
spl_ID = spl_ID.dropna(axis = 'index', subset = ['ID2', 'ID3'], how = 'all')
spl_ID_index = list(spl_ID.index)
#print(spl_ID)
#print(spl_ID_index)


#	extra1
extra1 = pd.DataFrame(data=None, columns=df_oryza.columns, index=spl_ID.index)
extra1 = extra1.reset_index(drop=True)
for i in range(0,169):
	extra1.loc[i] = df_oryza.iloc[spl_ID_index[i]]
extra1['RAP ID'] = spl_ID['ID2'].values
#print(extra1)
#export_csv = extra1.to_csv('extra.csv', index = None, header = True)


#	spl for 2
spl_ID2 = spl_ID.dropna(axis = 'index', subset = ['ID3'], how = 'all')
spl_ID_index2 = list(spl_ID2.index)
#print(spl_ID2)
#print(spl_ID_index2)


#	extra2
extra2 = pd.DataFrame(data=None, columns=df_oryza.columns, index=spl_ID2.index)
extra2 = extra2.reset_index(drop=True)
for i in range(0,11):
	extra2.loc[i] = df_oryza.iloc[spl_ID_index2[i]]
extra2['RAP ID'] = spl_ID2['ID3'].values
#print(extra2)
#export_csv = extra2.to_csv('extra.csv', index = None, header = True)


#	join to Oryza
df_oryza = df_oryza.append(extra1, ignore_index=True)
df_oryza = df_oryza.append(extra2, ignore_index=True)
print(df_oryza)


export_csv = df_oryza.to_csv('oryzadata.csv', index = None, header = True)