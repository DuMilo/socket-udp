from socket import *

serverName = '192.168.56.1'  
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence: ')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(2048)

print('From Server:', modifiedSentence.decode())

clientSocket.close()