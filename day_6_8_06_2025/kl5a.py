# stworzyć słownik, który ma metoda wyszukiwania najdłuższego klucza w słowniku

class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None)) # TypeError: object of type 'NoneType' has no len()

art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 17
print(art.longest_key())  # abraham
# assert służy do sprawdzania poprawności wyniku
# assert warunek -> komunikat błedu
assert 'abraham' == art.longest_key()  # nie ma błedu, jest ok


# assert 'zen' == art.longest_key()  # AssertionError

class LongestKeyDictMax(dict):
    def longest_key(self):
        return max(self.keys(), key=len)


art = LongestKeyDictMax()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 17
print(art.longest_key())  # abraham
assert 'abraham' == art.longest_key()
# assert 'zen' == art.longest_key()  # AssertionError
