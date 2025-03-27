# SOCKET com Python - Infra de Redes

## Diferença dos protocolos TCP/UDP no processo de Socket 

### Protocolo TCP 

- Orientado a conexão, ou seja, necessita de uma conexão client-server antes da transferência de dados, método esse chamado de _Three-Way Handshake_.
- Entrega lenta, mas tem entrega garantida de dados, além de manter a ordem dos dados.
- Mais utilizável para meios de comunicação, como WhatsApp, E-mail, etc.

### Protocolo UDP

- Não necessita de conexão, pois não estabelece um canal de comunicação dedicado antes da transferência de dados.
- Entrega rápida, porém sua entrega de dados não é garantida/confiável, além de não manter a ordem dos dados transferidos.
- Mais utilizável para meios de conexão simples e rápida, como streamings, jogos, etc.
