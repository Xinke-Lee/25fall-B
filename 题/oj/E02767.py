code={'A':'V','B':'W','C':'X','D':'Y','E':'Z','F':'A','G':'B','H':'C','I':'D','J':'E','K':'F','L':'G','M':'H','N':'I','O':'J','P':'K','Q':'L','R':'M','S':'N','T':'O','U':'P','V':'Q','W':'R','X':'S','Y':'T','Z':'U'}
word=str(input())
words=[]
for i in range(len(word)):
    words.append(word[i])
for i in range(len(words)):
    if word[i] in code:
        words[i]=code[word[i]]
print(''.join(words))