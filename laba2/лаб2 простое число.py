def is_prime(n):
    a=set()
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            a.add(d)
            a.add(n//d)
    if len(a)==2:
        return(True)
    else:
        return(False)
n=int(input())
print(is_prime(n))
