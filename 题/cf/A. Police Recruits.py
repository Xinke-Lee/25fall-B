n = int(input().strip())
a= list(map(int, input().split()))
police=0
criminal=0
for i in a:
   if i!=-1:
      police+=i
   else:
      if police>0:
         police-=1
      else:
         criminal+=1
print(criminal) 