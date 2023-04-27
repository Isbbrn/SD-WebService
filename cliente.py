import requests

def main():
    # URL do servidor
    url = "http://localhost:5000/message"

    # Mensagem para enviar
    continuar = True
    while continuar: 
        message = str(input(">>"))
        if message == "":
            continuar = False
            break
        data = {"message": message}     # Dados da mensagem em formato JSON

        # Faz a requisição HTTP POST com a mensagem em formato JSON
        response = requests.post(url, json=data)

        # Verifica se a requisição foi bem sucedida (status code 200)
        if response.status_code == 200:
            # Exibe a mensagem de resposta do assistente virtual
            print(response.json()["message"])
        else:
            print("Erro ao enviar mensagem. Status code:", response.status_code)

if __name__ == '__main__':
    main()
