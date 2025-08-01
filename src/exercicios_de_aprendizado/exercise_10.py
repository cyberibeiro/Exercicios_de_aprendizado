# Gigassegundo - https://exercism.org/tracks/python/exercises/gigasecond

from datetime import datetime, timedelta  # O timedelta que define se vai ser segundos
     #módulo         #classes
class Gigasecond:
    def __init__(self, moment: datetime) -> None: #Aqui diz que o tipo dele é uma data e hora
        self.moment = moment
        #armazeno o moment na variavel de instancia

    def date(self) -> datetime:
        return self.moment + timedelta(seconds=1_000_000_000) #date é um método por estar dentro de uma classe, vai agir sobre um objeto