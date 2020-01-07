import pandas as pd


#	headers
headers = pd.read_csv('head.txt', header = None, dtype = 'str', engine = 'python')
headers = list(headers[0])


#	imput snp trait table
snp_trait = pd.read_csv('input.csv', dtype = 'str', engine = 'python')
headers1 = ['biochemical_character', 'vegetative_organ', 'reproductive_organ','coloration' , 'seed', 'tolerance_resistance', 'QTL']
snp_trait = snp_trait.dropna(axis = 'index', subset = headers1, how = 'all')
snp_trait = snp_trait.fillna(0)
snp_trait[headers] = snp_trait[headers].astype(int)


#	input chr 1
input_1 = snp_trait[snp_trait['chr'] == 1]
input_1 = input_1.sort_values(by = ['snp_gap_id'])
export_csv = input_1.to_csv('input_1.csv', index = None, header = True)

#	input chr 2
input_2 = snp_trait[snp_trait['chr'] == 2]
input_2 = input_2.sort_values(by = ['snp_gap_id'])
export_csv = input_2.to_csv('input_2.csv', index = None, header = True)

#	input chr 3
input_3 = snp_trait[snp_trait['chr'] == 3]
input_3 = input_3.sort_values(by = ['snp_gap_id'])
export_csv = input_3.to_csv('input_3.csv', index = None, header = True)

#	input chr 4
input_4 = snp_trait[snp_trait['chr'] == 4]
input_4 = input_4.sort_values(by = ['snp_gap_id'])
export_csv = input_4.to_csv('input_4.csv', index = None, header = True)

#	input chr 5
input_5 = snp_trait[snp_trait['chr'] == 5]
input_5 = input_5.sort_values(by = ['snp_gap_id'])
export_csv = input_5.to_csv('input_5.csv', index = None, header = True)

#	input chr 6
input_6 = snp_trait[snp_trait['chr'] == 6]
input_6 = input_6.sort_values(by = ['snp_gap_id'])
export_csv = input_6.to_csv('input_6.csv', index = None, header = True)

#	input chr 7
input_7 = snp_trait[snp_trait['chr'] == 7]
input_7 = input_7.sort_values(by = ['snp_gap_id'])
export_csv = input_7.to_csv('input_7.csv', index = None, header = True)

#	input chr 8
input_8 = snp_trait[snp_trait['chr'] == 8]
input_8 = input_8.sort_values(by = ['snp_gap_id'])
export_csv = input_8.to_csv('input_8.csv', index = None, header = True)

#	input chr 9
input_9 = snp_trait[snp_trait['chr'] == 9]
input_9 = input_9.sort_values(by = ['snp_gap_id'])
export_csv = input_9.to_csv('input_9.csv', index = None, header = True)

#	input chr 10
input_10 = snp_trait[snp_trait['chr'] == 10]
input_10 = input_10.sort_values(by = ['snp_gap_id'])
export_csv = input_10.to_csv('input_10.csv', index = None, header = True)

#	input chr 11
input_11 = snp_trait[snp_trait['chr'] == 11]
input_11 = input_11.sort_values(by = ['snp_gap_id'])
export_csv = input_11.to_csv('input_11.csv', index = None, header = True)

#	input chr 12
input_12 = snp_trait[snp_trait['chr'] == 12]
input_12 = input_12.sort_values(by = ['snp_gap_id'])
export_csv = input_12.to_csv('input_12.csv', index = None, header = True)


print(len(input_1.index))
print(len(input_2.index))
print(len(input_3.index))
print(len(input_4.index))
print(len(input_5.index))
print(len(input_6.index))
print(len(input_7.index))
print(len(input_8.index))
print(len(input_9.index))
print(len(input_10.index))
print(len(input_11.index))
print(len(input_12.index))

print('Done!')