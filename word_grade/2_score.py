# use api_score.word_score 
# sample output : ../corpus/age_sentence_grades_1.tsv

import api_score
import pandas as pd

in_f = '../corpus4/5_sentence/age_sentence_okt_tokens_2.tsv'
df = pd.read_csv(in_f, sep='\t', index_col=0)
df2 = df.iloc[0:100].copy()

new_tokens = []
for i in df2['okt_tokens']:
    new_i = str(i).split()
    new_tokens.append(new_i)

word_grade = []
for i in new_tokens:
    tokens_grade = []
    for j in i:
        grade = api_score.word_score(j.replace("'", ""))
        tokens_grade.append(grade)
    word_grade.append(tokens_grade)

df2['grades'] = word_grade
df2.to_csv('../corpus/age_sentence_grades_1.tsv', sep='\t')