def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a, b

def sum(a,b):
    s=a+b
    print(f"sum ={s}")