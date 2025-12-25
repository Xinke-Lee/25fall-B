keyword=input()
keyword=keyword.replace('j','i')
l=len(keyword)
characters_0=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
characters=[]
for i in range(l):
    if keyword[i] not in characters:
        characters.append(keyword[i])
for j in characters_0:
    if j not in characters:
        characters.append(j)
matrix=[['']*5 for _ in range(5)]
x=0
y=0
ind=0
while ind<25:
    matrix[y][x]=characters[ind]
    ind+=1
    x+=1
    if x==5:
        y+=1
        x=0

def get_index(s):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==s:
                return i,j
    return None


n=int(input())
for _ in range(n):
    word=input()
    word=word.replace('j','i')
    length=len(word)
    ind_1=0
    ans=''
    pairs=[]
    while ind_1<length-1:
        if word[ind_1]!=word[ind_1+1]:
            pairs.append(word[ind_1]+word[ind_1+1])
            ind_1+=2
        else:
            if word[ind_1]!='x':
                pairs.append(word[ind_1]+'x')
                ind_1+=1
            else:
                pairs.append(word[ind_1]+'q')
                ind_1+=1
    if ind_1==length-1:
        if word[ind_1]!='x':
            pairs.append(word[ind_1]+'x')
        else:
            pairs.append(word[ind_1]+'q')
    for s in pairs:
        y1,x1=get_index(s[0])
        y2,x2=get_index(s[1])
        if y1==y2:
            if x1+1<5:
                a1=x1+1
            else:
                a1=0
            if x2+1<5:
                a2=x2+1
            else:
                a2=0
            ans+=matrix[y1][a1]+matrix[y2][a2]
        elif x1==x2:
            if y1+1<5:
                b1=y1+1
            else:
                b1=0
            if y2+1<5:
                b2=y2+1
            else:
                b2=0
            ans+=matrix[b1][x1]+matrix[b2][x2]
        else:
            ans+=matrix[y1][x2]+matrix[y2][x1]
    print(ans)