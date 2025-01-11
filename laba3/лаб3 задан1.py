'''f=open('ab.txt','r')
for i in f:
    print(i)'''
with open('ab.txt','r') as file:
    cont=file.read()
print(cont)
