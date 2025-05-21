import oracledb
from pandas import DataFrame
from pydantic import BaseModel
from datetime import date, datetime
from connection.connection_db import ConnectionDB
from controller.area_plantio_controller import AreaPlantioController
from controller.cultura_controller import CulturaController
from controller.sensor_controller import SensorController
from typing import List, Optional, Any # Importe List do módulo typing
import json
import random # Importa o módulo random

from model.leitura_sensor_model import LeituraSensorModel # Importe o módulo json


# Se você quer que carregar_dados_json seja um método da classe LeituraSensorController:
class LeituraSensorController:
    def __init__(self, db: ConnectionDB, conn_name: str = "ATV_FIAP"):
        self.db = db
        self.conn_name = conn_name
        self.conn = db.connect_to_oracle()
        self.potassio_atual = 0.0  # Inicializa potassio_atual
        self.fosforo_atual = 0.0    # Inicializa fosforo_atual

    def menu_leitura(self, conn):
        """
        Exibe um menu interativo para o usuário relacionado à leitura de sensores e executa a ação escolhida.
        Parâmetros:
            conn: Objeto de conexão com o banco de dados utilizado para consultar leituras de sensores.
        Fluxo:
            - Permite ao usuário inserir uma nova leitura de sensor.
            - Permite visualizar leituras de sensores já cadastradas.
            - Permite sair do menu.
        O menu permanece ativo até que o usuário escolha a opção de sair.
        Exibe o menu interativo para o usuário e executa as ações escolhidas.
        """
        while True:
            print("\n📊 Menu de Leitura de Sensores:")
            print("1️⃣ Inserir Leitura de Sensor")
            print("2️⃣ Visualizar Leituras de Sensor")
            print("0️⃣ Sair")

            opcao = input("Escolha uma opção (0-2): ").strip()
            if opcao == '1':
                self.processar_e_inserir_dados()  # Inserir leitura do sensor
            elif opcao == '2':
                leituras = self.get_leituras_por_criterio(conn) # Consulta as leituras do sensor
                if leituras:
                    print("\n📋 Leituras de Sensor:")
                    for leitura in leituras:
                        print(leitura)
                else:
                    print("⚠️ Nenhuma leitura de sensor encontrada.")
            elif opcao == '0':
                print("Saindo do menu de leitura...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

    def inserir_leitura_sensor(self, leitura: LeituraSensorModel):
        """
        Insere uma nova leitura de sensor no banco de dados.

        Args:
            leitura (LeituraSensorModel): Objeto contendo os dados da leitura do sensor a ser inserida.

        O método executa um comando INSERT na tabela 'leitura_sensor' com os valores fornecidos pelo objeto 'leitura'.
        Caso a inserção seja bem-sucedida, uma mensagem de sucesso é exibida. Caso contrário, uma mensagem de erro é exibida.
        """

        query = """
            INSERT INTO leitura_sensor (id_sensor, id_area_plantio, data_hora, temperatura, umidade, leitura_ldr, ph, potassio, fosforo, irrigacao)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)
            """
        cursor = self.db.get_cursor(self.conn_name)
        if cursor:
            cursor.execute(
                query,
                (
                    leitura.get_id_sensor(),
                    leitura.get_id_area_plantio(),
                    leitura.get_data_hora(),
                    leitura.get_temperatura(),
                    leitura.get_umidade(),
                    leitura.get_leitura_ldr(),
                    leitura.get_ph(),
                    leitura.get_potassio(),
                    leitura.get_fosforo(),
                    leitura.get_irrigacao(), # Já é '0' ou '1'
                ),
            )
            self.db.commit(self.conn_name)
            print("Leitura do sensor inserida com sucesso.")
        else:
            print("Erro ao obter o cursor.")

    def get_leituras_por_criterio(self, connection: ConnectionDB, where_clause: str = None) -> list[LeituraSensorModel]:
        """
        Recupera leituras de sensor do banco de dados com base em uma cláusula WHERE opcional.

        Args:
            connection (ConnectionDB): A conexão com o banco de dados.
            where_clause (str, optional): Uma string representando a cláusula WHERE da query SQL.
                                        Exemplo: "WHERE id_sensor = 25". Defaults to None.

        Returns:
            list[LeituraSensorModel]: Uma lista de objetos LeituraSensorModel encontrados.
        """
        leituras = []
        try:
            query = "SELECT ID_LEITURA, ID_SENSOR, ID_AREA_PLANTIO, DATA_HORA, TEMPERATURA, UMIDADE, LEITURA_LDR, PH, POTASSIO, FOSFORO, IRRIGACAO FROM leitura_sensor"
            if where_clause:
                query += f" {where_clause}"
            query += " ORDER BY DATA_HORA DESC"  # Ordena por data e hora, opcional

            print(f"Executando consulta: {query}")
            df_leituras = connection.fetch_dataframe(query)

            print("Resultado da consulta de leituras:")
            print(df_leituras)
            print("Colunas:", df_leituras.columns)

            if not df_leituras.empty:
                for _, row in df_leituras.iterrows():
                    leitura_data = {
                        "id_leitura_sensor": int(row["ID_LEITURA"]),
                        "id_sensor": int(row["ID_SENSOR"]),
                        "id_area_plantio": int(row["ID_AREA_PLANTIO"]),
                        "data_hora": str(row["DATA_HORA"]),
                        "temperatura": float(row["TEMPERATURA"]),
                        "umidade": float(row["UMIDADE"]),
                        "leitura_ldr": int(row["LEITURA_LDR"]),
                        "ph": float(row["PH"]),
                        "potassio": float(row["POTASSIO"]),
                        "fosforo": float(row["FOSFORO"]),
                        "irrigacao": str(row["IRRIGACAO"]),
                    }
                    leitura = LeituraSensorModel(**leitura_data)
                    leituras.append(leitura)
            else:
                print("⚠️ Nenhuma leitura de sensor encontrada com os critérios fornecidos.")

            return leituras

        except Exception as e:
            print(f"Erro ao obter leituras de sensor: {e}")
            return []

    def carregar_dados_json(self, nome_arquivo="data/console_print.json") -> List[dict]:
        """Carrega os dados do arquivo JSON."""
        try:
            with open(nome_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
            print(f"Dados carregados do arquivo '{nome_arquivo}'.")
            return dados
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON do arquivo '{nome_arquivo}'. Verifique se o arquivo está formatado corretamente.")
            return []
        except Exception as e:
            print(f"Erro inesperado ao carregar o arquivo '{nome_arquivo}': {e}")
            return []

    def processar_e_inserir_dados(self, nome_arquivo="data/console_print.json"):
        """
        Processa dados de sensores a partir de um arquivo JSON e insere leituras no banco de dados.
        Este método carrega dados de sensores de um arquivo JSON especificado, processa cada entrada,
        atualiza os valores acumulados de potássio e fósforo, converte e valida os dados recebidos,
        e insere novas leituras no banco de dados caso ainda não existam. Caso o arquivo contenha
        um único dicionário, ele é encapsulado em uma lista para processamento uniforme.
        Parâmetros:
            nome_arquivo (str): Caminho para o arquivo JSON contendo os dados dos sensores.
                                O padrão é "data/console_print.json".
        Fluxo:
            - Carrega os dados do arquivo JSON.
            - Recupera os últimos IDs de sensor e área de plantio do banco de dados.
            - Para cada item nos dados:
                - Atualiza os valores de potássio e fósforo conforme flags presentes.
                - Converte o campo de irrigação para o formato esperado.
                - Cria uma instância de LeituraSensorModel com os dados processados.
                - Verifica se a leitura já existe; se não, insere no banco de dados.
        Observações:
            - Caso não haja dados ou os IDs não possam ser recuperados, o método imprime uma mensagem e retorna.
            - O método utiliza valores aleatórios para simular a adição de potássio e fósforo.
            - Apenas leituras únicas são inseridas, evitando duplicidade.
        Exceções:
            - Imprime mensagens de erro caso o formato do JSON seja inválido ou dados essenciais estejam ausentes.
        Retorno:
            None
        """
        dados_json = self.carregar_dados_json(nome_arquivo)
        if not dados_json:
            print("Nenhum dado para processar.")
            return

        ultimo_id_sensor = self.get_ultimo_id("sensor", "id_sensor")
        ultimo_id_area_plantio = self.get_ultimo_id("area_plantio", "id_area_plantio")

        if ultimo_id_sensor is None or ultimo_id_area_plantio is None:
            print("Erro ao recuperar último id_sensor ou id_area_plantio. Verifique se as tabelas estão populadas.")
            return

        print(f"Ultimo ID Sensor: {ultimo_id_sensor}, Ultimo ID Area Plantio: {ultimo_id_area_plantio}")

        # Se o arquivo contém um único dicionário, encapsule em uma lista para processamento uniforme
        if isinstance(dados_json, dict):
            dados_list = [dados_json]
        elif isinstance(dados_json, list):
            dados_list = dados_json
        else:
            print("Formato de dados JSON inválido.")
            return

        for item in dados_list:
            potassio_bool = bool(item.get('potassio', False))
            fosforo_bool = bool(item.get('fosforo', False))

            potassio_adicionado = random.uniform(0.1, 0.5) if potassio_bool else 0.0
            fosforo_adicionado = random.uniform(0.2, 0.6) if fosforo_bool else 0.0

            self.potassio_atual += potassio_adicionado
            self.fosforo_atual += fosforo_adicionado

            data_hora_obj = datetime.now().date()

            irrigacao_str = str(item.get("irrigacao", "")).strip().upper()
            irrigacao_char = '1' if irrigacao_str in ['TRUE', '1', 'LIGADO', 'ATIVA', 'ATIVO'] else '0'

            leitura = LeituraSensorModel(
                id_sensor=ultimo_id_sensor,
                id_area_plantio=ultimo_id_area_plantio,
                temperatura=item.get("temperatura", 0.0),
                umidade=item.get("umidade", 0.0),
                leitura_ldr=item.get("leitura_ldr", 0),
                ph=item.get("ph", 0.0),
                potassio=self.potassio_atual,
                fosforo=self.fosforo_atual,
                irrigacao=irrigacao_char,
                data_hora=data_hora_obj
            )

            if not self.leitura_ja_existe(leitura):
                self.inserir_leitura_sensor(leitura)
                print(f"Potassio atual: {self.potassio_atual}, Fosforo atual: {self.fosforo_atual}")
            else:
                print(f"Leitura já existe: {leitura}. Ignorando inserção.")

    def leitura_ja_existe(self, leitura: LeituraSensorModel) -> bool:
        """
        Verifica se uma leitura de sensor já existe no banco de dados.

        Esta função executa uma consulta SQL para verificar se já existe um registro na tabela
        'leitura_sensor' com os mesmos valores de id_sensor, id_area_plantio, data_hora, temperatura,
        umidade, leitura_ldr, ph, potassio, fosforo e irrigacao fornecidos pelo objeto LeituraSensorModel.

        Args:
            leitura (LeituraSensorModel): Objeto contendo os dados da leitura do sensor a ser verificada.

        Returns:
            bool: True se a leitura já existe no banco de dados, False caso contrário.
        """
        
        # Verifica se a leitura já existe no banco de dados
        query = """
            SELECT 1 FROM leitura_sensor
            WHERE id_sensor = :1 AND id_area_plantio = :2 AND data_hora = :3 AND temperatura = :4
            AND umidade = :5 AND leitura_ldr = :6 AND ph = :7 AND potassio = :8 AND fosforo = :9 AND irrigacao = :10
            """
        cursor = self.db.get_cursor(self.conn_name)
        if cursor:
            cursor.execute(
                query,
                (
                    leitura.get_id_sensor(),
                    leitura.get_id_area_plantio(),
                    leitura.get_data_hora(),
                    leitura.get_temperatura(),
                    leitura.get_umidade(),
                    leitura.get_leitura_ldr(),
                    leitura.get_ph(),
                    leitura.get_potassio(),
                    leitura.get_fosforo(),
                    leitura.get_irrigacao(), # Também deve ser '0' ou '1'
                ),
            )
            return cursor.fetchone() is not None
        return False
    
    def get_ultimo_id(self, tabela: str, coluna_id: str) -> Optional[int]:
        """
        Recupera o último valor de ID de uma tabela.

        Args:
            tabela (str): Nome da tabela.
            coluna_id (str): Nome da coluna que representa o ID.

        Returns:
            Optional[int]: O último ID, ou None em caso de erro ou tabela vazia.
        """
        query = f"SELECT MAX({coluna_id}) FROM {tabela}"
        cursor = self.db.get_cursor(self.conn_name)
        if cursor:
            cursor.execute(query)
            resultado = cursor.fetchone()
            if resultado and resultado[0] is not None:
                return int(resultado[0])
            else:
                return None  # Tabela vazia
        return None
