try:
    with open('ed.txt','r') as file:
        cont=file.read()
        pass
except FileNotFoundError:
    print('файл не найден')
