# funkcje zagnieżdżone, funkcje wewnętrzne
# funkcja w funkcji
# wykorzystywane w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwrócimy adres funkcji


fun1()
func = fun1()
print(func)  # <function fun1.<locals>.fun2 at 0x1029e37e0>
print(type(func))  # <class 'function'>
func()  # To jest fun2
