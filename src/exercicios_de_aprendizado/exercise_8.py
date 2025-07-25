class SpaceAge:
    EARTH_YEAR_SECONDS = 31_557_600

    ORBITAL_PERIODS = {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    def on_planet(self, planet: str) -> float:
        if planet not in self.ORBITAL_PERIODS:
            raise ValueError(
                f"Planeta '{planet}' não encontrado. Por favor, use um dos seguintes: {', '.join(self.ORBITAL_PERIODS.keys())}"
            )
        period = self.ORBITAL_PERIODS[planet]
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * period), 2)