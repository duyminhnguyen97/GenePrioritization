import pandas as pd

#	import snp
snp_data = pd.read_csv('Rice_Association.csv', dtype = 'str', engine = 'python')
snp_data['Chr'] = snp_data['Chr'].replace({'chr':''}, regex=True)
int_head = ['Chr', '#GaP_id', 'Chr_Pos']
snp_data[int_head] = snp_data[int_head].astype(int)
#snp_data = snp_data.dropna(axis = 'index', subset = ['Trait_ontology'], how = 'all')
#print(snp_data)

number = [None]*12
for i in range(12):
	number[i] = len(snp_data[snp_data['Chr'] == (i+1)])
#print('Number of SNP in Chr: ',number)


#	headers
headers = pd.read_csv('head.txt', header = None, dtype = 'str', engine = 'python')
headers = list(headers[0])
#print(headers)


#	input form for all snp
snp_trait = pd.DataFrame(data = None, columns = headers)
snp_trait[headers] = snp_trait[headers].astype(int)
snp_trait['snp_gap_id'] = snp_data['#GaP_id']
snp_trait['chr'] = snp_data['Chr']
snp_trait['chr_pos'] = snp_data['Chr_Pos']

'''
#	biochemical character
biochemical_character = snp_data[snp_data['Trait_ontology'].str.contains('Physiology', regex = False)]
biochemical_character = biochemical_character.append(snp_data[snp_data['Trait_ontology'].str.contains('biochemical trait', regex = False)])
biochemical_character_index = biochemical_character.index
for i in range(len(biochemical_character_index)):
	snp_trait.at[biochemical_character_index[i],'biochemical_character'] = 1


#	vegetative_organ
vegetative_organ = snp_data[snp_data['Trait_ontology'].str.contains('Peduncle vascular bundle', regex = False)]
vegetative_organ = vegetative_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('Plant Morphology', regex = False)])
vegetative_organ = vegetative_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('Plant morphology', regex = False)])
vegetative_organ = vegetative_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('Root traits', regex = False)])
vegetative_organ = vegetative_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('plant morphology trait', regex = False)])
vegetative_organ = vegetative_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('root traits', regex = False)])
vegetative_organ_index = vegetative_organ.index
for i in range(len(vegetative_organ_index)):
	snp_trait.at[vegetative_organ_index[i],'vegetative_organ'] = 1


#	reproductive_organ
reproductive_organ = snp_data[snp_data['Trait_ontology'].str.contains('Grain quality', regex = False)]
reproductive_organ = reproductive_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('agronomic traits', regex = False)])
reproductive_organ = reproductive_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('agronomical traits', regex = False)])
reproductive_organ = reproductive_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('biological process trait', regex = False)])
reproductive_organ = reproductive_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('plant growth and development trait', regex = False)])
reproductive_organ = reproductive_organ.append(snp_data[snp_data['Trait_ontology'].str.contains('sterility or fertility trait', regex = False)])
reproductive_organ_index = reproductive_organ.index
for i in range(len(reproductive_organ_index)):
	snp_trait.at[reproductive_organ_index[i],'reproductive_organ'] = 1


#	seed
seed = snp_data[snp_data['Trait_ontology'].str.contains('Rice eating and cooking quality', regex = False)]
seed = seed.append(snp_data[snp_data['Trait_ontology'].str.contains('Seed Morphology', regex = False)])
seed_index = seed.index
for i in range(len(seed_index)):
	snp_trait.at[seed_index[i],'seed'] = 1


#	tolerance_resistance
tolerance_resistance = snp_data[snp_data['Trait_ontology'].str.contains('Manganese toxicity tolerance', regex = False)]
tolerance_resistance = tolerance_resistance.append(snp_data[snp_data['Trait_ontology'].str.contains('Physiological traits', regex = False)])
tolerance_resistance = tolerance_resistance.append(snp_data[snp_data['Trait_ontology'].str.contains('Salt Tolerance', regex = False)])
tolerance_resistance = tolerance_resistance.append(snp_data[snp_data['Trait_ontology'].str.contains('abiotic stress trait', regex = False)])
tolerance_resistance = tolerance_resistance.append(snp_data[snp_data['Trait_ontology'].str.contains('biotic stress trait', regex = False)])
tolerance_resistance_index = tolerance_resistance.index
for i in range(len(tolerance_resistance_index)):
	snp_trait.at[tolerance_resistance_index[i],'tolerance_resistance'] = 1


#	QTL
QTL = snp_data[snp_data['Trait_ontology'].str.contains('Yield', regex = False)]
QTL = QTL.append(snp_data[snp_data['Trait_ontology'].str.contains('plant quality trait', regex = False)])
QTL = QTL.append(snp_data[snp_data['Trait_ontology'].str.contains('quality traits', regex = False)])
QTL = QTL.append(snp_data[snp_data['Trait_ontology'].str.contains('yield trait', regex = False)])
QTL = QTL.append(snp_data[snp_data['Trait_ontology'].str.contains('Phenology', regex = False)])
QTL = QTL.append(snp_data[snp_data['Trait_ontology'].str.contains('plant vigor trait', regex = False)])
QTL_index = QTL.index
for i in range(len(QTL_index)):
	snp_trait.at[QTL_index[i],'QTL'] = 1


#	eliminate Nan
headers1 = ['biochemical_character', 'vegetative_organ', 'reproductive_organ', 'seed', 'tolerance_resistance', 'QTL']
snp_trait = snp_trait.dropna(axis = 'index', subset = headers1, how = 'all')
snp_trait = snp_trait.fillna(0)
snp_trait[headers1] = snp_trait[headers1].astype(int)


#	sort trait by chr
snp_trait = snp_trait.sort_values(by = ['chr', 'chr_pos'])
snp_trait = snp_trait.reset_index(drop = True)
'''

print(snp_trait)
export_csv = snp_trait.to_csv('input.csv', index = None, header = True)
