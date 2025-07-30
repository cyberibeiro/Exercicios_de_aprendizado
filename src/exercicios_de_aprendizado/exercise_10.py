# Gigassegundo - https://exercism.org/tracks/python/exercises/gigasecond

from datetime import datetime, timedelta  # O timedelta que define se vai ser segundos
     #módulo         #classes
class Gigasecond:
    def __init__(self, moment: datetime) -> None: #Aqui diz que o tipo dele é uma data e hora
        self.moment = moment

    def date(self) -> datetime:
        return self.moment + timedelta(seconds=1_000_000_000)
