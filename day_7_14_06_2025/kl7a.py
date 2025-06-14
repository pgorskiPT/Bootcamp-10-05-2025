class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_document(self):
        print("Skanowanie dokumentu")
        return "Zawartość dokumentu"


# mixin
class MultifunctionalDevice(Printer, Scanner):

    def photocopy(self):
        content = self.scan_document()
        self.print_message(content)


device = MultifunctionalDevice()
device.photocopy()
# Skanowanie dokumentu
# Drukowanie wiadomości Zawartość dokumentu

device.print_message("Komunikat")  # Drukowanie wiadomości Komunikat

message = device.scan_document()
print("Odczytany komunikat:", message)  # Odczytany komunikat: Zawartość dokumentu

print(MultifunctionalDevice.__mro__)
# (<class '__main__.MultifunctionalDevice'>, <class '__main__.Printer'>, <class '__main__.Scanner'>, <class 'object'>)
