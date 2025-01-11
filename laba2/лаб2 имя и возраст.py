def describe_person(name,age=30):
    return('Имя: '+ name +', возраст:'+ str(age))
name=input()
age=int(input())
print(describe_person(name,age))
