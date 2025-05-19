from connection.connection_db import ConnectionDB
from model.cultura_model import CulturaModel

class CulturaController:
    def __init__(self):
        self.cultura = []

    def menu_cultura(self):
        """
        Exibe o menu interativo para o usuário e executa as ações escolhidas.
        """
        while True:
            print("\n🌾 Menu das Culturas:")
            print("1️⃣ Cadastrar Cultura")
            print("2️⃣ Visualizar Culturas")
            print("3️⃣ Atualizar Cultura")
            print("4️⃣ Remover Cultura")
            print("0️⃣ Sair")

            opcao = input("Escolha uma opção (0-4): ").strip()
            if opcao == '1':
                self.create_cultura()
            elif opcao == '2':
                connection = ConnectionDB()
                connection.connect_to_oracle()
                try:
                    culturas = self.get_culturas(connection)
                    if culturas:
                        print("\n🌱 Culturas cadastradas:")
                        for cultura in culturas:
                            print(f"- {cultura.nome_cultura}")
                    else:
                        print("⚠️ Nenhuma cultura encontrada.")
                finally:
                    connection.close_all()
            elif opcao == '3':
                self.update_cultura()
            elif opcao == '4':
                self.delete_cultura()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

    def create_cultura(self) -> CulturaModel:
        connection = ConnectionDB(can_write=True)
        connection.connect_to_oracle()

        nome_cultura = input("Digite o nome da cultura: ").lower()

        if self.cultura_exist(connection, nome_cultura):
            try:
                connection.write(f"INSERT INTO cultura (nome_cultura) VALUES ('{nome_cultura}')")
                connection.commit()
                print("✅ Cultura criada com sucesso!")

                df_cultura = connection.fetch_dataframe(
                    f"SELECT id_cultura, nome_cultura FROM cultura WHERE nome_cultura='{nome_cultura}'"
                )

                if not df_cultura.empty:
                    nova_cultura = CulturaModel(
                        id_cultura=df_cultura.id_cultura.values[0],
                        nome=df_cultura.nome_cultura.values[0]
                    )
                    return nova_cultura
                else:
                    print("⚠️ Erro: Cultura não encontrada após inserção.")
                    return None
            except Exception as e:
                print(f"❗️ Erro ao criar cultura: {e}")
                return None
            finally:
                connection.close_all()
        else:
            print("⚠️ Cultura já existe.")
            connection.close_all()
            return None

    def cultura_exist(self, connection: ConnectionDB, nome_cultura: str = None) -> bool:
        df_cultura = connection.fetch_dataframe(f"SELECT nome_cultura FROM cultura WHERE nome_cultura='{nome_cultura}'")
        return df_cultura.empty

    def get_culturas(self, connection: ConnectionDB) -> list:
        """
        Recupera todas as culturas do banco de dados em uma lista ordenada por nome_cultura.
        """
        try:
            query = "SELECT nome_cultura, id_cultura FROM cultura ORDER BY nome_cultura" # Inclui id_cultura na consulta
            print(f"Executando consulta: {query}")
            df_culturas = connection.fetch_dataframe(query)

            print("Resultado da consulta de culturas:")
            print(df_culturas)
            print("Colunas:", df_culturas.columns)

            culturas = []
            if not df_culturas.empty:
                for _, row in df_culturas.iterrows():
                    nome = row.get('nome_cultura') or row.get('NOME_CULTURA')
                    id_cultura = row.get('id_cultura') or row.get('ID_CULTURA') # Recupera id_cultura
                    culturas.append(CulturaModel(id_cultura=id_cultura, nome=nome)) # Passa id_cultura para o model
            else:
                print("⚠️ Nenhuma cultura encontrada.")
                if df_culturas is not None and len(df_culturas) == 0:
                    print("⚠️ A tabela 'cultura' está vazia ou a consulta não retornou resultados.")
                else:
                    print("⚠️ Erro na consulta ou ao recuperar dados da tabela 'cultura'.")
            return culturas

        except Exception as e:
            print(f"Erro ao obter culturas: {e}")
            return []


    def get_cultura_by_id(self, connection: ConnectionDB, id_cultura: int = None) -> CulturaModel:
        df_cultura = connection.fetch_dataframe(f"SELECT * FROM cultura WHERE id_cultura='{id_cultura}'")
        if not df_cultura.empty:
            return CulturaModel(
                id_cultura=df_cultura.id_cultura.values[0],
                nome=df_cultura.nome_cultura.values[0]
            )
        else:
            print("⚠️ Cultura não encontrada.")
            return None

    def update_cultura(self):
        connection = ConnectionDB(can_write=True)
        connection.connect_to_oracle()
        try:
            culturas = self.get_culturas(connection)
            if not culturas:
                print("⚠️ Nenhuma cultura cadastrada para atualizar.")
                return

            print("\nCulturas cadastradas:")
            for cultura in culturas:
                print(f"- {cultura.nome_cultura}")

            nome_atual = input("Digite o nome da cultura que deseja modificar: ").strip().lower()
            if not any(c.nome_cultura == nome_atual for c in culturas):
                print("❗ Cultura não encontrada.")
                return

            novo_nome = input("Digite o novo nome da cultura: ").strip().lower()
            if nome_atual == novo_nome:
                print("⚠️ Novo nome igual ao atual. Nenhuma alteração feita.")
                return

            self.update_cultura_by_nome(connection, nome_atual, novo_nome)
        finally:
            connection.close_all()

    def delete_cultura(self):
        connection = ConnectionDB(can_write=True)
        connection.connect_to_oracle()
        try:
            culturas = self.get_culturas(connection)
            if not culturas:
                print("⚠️ Nenhuma cultura cadastrada para remover.")
                return

            print("\nCulturas cadastradas:")
            for cultura in culturas:
                print(f"- {cultura.nome_cultura}")

            nome = input("Digite o nome da cultura que deseja remover: ").strip().lower()
            if not any(c.nome_cultura == nome for c in culturas):
                print("❗ Cultura não encontrada.")
                return

            self.delete_cultura_by_nome(connection, nome)
        finally:
            connection.close_all()

    # Adicione os métodos update_cultura_by_nome e delete_cultura_by_nome se ainda não tiverem sido implementados.
