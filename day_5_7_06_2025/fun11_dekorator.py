# dekorator - funkcja opakowująca inną funkcję dodatkową funkcjonalnością
# jako argument przyjmuje funkcję
# wykorzystują zasady funkcji wewnętrznej
def dekor(func):
    def wew():
        print("Dekoruj")
        return func()

    return wew


@dekor # dekorator
def hej():
    print("Hej!")


hej()
# Dekoruj
# Hej!
