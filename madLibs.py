#!python3
import re
file = open(r'C:\Users\Administrator\Desktop\Macbook\madlibs.txt')
words = file.read()
file.close()
keywordsRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
mo = keywordsRegex.findall(words)
for keyword in mo:
    keyword = keyword.lower()
    if keyword == 'adjective':
        replaceword = input(f'Enter an {keyword}:\n')
    else:
        replaceword = input(f'Enter a {keyword}:\n')
    words = keywordsRegex.sub(replaceword,words,1)
print("填词完成！")
file = open(r'C:\Users\Administrator\Desktop\Macbook\New_madlibs.txt','w')
file.write(words)
file.close()