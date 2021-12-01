from selenium.webdriver.common.by import By

class Kinda:

    base_url = "https://kindalab.co/"
    titulo = (By.CLASS_NAME, 'title')

    def __init__(self, driver):
        self.driver = driver

    def abrir_url(self):
        self.driver.get(Kinda.base_url)

    def ver_titulo(self):
        titulo = self.driver.find_element(*self.titulo)
        return titulo.text
