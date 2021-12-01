from Pages.Kindalab_homepage import Kinda


class Test_config:

    def test_abrir_url(self, browser):
        k = Kinda(browser)
        k.abrir_url()
        assert k.ver_titulo() == 'WE ARE\n DEVELOPERS'
        print(k.ver_titulo())

