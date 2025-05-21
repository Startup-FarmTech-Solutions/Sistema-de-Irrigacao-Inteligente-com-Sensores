import threading
import time
from sensor_solo.main import main
from controller.cultura_controller import CulturaController
from controller.area_plantio_controller import AreaPlantioController
from controller.sensor_controller import SensorController

class Menu:
    def __init__(self):
        # Inicia o servidor em uma thread separada
        self.server_thread = threading.Thread(target=main, daemon=True)
        self.server_thread.start()
        # Aguarda alguns segundos para garantir que o servidor suba
        time.sleep(2)

    def display_menu(self):
        """
        Exibe o menu principal e direciona para os menus das controllers.
        """
        while True:
            print("\n🧾 Menu Principal:")
            print("1️⃣ Menu de Culturas")
            print("2️⃣ Menu de Áreas de Plantio")
            print("3️⃣ Menu de Sensores")
            print("0️⃣ Sair")

            opcao = input("Escolha uma opção (0-3): ").strip()
            if opcao == '1':
                CulturaController().menu_cultura()
            elif opcao == '2':
                AreaPlantioController().menu_area_plantio()
            elif opcao == '3':
                SensorController().menu_sensor()
            elif opcao == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
