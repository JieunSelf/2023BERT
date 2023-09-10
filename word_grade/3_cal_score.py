# calculate word score according to the number of beginner, intermediate, and advanced words
# sample output : ../corpus/grade_score_1.tsv
# the final result : ../corpus/result.tsv

import pandas as pd
import re

df_all = pd.DataFrame()
in_f = '../corpus/age_sentence_grades_1.tsv'
df = pd.read_csv(in_f, sep='\t', encoding='utf-8')
word_score = []

for i in df['grades']: 
    count = 0
    score = 0
    list_result = re.findall(r'[초중고]{1}급', i)
    for j in list_result :      
        if j == '초급':
            count +=1 
            score += 1
        elif j == '중급':
            count += 1
            score += 2
        elif j == '고급':
            count += 1
            score += 3
    final_score = 0
    if count != 0 :
        final_score = score / count
    word_score.append(final_score)

df['word_score'] = pd.Series(word_score)
df.to_csv('../corpus/grade_score_1.tsv', sep='\t')