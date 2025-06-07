def allparams(a, b, /, c, **kwargs):
    print(a, b, c)
    print(kwargs)


allparams(1, 2, 3)
allparams(1, 2, c=9)  # 1 2 9
# TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# po dodaniu /
# a i b muszą byc tylko po pozycji przekazane
# allparams(a=1, b=2, c=8)
allparams(1, 2, c=9)  # 1 2 9
allparams(1, 2, c=9, a=8)  # {'a': 8}
allparams(1, 2, 3, a=8, name="Radek")  # 1 2 3,{'a': 8, 'name': 'Radek'}


def allparams_all(a, b, /, c=43, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f'{args=}')
    print(f'{kwargs=}')


allparams_all(1, 2)
# a=1, b=2
# c=43, d=256
# args=()
# kwargs={}
allparams_all(1, 2, 3)
# a=1, b=2
# c=3, d=256
# args=()
# kwargs={}
allparams_all(1, 2, c=90)
# a=1, b=2
# c=90, d=256
# args=()
# kwargs={}
# zeby przekazac do args, c musi byc pozycyjne
allparams_all(1, 2, 90, 2, 4, 5, 6)
# a=1, b=2
# c=90, d=256
# args=(2, 4, 5, 6)
# kwargs={}
allparams_all(1, 2, 90, 2, 4, 5, 6, 7, 8, 9, 10)
# a=1, b=2
# c=90, d=256
# args=(2, 4, 5, 6, 7, 8, 9, 10)
# kwargs={}
# przy takiej konstrukcji funkcji d możemy przekazac tylko po nazwie
allparams_all(1, 2, 90, 2, 4, 5, 6, 7, 8, 9, 10, d=100)
# a=1, b=2
# c=90, d=100
# args=(2, 4, 5, 6, 7, 8, 9, 10)
# kwargs={}
allparams_all(1, 2, 90, 2, 4, 5, 6, 7, 8, 9, 10, d=100, name="Radek")
# a=1, b=2
# c=90, d=100
# args=(2, 4, 5, 6, 7, 8, 9, 10)
# kwargs={'name': 'Radek'}
allparams_all(1, 2, 90, 2, 4, 5, 6, 7, 8, 9, 10, d=100, name="Radek", a=89)
# a=1, b=2
# c=90, d=100
# args=(2, 4, 5, 6, 7, 8, 9, 10)
# kwargs={'name': 'Radek', 'a': 89} - a trafia do kwargs
