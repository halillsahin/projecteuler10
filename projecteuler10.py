asallar=2
a=3
while a<2000000:
    for i in range(2,int((a**0.5)+1)):
        if a%i==0:
            a+=1
            break
    else:
        asallar+=a
        a+=1
print(asallar)