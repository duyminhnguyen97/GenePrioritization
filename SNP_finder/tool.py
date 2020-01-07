import pandas as pd


#	function to get gene
def get_gene(input_set, data_set):
	snp_input = pd.read_csv('../SNP_finder/input/split_by_chr/' + input_set, engine = 'python')
	data_input = pd.read_csv('../SNP_finder/train_data/' + data_set, engine = 'python')
	result = pd.DataFrame(data = None, columns = ['snp_gap_id', 'gene_name', 'score'])
	header = list(snp_input.columns.values)

	#	get gene + score
	for k in range (1,8):
		trait_input = snp_input[snp_input[header[k]] == 1].reset_index(drop = True)
		train_data = data_input[data_input[header[k]] == 1].reset_index(drop = True)
		result_1 = pd.DataFrame(data = None, columns = ['snp_gap_id', 'gene_name', 'score'])
		result_1['snp_gap_id'] = trait_input['snp_gap_id']

		for i in range(len(trait_input['chr'])):
			for j in range(len(train_data['chr'])):
				if trait_input.chr_pos[i] > train_data.midpoint[j]:
					if j == (len(train_data['chr']) - 1):
						dis1 = trait_input.chr_pos[i] - train_data.midpoint[(j-1)]
						if dis1 < train_data.radius[(j-1)]:
							result_1.gene_name[i] = train_data.gene_name[(j-1)]
							result_1.score[i] = 100
							break
						else:
							score1 = (train_data.radius[(j-1)] / dis1)*100
							result_1.gene_name[i] = train_data.gene_name[(j-1)]
							result_1.score[i] = score1
							break
					else:
						continue

				if j == 0:
					dis2 = train_data.midpoint[j] - trait_input.chr_pos[i]
					if dis2 < train_data.radius[j]:
						result_1.gene_name[i] = train_data.gene_name[j]
						result_1.score[i] = 100
						break
					else:
						score2 = (train_data.radius[j] / dis2)*100
						result_1.gene_name[i] = train_data.gene_name[j]
						result_1.score[i] = score2
						break

				dis1 = trait_input.chr_pos[i] - train_data.midpoint[(j-1)]
				dis2 = train_data.midpoint[j] - trait_input.chr_pos[i]
				
				if dis1 < train_data.radius[(j-1)]:
					result_1.gene_name[i] = train_data.gene_name[(j-1)]
					result_1.score[i] = 100
					break

				if dis2 < train_data.radius[j]:
					result_1.gene_name[i] = train_data.gene_name[j]
					result_1.score[i] = 100
					break

				else:
					score1 = (train_data.radius[(j-1)] / dis1)*100
					score2 = (train_data.radius[j] / dis2)*100
					if score1 > score2:
						result_1.gene_name[i] = train_data.gene_name[(j-1)]
						result_1.score[i] = score1
						break
					else:
						result_1.gene_name[i] = train_data.gene_name[j]
						result_1.score[i] = score2
						break
					
		result = result.append(result_1)
	return result

#	call function
chr1 = get_gene('input_1.csv', 'training1.csv').sort_values(by = ['snp_gap_id'])
chr2 = get_gene('input_2.csv', 'training2.csv').sort_values(by = ['snp_gap_id'])
chr3 = get_gene('input_3.csv', 'training3.csv').sort_values(by = ['snp_gap_id'])
chr4 = get_gene('input_4.csv', 'training4.csv').sort_values(by = ['snp_gap_id'])
chr5 = get_gene('input_5.csv', 'training5.csv').sort_values(by = ['snp_gap_id'])
chr6 = get_gene('input_6.csv', 'training6.csv').sort_values(by = ['snp_gap_id'])
chr7 = get_gene('input_7.csv', 'training7.csv').sort_values(by = ['snp_gap_id'])
chr8 = get_gene('input_8.csv', 'training8.csv').sort_values(by = ['snp_gap_id'])
chr9 = get_gene('input_9.csv', 'training9.csv').sort_values(by = ['snp_gap_id'])
chr10 = get_gene('input_10.csv', 'training10.csv').sort_values(by = ['snp_gap_id'])
chr11 = get_gene('input_11.csv', 'training11.csv').sort_values(by = ['snp_gap_id'])
chr12 = get_gene('input_12.csv', 'training12.csv').sort_values(by = ['snp_gap_id'])

print(chr1)
print(chr2)
print(chr3)
print(chr4)
print(chr5)
print(chr6)
print(chr7)
print(chr8)
print(chr9)
print(chr10)
print(chr11)
print(chr12)

#final = pd.DataFrame(data = None, columns = ['snp_gap_id', 'gene_name', 'score'])
final = pd.concat([chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chr10,chr11,chr12]).reset_index(drop = True)

final = final.sort_values(by = ['snp_gap_id'])
print(final)

export_csv = final.to_csv('result.csv', index = None, header = True)