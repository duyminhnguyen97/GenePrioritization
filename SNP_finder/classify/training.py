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
biochemical_character_index = biochemical_character.index
for i in range(len(biochemical_character_index)):
	training.at[biochemical_character_index[i],'biochemical_character'] = 1


#	vegetative_organ_SAM
vegetative_organ_SAM = gene_data[gene_data['Trait Class'].str.contains('Vegetative organ - Shoot apical meristem(SAM)', regex = False)]
vegetative_organ_SAM_index = vegetative_organ_SAM.index
for i in range(len(vegetative_organ_SAM_index)):
	training.at[vegetative_organ_SAM_index[i],'vegetative_organ_SAM'] = 1


#	vegetative_organ_leaf
vegetative_organ_leaf = gene_data[gene_data['Trait Class'].str.contains('Vegetative organ - Leaf', regex = False)]
vegetative_organ_leaf_index = vegetative_organ_leaf.index
for i in range(len(vegetative_organ_leaf_index)):
	training.at[vegetative_organ_leaf_index[i],'vegetative_organ_leaf'] = 1


#	vegetative_organ_culm
vegetative_organ_culm = gene_data[gene_data['Trait Class'].str.contains('Vegetative organ - Culm', regex = False)]
vegetative_organ_culm_index = vegetative_organ_culm.index
for i in range(len(vegetative_organ_culm_index)):
	training.at[vegetative_organ_culm_index[i],'vegetative_organ_culm'] = 1


#	vegetative_organ_root
vegetative_organ_root = gene_data[gene_data['Trait Class'].str.contains('Vegetative organ - Root', regex = False)]
vegetative_organ_root_index = vegetative_organ_root.index
for i in range(len(vegetative_organ_root_index)):
	training.at[vegetative_organ_root_index[i],'vegetative_organ_root'] = 1


#	reproductive_organ_heading_date
reproductive_organ_heading_date = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ - Heading date', regex = False)]
reproductive_organ_heading_date_index = reproductive_organ_heading_date.index
for i in range(len(reproductive_organ_heading_date_index)):
	training.at[reproductive_organ_heading_date_index[i],'reproductive_organ_heading_date'] = 1


#	reproductive_organ_inflorescence
reproductive_organ_inflorescence = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ - Inflorescence', regex = False)]
reproductive_organ_inflorescence_index = reproductive_organ_inflorescence.index
for i in range(len(reproductive_organ_inflorescence_index)):
	training.at[reproductive_organ_inflorescence_index[i],'reproductive_organ_inflorescence'] = 1


#	reproductive_organ_panicle
reproductive_organ_panicle = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ - panicle', regex = False)]
reproductive_organ_panicle_index = reproductive_organ_panicle.index
for i in range(len(reproductive_organ_panicle_index)):
	training.at[reproductive_organ_panicle_index[i],'reproductive_organ_panicle'] = 1


#	reproductive_organ_panicle_mode_branching
reproductive_organ_panicle_mode_branching = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ - Panicle, Mode of branching', regex = False)]
reproductive_organ_panicle_mode_branching_index = reproductive_organ_panicle_mode_branching.index
for i in range(len(reproductive_organ_panicle_mode_branching_index)):
	training.at[reproductive_organ_panicle_mode_branching_index[i],'reproductive_organ_panicle_mode_branching'] = 1


#	reproductive_organ_spikelet_flower_glume_awn
reproductive_organ_spikelet_flower_glume_awn = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ - Spikelet, flower, glume, awn', regex = False)]
reproductive_organ_spikelet_flower_glume_awn_index = reproductive_organ_spikelet_flower_glume_awn.index
for i in range(len(reproductive_organ_spikelet_flower_glume_awn_index)):
	training.at[reproductive_organ_spikelet_flower_glume_awn_index[i],'reproductive_organ_spikelet_flower_glume_awn'] = 1


