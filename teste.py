import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By


class testSelenium:
    url = 'https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do'

    def __init__(self) -> None:  # inicializar o projeto
        pass

    def iniciar(self):
        try:
            self.carregarDrivers()
            self.iniciaAba(self.url)
        except Exception as error:
            print(error)
        finally:
            self.navegador.close()

    def carregarDrivers(self) -> None:  # carregar definições de drivers
        options = ChromeOptions()
        path_chromedriver = ':\\Users\\pedro\\Downloads\\' + \
                            'chromedriver_win32\\chromedriver.exe'

        # options.add_argument(
        #     f'user-data-dir={self.inicializacao.config["diretorio_user_data"]}')
        # options.add_experimental_option("prefs", prefs)

        self.navegador = Chrome(
            options=options, executable_path=f"{path_chromedriver}")

        self.timer = WebDriverWait(self.navegador, 10)

    def iniciaAba(self, url):
        time.sleep(1)
        self.navegador.get(url)
        self.navegador.maximize_window()


testSelenium().iniciar()
