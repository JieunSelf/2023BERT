# https://krdict.korean.go.kr/openApi/openApiInfo 한국어기초사전 오픈 API

import requests
import xml.etree.ElementTree as ET
from fake_useragent import UserAgent


def word_score(word):
    ua = UserAgent()
    url = 'https://krdict.korean.go.kr/api/search?certkey_no=4398&key=YOURKEY&type_search=search&part=word&q={}&sort=dict'.format(
        word)  # get an authentication key (YOURKEY) by applying for the use of Open API

    headers = {"user-agent": ua.random}
    response = requests.get(url, verify=False, headers=headers).text
    root = ET.fromstring(response)

    try:
        item_1 = root.findall('item')[0]
        word_grade = item_1.find('word_grade').text
        if word_grade:
            grade = word_grade
        else:
            grade = None

    except Exception as e:
        grade = None

    return grade