#	reproductive_organ_pollination_fertilization_fertility
reproductive_organ_pollination_fertilization_fertility = gene_data[gene_data['Trait Class'].str.contains('Reproductive organ - Pollination, fertilization, fertility', regex = False)]
reproductive_organ_pollination_fertilization_fertility_index = reproductive_organ_pollination_fertilization_fertility.index
for i in range(len(reproductive_organ_pollination_fertilization_fertility_index)):
	training.at[reproductive_organ_pollination_fertilization_fertility_index[i],'reproductive_organ_pollination_fertilization_fertility'] = 1


#	heterochrony
heterochrony = gene_data[gene_data['Trait Class'].str.contains('Heterochrony', regex = False)]
heterochrony_index = heterochrony.index
for i in range(len(heterochrony_index)):
	training.at[heterochrony_index[i],'heterochrony'] = 1


#	coloration_anthocyanin
coloration_anthocyanin = gene_data[gene_data['Trait Class'].str.contains('Coloration - Anthocyanin', regex = False)]
coloration_anthocyanin_index = coloration_anthocyanin.index
for i in range(len(coloration_anthocyanin_index)):
	training.at[coloration_anthocyanin_index[i],'coloration_anthocyanin'] = 1


#	coloration_chlorophyll
coloration_chlorophyll = gene_data[gene_data['Trait Class'].str.contains('Coloration - Chlorophyll', regex = False)]
coloration_chlorophyll_index = coloration_chlorophyll.index
for i in range(len(coloration_chlorophyll_index)):
	training.at[coloration_chlorophyll_index[i],'coloration_chlorophyll'] = 1


#	coloration_others
coloration_others = gene_data[gene_data['Trait Class'].str.contains('Coloration - Others', regex = False)]
coloration_others_index = coloration_others.index
for i in range(len(coloration_others_index)):
	training.at[coloration_others_index[i],'coloration_others'] = 1


#	seed_morphological_traits
seed_morphological_traits = gene_data[gene_data['Trait Class'].str.contains('Seed - Morphological traits', regex = False)]
seed_morphological_traits_index = seed_morphological_traits.index
for i in range(len(seed_morphological_traits_index)):
	training.at[seed_morphological_traits_index[i],'seed_morphological_traits'] = 1


#	seed_physiological_traits
seed_physiological_traits = gene_data[gene_data['Trait Class'].str.contains('Seed - Physiological traits', regex = False)]
seed_physiological_traits_index = seed_physiological_traits.index
for i in range(len(seed_physiological_traits_index)):
	training.at[seed_physiological_traits_index[i],'seed_physiological_traits'] = 1


#	tolerance_resistance_lesion_mimic
tolerance_resistance_lesion_mimic = gene_data[gene_data['Trait Class'].str.contains('Tolerance and resistance - Lesion mimic', regex = False)]
tolerance_resistance_lesion_mimic_index = tolerance_resistance_lesion_mimic.index
for i in range(len(tolerance_resistance_lesion_mimic_index)):
	training.at[tolerance_resistance_lesion_mimic_index[i],'tolerance_resistance_lesion_mimic'] = 1


#	tolerance_resistance_disease_resistance
tolerance_resistance_disease_resistance = gene_data[gene_data['Trait Class'].str.contains('Tolerance and resistance - Disease resistance', regex = False)]
tolerance_resistance_disease_resistance_index = tolerance_resistance_disease_resistance.index
for i in range(len(tolerance_resistance_disease_resistance_index)):
	training.at[tolerance_resistance_disease_resistance_index[i],'tolerance_resistance_disease_resistance'] = 1


#	tolerance_resistance_insect_resistance
tolerance_resistance_insect_resistance = gene_data[gene_data['Trait Class'].str.contains('Tolerance and resistance - Insect resistance', regex = False)]
tolerance_resistance_insect_resistance_index = tolerance_resistance_insect_resistance.index
for i in range(len(tolerance_resistance_insect_resistance_index)):
	training.at[tolerance_resistance_insect_resistance_index[i],'tolerance_resistance_insect_resistance'] = 1


