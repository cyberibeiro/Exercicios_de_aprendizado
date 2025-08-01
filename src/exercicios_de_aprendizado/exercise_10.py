# Gigassegundo - https://exercism.org/tracks/python/exercises/gigasecond

from datetime import datetime, timedelta

class Gigasecond:
    def __init__(self, moment: datetime) -> None:
        """
        Inicializa o objeto com um momento no tempo.

        Args:
            moment (datetime): Data e hora inicial a partir da qual o cálculo será feito.
        """
        self.moment = moment


    def date(self) -> datetime:
        """
        Retorna a data e hora após adicionar 1 gigassegundo (1.000.000.000 segundos) ao momento inicial.

        Returns:
            datetime: Nova data e hora após a soma
        """
        return self.moment + timedelta(seconds=1_000_000_000)