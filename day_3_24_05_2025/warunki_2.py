# # od pythona 3.10 istniej match case
#
# lista = []
# lang = input("podaj znany Ci język programowania")
#
# match lang.casefold().strip():
#     case "python":
#         print("Lubię pythona")
#         lista.append(lang.capitalize())
#     case "java":
#         print("Java to kawa")
#         lista.append(lang.capitalize())
#     case "c++":
#         print("To za trudne")
#         lista.append(lang.capitalize())
#     case _:  # odpowiednik else
#         print("Nie znam takiego języka")
#
# print(f'Lista z odpowiedziami {lista}')
# # Java to kawa
# # Lista z odpowiedziami ['java']

# dane = [1, 2, 3]
dane = {"nazwa": 'Radek', "wiek": 45}
match dane:
    case [a, b, c]:
        print(f"Lista z trzema elementami {a=}, {b=}, {c=}")
    case {'nazwa': n, "wiek": w}:
        print(f"Słownik reprezentujący osobę {n}, wiek {w}")
    case _:
        print("Błędny typ danych")
# Lista z trzema elementami a=1, b=2, c=3
# Słownik reprezentujący osobę Radek, wiek 45
