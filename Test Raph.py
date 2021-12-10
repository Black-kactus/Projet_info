class salutation():
    def __init__(self):
        self.hello=1
    def bonjour(self):
        self.hello=2

a=salutation()
print(a.hello)
a.bonjour()
print(a.hello)