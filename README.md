# Text Classification
## 1. 실습 소개
- 만 6~18세의 아동 및 청소년 저자의 생활문 텍스트를 대상으로 저자의 연령을 프로파일링 하고자 함. 
- 본 프로젝트는 두 개의 실습으로 구성되어 있음. 
  
  (1) word_grade : 국립국어원 '한국어 기초사전'에서 제공하는 어휘 등급을 활용하여 연령별 어휘 사용 수준 정도를 분석함.  
  (2) classification : BERT 계열의 모델을 활용하여 text classification을 진행함.
   


## 2. corpus
- 실험 데이터 : 국립국어원 모두의 말뭉치에서 제공되는 '국립국어원 비출판물 말뭉치' 중 만 6~18세 저자의 일기와 수필글
- https://corpus.korean.go.kr/request/reausetMain.do?lang=ko
  
  
- 예시
   
```xml
<?xml version="1.0" encoding="UTF-8"?>
<SJML>
    <header>
        <fileInfo>
            <fileId>WDRW1900102137</fileId>
            <annoLevel>원시</annoLevel>
            <category>비출판물 > 일기</category>
        </fileInfo>
        <sourceInfo>
            <title>초코파이</title>
            <author id="P02137" age="6" occupation="고등학생" sex="F" submission="온라인" handwriting="No">개인글작성자</author>
        </sourceInfo>
    </header>
    <text date="20090000" subclass="null_게임">
        <p>엄마가 어제 초코파이를 사주셨다. 그래서 하나 먹으려고 했지만 엄마가 안 된다고 했다. 그 전에는 오빠 머리를 깎고 왔었다. 그 전에는 마다가스카 2를 보고 있었다. 애니메이션이 다 끝나서 집에 갔어. 그런데 오빠가 게임을 해서 내가 보고있는데 오빠가 남자캐릭터를 새로 골랐길래 내가 마법사 캐릭터도 하라고 했어. 마법사 이름을 정하고 게임을 계속하다가 나는 씻었다.</p>
    </text>
</SJML>
```

## 3. 전처리
- KSS(Korean Sentence Splitter) 라이브러리를 사용하여 문장 분리
- 문장의 길이가 10글자 이하 또는 300자 이상의 문장은 제외
- 총 3,626개의 글에 대해 47,775개의 문장으로 분리됨
- 형태소 분석기 Mecab을 활용한 토큰화(tokenization) 작업
- 토큰화된 단어 중 불용어(조사, 구두점, 감탄사 등) 제거
## 4. 결과
- [국립국어원 한국어기초사전 Open API](https://krdict.korean.go.kr/openApi/openApiInfo)을 활용하여 토큰화된 어휘를 초급, 중급, 고급 각각의 등급에 따라 1~3점으로 점수를 부여하고 어휘 수준을 수치화함.
- 어휘 수준 점수를 계산한 결과, 만 6~11세의 저자들은 평균 1.238점, 만 12~18세의 저자들은 평균 1.306점으로 나타남(p<.05). 즉, 연령이 높은 저자 집단이 상대적으로 고급 어휘를 많이 사용하고 있음. 
  


| 분류 | 평균(M)    | 표준편차(SD)    |
| :---:   | :---: | :---: |
| 만 6~11세 | 1.238   | 0.269   |
| 만 12~18세 | 1.306   | 0.244   |

- 사전 학습 모델로는 구글에서 공개한 multilingual BERT, 한국어 데이터로 학습한 모델 중 오픈소스로 공개되어 있는 KoBERT, KoELECTRA base-v3 버전의 모델을 사용하여 그 성능을 비교함. 

| Model | 개발    | 학습 코퍼스    | Tokenizer | Vocab |
| :---:   | :---: | :---: | :---: | :---: |
| multilingual BERT | Google  | 104개 언어의 위키피디아  | Wordpiece | 110,000
| KoBERT | SKT   | 위키피디아와 뉴스 등에서 <br> 수집한 수백만 개의 한국어 문장  | SentencePiece | 8,002 |
|KoELECTRA base-v3 | 개인(박장원) | 한국어, 뉴스, 위키백과, <br> 나무위키, 모두의 말뭉치 등 약 34GB의 말뭉치 | Wordpiece | 35,000


- 각 모델의 성능을 평가한 결과는 다음 표와 같으며, KoELECTRA 모델이 가장 높은 성능을 나타냄. 
  
| Model | accuracy    | precision    | recall | F-score |
| :---:   | :---: | :---: | :---: | :---: |
| multilingual BERT | 0.8397  | 0.8548  | 0.8729 | 0.8638
| KoBERT | 0.8637   | 0.8799  |  0.8871 | 0.8835 |
|KoELECTRA base-v3 | 0.8674 | 0.8736 | 0.9029 | 0.8880


