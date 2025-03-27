from socket import *
import sys

serverName = 'localhost' 
serverPort = 12000

try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    while True:
        try:
            message = input("Digite sua mensagem (ou 'sair' para terminar): ")
            if message.lower() == 'sair':
                break
                
            clientSocket.sendto(message.encode(), (serverName, serverPort))
        
            clientSocket.settimeout(5.0) 
            
            try:
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                print("Resposta do servidor:", modifiedMessage.decode())
            except timeout:
                print("Servidor não respondeu dentro do tempo esperado")
            except ConnectionResetError:
                print("Erro: Conexão foi resetada pelo servidor")
                
        except KeyboardInterrupt:
            print("\nCliente encerrado pelo usuário")
            break
            
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    clientSocket.close()
    sys.exit(0)
