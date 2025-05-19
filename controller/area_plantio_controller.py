from connection.connection_db import ConnectionDB
from model.area_plantio_model import AreaPlantioModel

class AreaPlantioController:
    def __init__(self):
        self.areas_plantio = []  # Lista para armazenar objetos AreaPlantioModel, se necessário

    def menu_area_plantio(self):
        """
        Exibe o menu interativo para o usuário e executa as ações escolhidas.
        """
        while True:
            print("\n🚜Menu das Áreas de Plantio:")
            print("1️⃣ Cadastrar Área de Plantio")
            print("2️⃣ Visualizar Áreas de Plantio")
            print("3️⃣ Atualizar Área de Plantio")
            print("4️⃣ Remover Área de Plantio")
            print("0️⃣ Sair")
            
            opcao = input("Escolha uma opção (0-4): ").strip()
            if opcao == '1':
                self.create_area_plantio()
            elif opcao == '2':
                self.get_areas_plantio()
            elif opcao == '3':
                self.update_area_plantio_by_id()
            elif opcao == '4':
                self.delete_area_plantio_by_id()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

    # Método para validar a latitude
    def validate_latitude(self) -> float:
        """
        Solicita e valida a latitude inserida pelo usuário.
        A latitude deve ser um número decimal entre -90 e +90.
        Aceita tanto ponto quanto vírgula como separador decimal.
        """
        while True:
            latitude_str = input("Digite a latitude da área (ex: -23.55 ou -23,55): ")
            # Substitui vírgula por ponto para facilitar a conversão para float
            latitude_str = latitude_str.replace(",", ".")
            try:
                latitude = float(latitude_str)
                if -90 <= latitude <= 90:
                    return latitude
                else:
                    print("Latitude inválida. Deve estar entre -90 e +90.")
            except ValueError:
                print("Entrada inválida. Digite um número decimal para a latitude.")

    # Método para validar a longitude
    def validate_longitude(self) -> float:
        """
        Solicita e valida a longitude inserida pelo usuário.
        A longitude deve ser um número decimal entre -180 e +180.
        Aceita tanto ponto quanto vírgula como separador decimal.
        """
        while True:
            longitude_str = input("Digite a longitude da área (ex: -46.63 ou -46,63): ")
            # Substitui vírgula por ponto para facilitar a conversão para float
            longitude_str = longitude_str.replace(",", ".")
            try:
                longitude = float(longitude_str)
                if -180 <= longitude <= 180:
                    return longitude
                else:
                    print("Longitude inválida. Deve estar entre -180 e +180.")
            except ValueError:
                print("Entrada inválida. Digite um número decimal para a longitude.")

    # Método para criar uma nova área de plantio
    def create_area_plantio(self) -> AreaPlantioModel:
        """
        Cria uma nova área de plantio no banco de dados e retorna um objeto AreaPlantioModel.
        """
        # Cria uma nova conexão com o banco que permite escrita
        connection = ConnectionDB(can_write=True)
        connection.connect_to_oracle()

        print("Informe os detalhes da nova área de plantio:")
        latitude = self.validate_latitude()
        longitude = self.validate_longitude()

        # Verifica se a área de plantio já existe pela latitude e longitude
        if self.area_plantio_existe(connection, latitude, longitude):
            # Solicita os dados da área de plantio ao usuário
            area_total = input("Digite o tamanho total da área em hectáres (formato: 00.00): ")
            descricao_local = input("Digite uma descrição do local da área: ")

            try:
                # Insere a nova área de plantio no banco de dados
                connection.write(f"""
                    INSERT INTO area_plantio (area, latitude, longitude, descricao_local)
                    VALUES ({area_total}, {latitude}, {longitude}, '{descricao_local}')
                    """)
                connection.commit()

                # Recupera a área de plantio recém-inserida para criar o objeto AreaPlantioModel
                df_area = connection.fetch_dataframe(
                    f"SELECT * FROM area_plantio WHERE latitude = {latitude} AND longitude = {longitude}"
                )

                # Verifica se a área foi inserida corretamente no banco de dados
                if not df_area.empty:
                    # Cria e retorna um novo objeto AreaPlantioModel
                    nova_area = AreaPlantioModel(
                        df_area.id_area_plantio.values[0],
                        df_area.area.values[0],
                        df_area.latitude.values[0],
                        df_area.longitude.values[0],
                        df_area.descricao_local.values[0]
                    )
                    print("✅ Área de plantio criada e retornada com sucesso!")
                    return nova_area  # Retorna a nova área de plantio criada
                else:
                    print("⚠️ Erro: Área de plantio não encontrada no banco de dados após inserção.")
                    return None
            except Exception as e:
                print(f"❗️ Erro ao inserir a área de plantio: {e}")
                return None
            finally:
                connection.close_all()  # Garante que a conexão seja fechada
        else:
            print("⚠️ Área de plantio já existe no banco de dados com essas coordenadas.")
            connection.close_all()
            return None

    # Método para verificar se a área de plantio já existe
    def area_plantio_existe(self, connection: ConnectionDB, latitude: float, longitude: float) -> bool:
        """
        Verifica se uma área de plantio já existe no banco de dados com a latitude e longitude fornecidas.
        """
        df_area = connection.fetch_dataframe(
            f"SELECT * FROM area_plantio WHERE latitude = {latitude} AND longitude = {longitude}"
        )
        return df_area.empty  # Retorna True se uma área com essas coordenadas já existir
    
    def get_areas_plantio(self) -> list:
        """
        Recupera todas as áreas de plantio do banco de dados.
        """
        connection = ConnectionDB(can_write=False)
        connection.connect_to_oracle()

        try:
            # Recupera todas as áreas de plantio
            df_areas = connection.fetch_dataframe("SELECT * FROM area_plantio")
            if not df_areas.empty:
                # Cria uma lista de objetos AreaPlantioModel
                self.areas_plantio = [
                    AreaPlantioModel(
                        row.id_area_plantio,
                        row.area,
                        row.latitude,
                        row.longitude,
                        row.descricao_local
                    ) for index, row in df_areas.iterrows()
                ]
                return self.areas_plantio
            else:
                print("⚠️ Nenhuma área de plantio encontrada no banco de dados.")
                return []
        except Exception as e:
            print(f"❗️ Erro ao recuperar áreas de plantio: {e}")
            return []
        finally:
            connection.close_all()  # Garante que a conexão seja fechada

    def get_areas_plantio(self) -> list:
        """
        Recupera os nomes (descrição_local) de todas as áreas de plantio do banco de dados.
        """
        connection = ConnectionDB(can_write=False)
        connection.connect_to_oracle()

        try:
            df_areas = connection.fetch_dataframe("SELECT descricao_local FROM area_plantio")
            if not df_areas.empty:
                nomes_areas = df_areas['descricao_local'].tolist()
                return nomes_areas
            else:
                print("⚠️ Nenhuma área de plantio encontrada no banco de dados.")
                return []
        except Exception as e:
            print(f"❗️ Erro ao recuperar nomes das áreas de plantio: {e}")
            return []
        finally:
            connection.close_all()

    def update_area_plantio(self, id_area_plantio: int) -> AreaPlantioModel:
        """
        Atualiza uma área de plantio existente no banco de dados.
        """
        connection = ConnectionDB(can_write=True)
        connection.connect_to_oracle()

        # Recupera a área de plantio pelo ID
        area_plantio = self.get_area_plantio_by_id(id_area_plantio)
        if area_plantio is None:
            print("⚠️ Área de plantio não encontrada para atualização.")
            return None

        print("Informe os novos detalhes da área de plantio (deixe em branco para manter o valor atual):")
        
        # Solicita novos dados ao usuário, mantendo os valores atuais se deixados em branco
        area_total = input(f"Área total (atual: {area_plantio.get_area()}): ")
        if area_total == "":
            area_total = area_plantio.get_area()
        
        descricao_local = input(f"Descrição do local (atual: {area_plantio.get_descricao_local()}): ")
        if descricao_local == "":
            descricao_local = area_plantio.get_descricao_local()

        try:
            # Atualiza a área de plantio no banco de dados
            connection.write(f"""
                UPDATE area_plantio
                SET area = {area_total}, descricao_local = '{descricao_local}'
                WHERE id_area_plantio = {id_area_plantio}
                """)
            connection.commit()

            # Recupera a área de plantio atualizada
            updated_area = self.get_area_plantio_by_id(id_area_plantio)
            if updated_area:
                print("✅ Área de plantio atualizada com sucesso!")
                return updated_area  # Retorna a área atualizada
            else:
                print("⚠️ Erro: Área de plantio não encontrada após atualização.")
                return None
        except Exception as e:
            print(f"❗️ Erro ao atualizar a área de plantio: {e}")
            return None
        finally:
            connection.close_all()  # Garante que a conexão seja fechada

    def delete_area_plantio_by_id(self, id_area_plantio: int) -> bool:
        """
        Deleta uma área de plantio do banco de dados pelo ID.
        """
        connection = ConnectionDB(can_write=True)
        connection.connect_to_oracle()

        # Verifica se a área de plantio existe
        area_plantio = self.get_area_plantio_by_id(id_area_plantio)
        if area_plantio is None:
            print("⚠️ Área de plantio não encontrada para deleção.")
            return False

        try:
            # Deleta a área de plantio do banco de dados
            connection.write(f"DELETE FROM area_plantio WHERE id_area_plantio = {id_area_plantio}")
            connection.commit()
            print("✅ Área de plantio deletada com sucesso!")
            return True
        except Exception as e:
            print(f"❗️ Erro ao deletar a área de plantio: {e}")
            return False
        finally:
            connection.close_all()  # Garante que a conexão seja fechada

