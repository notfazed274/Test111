
class Kinda:

    base_url = "https://kindalab.co/"

    def __init__(self, driver):
        self.driver = driver

    def abrir_url(self):
        self.driver.get(Kinda.base_url)