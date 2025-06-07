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

