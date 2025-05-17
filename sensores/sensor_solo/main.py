import socket
import json
import random

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do computador (localhost)
PORT = 12345        # Porta para a comunicação
BUFFER_SIZE = 1024

# Banco de dados SQL simulado em Python (dicionário)
database = {
    "leituras": []
}

# Variáveis para armazenar os valores de potássio e fósforo
potassio_atual = 0
fosforo_atual = 0

# Função para adicionar uma leitura ao banco de dados simulado
def adicionar_leitura(leitura):
    database["leituras"].append(leitura)
    print("Leitura adicionada ao banco de dados.")

# Função para recuperar todas as leituras do banco de dados simulado
def obter_leituras():
    return database["leituras"]

# Função para recuperar uma leitura específica por ID (simulado pelo índice)
def obter_leitura_por_id(id):
    if 0 <= id < len(database["leituras"]):
        return database["leituras"][id]
    else:
        return None

# Função para atualizar uma leitura existente (simulado pelo índice)
def atualizar_leitura(id, nova_leitura):
    if 0 <= id < len(database["leituras"]):
        database["leituras"][id] = nova_leitura
        print("Leitura atualizada no banco de dados.")
    else:
        print("ID de leitura inválido.")

# Função para deletar uma leitura (simulado pelo índice)
def deletar_leitura(id):
    if 0 <= id < len(database["leituras"]):
        del database["leituras"][id]
        print("Leitura deletada do banco de dados.")
    else:
        print("ID de leitura inválido.")

# Função para salvar os dados em um arquivo JSON
def salvar_dados_json(dados):
    try:
        with open("dados_sensores.json", 'w') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("Dados salvos em dados_sensores.json")
    except Exception as e:
        print(f"Erro ao salvar dados em JSON: {e}")

# Função principal para receber dados do ESP32 e processá-los
def main():
    global potassio_atual, fosforo_atual
    dados_sensores = []

    # Cria o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Espera por apenas uma conexão

    print(f"Servidor aguardando conexão em {HOST}:{PORT}...")

    try:
        # Aceita a conexão do ESP32
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")

        while True:
            # Recebe os dados do ESP32
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                print("Conexão encerrada pelo cliente.")
                break

            # Decodifica os dados recebidos
            mensagem = data.decode('utf-8').strip()
            print(f"Mensagem recebida: {mensagem}")

            try:
                # Carrega os dados JSON
                leitura = json.loads(mensagem)
                dados_sensores.append(leitura)

                # Adiciona a leitura ao banco de dados simulado
                adicionar_leitura(leitura)

                # Imprime os dados recebidos
                print("\nDados Recebidos do ESP32:")
                print(json.dumps(leitura, indent=4, ensure_ascii=False))

                # Simula o acionamento dos botões de potássio e fósforo
                if leitura['potassio'] == 1:
                    potassio_adicionado = random.uniform(0.1, 0.5)
                    potassio_atual += potassio_adicionado
                    print(f"Potássio adicionado: {potassio_adicionado:.2f} g. Potássio atual: {potassio_atual:.2f} g")

                if leitura['fosforo'] == 1:
                    fosforo_adicionado = random.uniform(0.2, 0.6)
                    fosforo_atual += fosforo_adicionado
                    print(f"Fósforo adicionado: {fosforo_adicionado:.2f} g. Fósforo atual: {fosforo_atual:.2f} g")

                # Demonstração das operações CRUD
                print("\n--- Operações CRUD no Banco de Dados Simulado ---")
                print("Todas as Leituras:", obter_leituras())
                if database["leituras"]:
                    primeira_leitura = obter_leitura_por_id(0)
                    print("Primeira Leitura:", primeira_leitura)
                    
                    # Cria uma nova leitura para atualizar
                    nova_leitura = {
                        "temperatura": 28.5,
                        "umidade": 72.0,
                        "pH": 6.8,
                        "categoria_pH": "Neutro",
                        "potassio": 0,
                        "fosforo": 0,
                        "irrigacao": False
                    }
                    atualizar_leitura(0, nova_leitura)
                    print("Leitura Atualizada:", obter_leitura_por_id(0))
                    
                    deletar_leitura(len(database["leituras"]) -1)
                    print("Leitura Deletada. Leituras Restantes:", obter_leituras())
                else:
                    print("Banco de dados está vazio")

                # Salva os dados em um arquivo JSON
                salvar_dados_json(dados_sensores)
                dados_sensores = []

                # Envia uma resposta de volta para o cliente (ESP32)
                client_socket.send("Dados recebidos com sucesso!".encode('utf-8'))

            except json.JSONDecodeError:
                print(f"Erro ao decodificar JSON: {mensagem}")
                client_socket.send("Erro ao decodificar JSON!".encode('utf-8'))
            except Exception as e:
                print(f"Erro inesperado: {e}")
                client_socket.send(f"Erro no servidor: {e}".encode('utf-8'))

    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
    finally:
        server_socket.close()
        print("Servidor encerrado.")

if __name__ == "__main__":
    main()