import pandas  as pd

#	data header
headers = pd.read_csv('head.txt', header = None, dtype = 'str', engine = 'python')
headers = list(headers[0])
#print(headers)


#	import genedata.csv
gene_data = pd.read_csv('genedata.csv', dtype = 'str', engine = 'python')
gene_data['Chr'] = gene_data['Chr'].replace({'chr':''}, regex=True)
gene_data['Chr'] = gene_data['Chr'].astype(int)
gene_data['Chr_start'] = gene_data['Chr_start'].astype(int)
gene_data['Chr_end'] = gene_data['Chr_end'].astype(int)
gene_data = gene_data.dropna(axis = 'index', subset = ['Trait Class'], how = 'all')
gene_data = gene_data.reset_index(drop = True)
#print(gene_data['Trait Class'])


#	create training dataset
training = pd.DataFrame(data = None, columns = headers)
training[headers] = training[headers].astype(int)
training['gene_name'] = training['gene_name'].astype(str)
training['gene_name'] = gene_data['RAP ID']
training['chr'] = gene_data['Chr']
training['chr_start'] = gene_data['Chr_start']
training['chr_end'] = gene_data['Chr_end']
training = training.reset_index(drop = True)
#print(training)


#	biochemical character
biochemical_character = gene_data[gene_data['Trait Class'].str.contains('Biochemical character', regex = False)]
#biochemical_character = biochemical_character.append(gene_data[gene_data['Trait Class'].str.contains('Coloration', regex = False)])
biochemical_character_index = biochemical_character.index
print(biochemical_character_index)
for i in range(len(biochemical_character_index)):
	training.at[biochemical_character_index[i],'biochemical_character'] = 1


#	vegetative_organ
vegetative_organ = gene_data[gene_data['Trait Class'].str.contains('Vegetative organ', regex = False)]
vegetative_organ_index = vegetative_organ.index
for i in range(len(vegetative_organ_index)):
	training.at[vegetative_organ_index[i],'vegetative_organ'] = 1


#	reproductive_organ
reproductive_organ = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ', regex = False)]
reproductive_organ_index = reproductive_organ.index
for i in range(len(reproductive_organ_index)):
	training.at[reproductive_organ_index[i],'reproductive_organ'] = 1


#	coloration
coloration = gene_data[gene_data['Trait Class'].str.contains('Coloration', regex = False)]
coloration = coloration.index
for i in range(len(coloration)):
	training.at[coloration[i],'coloration'] = 1


#	seed
seed = gene_data[gene_data['Trait Class'].str.contains('Seed', regex = False)]
seed_index = seed.index
for i in range(len(seed_index)):
	training.at[seed_index[i],'seed'] = 1


#	tolerance_resistance
tolerance_resistance = gene_data[gene_data['Trait Class'].str.contains('Tolerance and resistance', regex = False)]
tolerance_resistance_index = tolerance_resistance.index
for i in range(len(tolerance_resistance_index)):
	training.at[tolerance_resistance_index[i],'tolerance_resistance'] = 1


#	Character as QTL
QTL = gene_data[gene_data['Trait Class'].str.contains('Character as QTL', regex = False)]
QTL_index = QTL.index
for i in range(len(QTL_index)):
	training.at[QTL_index[i],'QTL'] = 1


#	eliminate Nan
headers1 = ['biochemical_character', 'vegetative_organ', 'reproductive_organ', 'seed', 'coloration', 'tolerance_resistance', 'QTL']
training = training.dropna(axis = 'index', subset = headers1, how = 'all')
training = training.fillna(0)
training[headers1] = training[headers1].astype(int)

#	sort training
training = training.sort_values(by = ['chr', 'chr_start'])
training = training.reset_index(drop = True)

training.insert(11, "midpoint",None,True)
training.insert(12, "radius",None,True)

for i in range(len(training['chr'])):
	training['midpoint'][i] = (training['chr_start'][i] + training['chr_end'][i])/2
	training['radius'][i] = training['chr_end'][i] - training['midpoint'][i]
print(training)


print(training)
export_csv = training.to_csv('training.csv', index = None, header = True)



#-------------------------------------------------------------------------
#	split dataframe
training1 = training[training['chr'] == 1]
training2 = training[training['chr'] == 2]
training3 = training[training['chr'] == 3]
training4 = training[training['chr'] == 4]
training5 = training[training['chr'] == 5]
training6 = training[training['chr'] == 6]
training7 = training[training['chr'] == 7]
training8 = training[training['chr'] == 8]
training9 = training[training['chr'] == 9]
training10 = training[training['chr'] == 10]
training11 = training[training['chr'] == 11]
training12 = training[training['chr'] == 12]

print(len(training1.chr))
print(len(training2.chr))
print(len(training3.chr))
print(len(training4.chr))
print(len(training5.chr))
print(len(training6.chr))
print(len(training7.chr))
print(len(training8.chr))
print(len(training9.chr))
print(len(training10.chr))
print(len(training11.chr))
print(len(training12.chr))

export_csv = training1.to_csv('training1.csv', index = None, header = True)
export_csv = training2.to_csv('training2.csv', index = None, header = True)
export_csv = training3.to_csv('training3.csv', index = None, header = True)
export_csv = training4.to_csv('training4.csv', index = None, header = True)
export_csv = training5.to_csv('training5.csv', index = None, header = True)
export_csv = training6.to_csv('training6.csv', index = None, header = True)
export_csv = training7.to_csv('training7.csv', index = None, header = True)
export_csv = training8.to_csv('training8.csv', index = None, header = True)
export_csv = training9.to_csv('training9.csv', index = None, header = True)
export_csv = training10.to_csv('training10.csv', index = None, header = True)
export_csv = training11.to_csv('training11.csv', index = None, header = True)
export_csv = training12.to_csv('training12.csv', index = None, header = True)
