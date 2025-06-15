# napisać dekorator, który zmieni wynik działania funkcji na duże litery
from colorama import init, Fore, Style

init(autoreset=True)


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper  # adres funkcji


# bold_decorator \033[1m , \033[0m
def bold_decorator(func):
    def wrapper():
        result = func()
        # return f"\033[1m" + result + "\033[0m"
        # return Fore.RED + result  # HELLO WORLD! kolor czerwony
        return Style.BRIGHT + result  # HELLO WORLD!

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!"


# kolejność ma znaczenie
@bold_decorator
@uppercase_decorator
def greeting2():
    return "Hello World!"


print(greeting())  # Hello World! bez dekoratora
# po uzyciu dekoratora uppercase: HELLO WORLD!
print(greeting2())
