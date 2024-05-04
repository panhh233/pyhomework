import jieba

with open(r'歌唱祖国.txt', 'r', encoding = 'utf-8') as file:
    content = file.read()
    words = jieba.lcut(content)
    words_freq = {}
    for word in words:
        if len(word) < 2:
            continue
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    
    words_freq_sorted = sorted(words_freq.items(), key = lambda x: x[1], reverse = True)
    print(words_freq_sorted[:5])