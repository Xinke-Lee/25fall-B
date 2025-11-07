a=str(input())
b=(list(a))
for i in range(len(a)):
    if a[i].isupper():
        b[i]=a[i].lower()
    else:
        b[i]=a[i].upper()
print(''.join(b))
