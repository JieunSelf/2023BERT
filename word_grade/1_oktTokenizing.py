# Tokenizing for word grade (tokenizer : konlpy.okt)
# output file : ../corpus/age_sentence_okt_tokens_2.tsv

from konlpy.tag import Okt
import pandas as pd

okt = Okt()
in_f = '../corpus/age_sentence.tsv'
out_f = '../corpus4/5_sentence/age_sentence_okt_tokens.tsv'

dataset = pd.read_csv(in_f, delimiter='\t')
selected_tokens = []

# funcion for extracting only the tokens for word grade
def okt_select_tokens(tokens):
    selected = []
    for j in okt.pos(tokens, stem=True):
        if j[1] in ['Noun', 'Verb', 'Adjective', 'Adverb']:
            selected.append(j[0])
    return (' '.join(selected)).strip()

for i in dataset['sentence']:
    selected_tokens.append(okt_select_tokens(i))

dataset['okt_tokens'] = selected_tokens
dataset.to_csv(out_f, sep='\t')