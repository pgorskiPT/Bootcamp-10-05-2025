class MyClass:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter


print(MyClass.increment_counter())
print(MyClass.increment_counter())
print(MyClass.increment_counter())
c = MyClass()
print(c.counter)  # 3
print(c.increment_counter())  # 4
c.counter = 0  # nadpiszemy
print(c.counter)  # 0
c.increment_counter()
print(c.counter)
print(MyClass.counter)  # 5

c2 = MyClass()
print(c2.increment_counter())  # 6
