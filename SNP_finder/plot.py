import pandas as pd
import matplotlib.pyplot as plt

result_trait = pd.read_csv('result.csv', engine = 'python')
result_notrait = pd.read_csv('result_para.csv', engine = 'python')

final = pd.merge(result_trait, result_notrait, how='inner', on=['snp_gap_id'])
final = final.rename(columns={"score_x": "score_trait", "score_y": "score_notrait", 'gene_name_x': 'gene_name_trait', 'gene_name_y': 'gene_name_notrait'})
final['match'] = None


for i in range(len(final.index)):
	if final['score_trait'][i] == final['score_notrait'][i]:
		final['match'][i] = 1
	else:
		final['match'][i] = 0


print(final)
export_csv = final.to_csv('final.csv', index = None, header = True)


#	plot
snp_id = final.snp_gap_id
score_trait = final.score_trait
score_notrait = final.score_notrait


fig = plt.figure(figsize = (15,5))
ax = fig.add_axes([0,0,1,1])
ax.scatter(snp_id, score_trait, color='r')
ax.set_xlabel('SNP ID')
ax.set_ylabel('score')
ax.set_title('SNP with trait class')
plt.show()



fig = plt.figure(figsize = (15,5))
ax = fig.add_axes([0,0,1,1])
ax.scatter(snp_id, score_notrait, color='b')
ax.set_xlabel('SNP ID')
ax.set_ylabel('score')
ax.set_title('SNP without trait class')
plt.show()
