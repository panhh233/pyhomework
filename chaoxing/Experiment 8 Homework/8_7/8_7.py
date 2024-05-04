import requests, jieba

url = 'https://baike.baidu.com/item/Python/407313?fr=ge_ala'

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text
    words = jieba.lcut(content)
    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    words_freq_sorted = sorted(words_freq.items(), key = lambda x: x[1], reverse = True)
    print(words_freq_sorted[:5])

except requests.exceptions.RequestException as error:
    print(str(error))