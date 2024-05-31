import requests, jieba, bs4

url = 'https://baike.baidu.com/item/Python/407313?fr=ge_ala'
header = {'user-agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=header, timeout=10)
    response.encoding = response.apparent_encoding
    #content = bs4.BeautifulSoup(response.text, 'html.parser').get_text()
    words = jieba.lcut(response.text, cut_all=False)
    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    words_freq_sorted = sorted(words_freq.items(), key=lambda x: x[1], reverse=True)
    print(words_freq_sorted[:5])

except requests.exceptions.RequestException as error:
    print(str(error))
