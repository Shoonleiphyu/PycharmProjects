class Band:
    """write a class for band with methods add and play"""
    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        return f"{self.band_name} ({', '.join([str(musician) for musician in self.musicians])})"

    def add(self,musicians):
        self.musicians.append(musicians)

    def play(self):
        print(f"{self.band_name}")
        for musician in self.musicians:
            print(musician.play())

