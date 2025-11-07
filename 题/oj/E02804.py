dict={}
word=[]
while True:
   a=input().strip()
   b=a.split()
   if len(b)==2:
       dict[b[1]]=b[0]
   elif len(b)==1:
       word.append(b[0])
   if a=='':
       break

while True:
    try:
        a=input().strip()
        if a=='':
            break
        word.append(a)
    except EOFError:
        break
for i in word:
    if i in dict:
        print(dict[i])
    else: 
        print('eh')
