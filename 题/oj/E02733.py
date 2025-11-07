a=int(input())
if a%4==0:
    if a%100==0:
        if a%400==0:
            print('Y')
        else:
            print('N')
    if a%3200==0:
        print('N')
    if a%100!=0:
        print('Y')
else:
    print('N')