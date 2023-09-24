from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """set flagfall to 4.5"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initializing variables of silver_service_taxi, adding a new variable fanciness"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of $ {self.flagfall:.2f}"

    def get_fare(self):
        """adding the current fare which inherit from Taxi class with flagfall and generate a total fare"""
        return self.flagfall + super().get_fare()