#	tolerance_resistance_stress_tolerance
tolerance_resistance_stress_tolerance = gene_data[gene_data['Trait Class'].str.contains('Tolerance and resistance - Stress tolerance', regex = False)]
tolerance_resistance_stress_tolerance_index = tolerance_resistance_stress_tolerance.index
for i in range(len(tolerance_resistance_stress_tolerance_index)):
	training.at[tolerance_resistance_stress_tolerance_index[i],'tolerance_resistance_stress_tolerance'] = 1


#	QTL_grain_quality
QTL_grain_quality = gene_data[gene_data['Trait Class'].str.contains('Character as QTL - Grain quality', regex = False)]
QTL_grain_quality_index = QTL_grain_quality.index
for i in range(len(QTL_grain_quality_index)):
	training.at[QTL_grain_quality_index[i],'QTL_grain_quality'] = 1


#	QTL_yield_productivity
QTL_yield_productivity = gene_data[gene_data['Trait Class'].str.contains('Character as QTL - Yield and productivity', regex = False)]
QTL_yield_productivity_index = QTL_yield_productivity.index
for i in range(len(QTL_yield_productivity_index)):
	training.at[QTL_yield_productivity_index[i],'QTL_yield_productivity'] = 1


#	QTL_plant_growth_activity
QTL_plant_growth_activity = gene_data[gene_data['Trait Class'].str.contains('Character as QTL - Plant growth activity', regex = False)]
QTL_plant_growth_activity_index = QTL_plant_growth_activity.index
for i in range(len(QTL_plant_growth_activity_index)):
	training.at[QTL_plant_growth_activity_index[i],'QTL_plant_growth_activity'] = 1


#	QTL_germination
QTL_germination = gene_data[gene_data['Trait Class'].str.contains('Character as QTL - Germination', regex = False)]
QTL_germination_index = QTL_germination.index
for i in range(len(QTL_germination_index)):
	training.at[QTL_germination_index[i],'QTL_germination'] = 1


#	QTL_root_activity
QTL_root_activity = gene_data[gene_data['Trait Class'].str.contains('Character as QTL - Root activity', regex = False)]
QTL_root_activity_index = QTL_root_activity.index
for i in range(len(QTL_root_activity_index)):
	training.at[QTL_root_activity_index[i],'QTL_root_activity'] = 1


#	QTL_seed_sterility
QTL_seed_sterility = gene_data[gene_data['Trait Class'].str.contains('Character as QTL - Seed sterility', regex = False)]
QTL_seed_sterility_index = QTL_seed_sterility.index
for i in range(len(QTL_seed_sterility_index)):
	training.at[QTL_seed_sterility_index[i],'QTL_seed_sterility'] = 1


#	eliminate Nan
headers1 = ['biochemical_character', 'vegetative_organ_SAM', 'vegetative_organ_leaf', 'vegetative_organ_culm', 'vegetative_organ_root', 'reproductive_organ_heading_date', 'reproductive_organ_inflorescence', 'reproductive_organ_panicle', 'reproductive_organ_panicle_mode_branching', 'reproductive_organ_spikelet_flower_glume_awn', 'reproductive_organ_pollination_fertilization_fertility', 'heterochrony', 'coloration_anthocyanin', 'coloration_chlorophyll', 'coloration_others', 'seed_morphological_traits', 'seed_physiological_traits', 'tolerance_resistance_lesion_mimic', 'tolerance_resistance_disease_resistance', 'tolerance_resistance_insect_resistance', 'tolerance_resistance_stress_tolerance', 'QTL_grain_quality', 'QTL_yield_productivity', 'QTL_plant_growth_activity', 'QTL_germination', 'QTL_root_activity', 'QTL_seed_sterility']
training = training.dropna(axis = 'index', subset = headers1, how = 'all')
training = training.fillna(0)
training[headers1] = training[headers1].astype(int)

#	sort training
training = training.sort_values(by = ['chr', 'chr_start'])
training = training.reset_index(drop = True)


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
