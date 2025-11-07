k=int(input())
s=str(input())
dict1={}
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=[]
for i in range(26):
    dict1[letters[i]]=letters[(i-k)%26]
for i in range(len(s)):
    if s[i] in dict1:
        word.append(dict1[s[i]])
    elif s[i].lower() in dict1:
        word.append(dict1[s[i].lower()].upper())
print(''.join(word))