class Persona:
    def __init__(self: object) -> None:
        self.name = 'asdw'
        self.age = '12345'

    def __str__(self) -> str:
        return f'{self.name}: {self.age}'


s = Persona()
if s:
    print(s)
