from pprint import pprint


class ContactList(list['Contact']):
    """
    Lista z metodą search()
    """

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name.casefold() in c.name.casefold():
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    # all_contacts = []  # pusta lista
    all_contacts = ContactList()  # pusta lista

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # __repr__ rownież zmienia __str__
    # !r dodaje  apostrrofy do stringów
    def __repr__(self):
        return f"{self.name!r} {self.email!r}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        return f"{self.name}, {self.email}"


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, mail, phone="000000000"):
        super().__init__(name, mail)
        self.phone = phone

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.email} +48{self.phone}"


lista = ContactList()
print(type(lista))  # <class '__main__.ContactList'>
print(lista)  # []

c1 = Contact("Adam", "adam@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c2.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c2.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

print(Contact.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

s1 = Suplier("Marek", "marek@o2.pl")
print(Contact.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
print(s1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]

s1.order("kawa")  # kawa zamówiono od Marek

# wypisz kontakty "Radek" z listy all_contacts
print(s1.all_contacts.search("Radek"))  # [Radek radek@wp.pl]

f1 = Friend("Marcin", "marcin@o2.pl", "456876543")
print(f1)  # Friend Marcin marcin@o2.pl +48456876543
f1.order("herbata")  # herbata zamówiono od Marcin
print(f1.all_contacts)

pprint(f1.all_contacts)
# ['Adam' 'adam@wp.pl',
#  'Radek' 'radek@wp.pl',
#  'Tomek' 'tomek@wp.pl',
#  Marek, marek@o2.pl,
#  Friend Marcin marcin@o2.pl +48456876543]
