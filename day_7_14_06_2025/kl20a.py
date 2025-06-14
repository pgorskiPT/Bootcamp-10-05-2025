class NotFound(Exception):
    def __init__(self, resource, resource_id):
        msg = f"{resource} o ID {resource_id} nie znaleziono"
        super().__init__(msg)
        self.resource = resource
        self.resource_id = resource_id

    @classmethod
    def user(cls, user_id):
        return cls("Użytkownik", user_id)

    @staticmethod
    def for_any(resource, resource_id):
        return NotFound(resource, resource_id)


# raise NotFound.user(7)
# # Traceback (most recent call last):
# #   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_7_14_06_2025/kl20a.py", line 17, in <module>
# #     raise NotFound.user(7)
# # NotFound: Użytkownik o ID 7 nie znaleziono

raise NotFound.for_any("Dokument", 45)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_7_14_06_2025/kl20a.py", line 23, in <module>
#     raise NotFound.for_any("Dokument", 45)
# NotFound: Dokument o ID 45 nie znaleziono
