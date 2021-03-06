class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        return id(self)


if __name__ == "__main__":
    monza = Carro('Monza')
    print(id(monza), monza.acelerar(), Carro.acelerar(monza))
    chevete = Carro('Chevete')
    print(id(chevete), chevete.acelerar(), Carro.acelerar(chevete))
    print(monza.nome)
    print(chevete.nome)
    chevete.nome = 'Chevete'
    print(chevete.nome)
