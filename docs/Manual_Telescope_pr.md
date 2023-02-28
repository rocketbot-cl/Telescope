



# Rocketbot Telescope
  
Module for Rocketbot Telescope  
  
![banner](/imgs/Banner_Telescope.png)

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  

## Como usar este módulo

Para usar este módulo você deve:

1. Criar projeto
2. Gere o modelo
   1. Pegue um ponto de referência.
   2. Selecione os dados que deseja extrair.
   3. Salve o modelo.
   4. Carregue e processe um arquivo.
   5. Verifique os dados extraídos.
3. Salve o token gerado para o modelo
4. Crie um arquivo chamado telescópio.ini contendo:
   [USER]
   user = aaaa@rocketbot.cl
   password = robot1111
   server = http://11.11.1.111/api


## Descrição do comando

### Login Telescope
  
Comando para conectar ao telescópio
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o arquivo .ini|Selecione o arquivo .ini para conectar|C:/Users/User/Desktop/arquivo.ini|

### Carregar documento
  
Carregar documento para obter texto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione o arquivo|Selecione o documento para carregar para obter o texto|C:/Users/User/Desktop/documento.jpg|
|Token de Template|Token de Template no Telescope|RCKU2GKCUP4XB5VW|
|Atribuir a variável|Variável onde o texto obtido será armazenado|var|

### Carregar documentos
  
Carregue vários documentos para obter texto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione a pasta|Selecione a pasta onde estão localizados os documentos a serem carregados|C:/Users/User/Desktop/pasta|
|Template ID|ID de Template no Telescope|RCKU2GKCUP4XB5VW|
|Set to var|Variável onde o conteúdo dos documentos será armazenado|var|

### Consultar estado do resultado
  
Retorna o status de um resultado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Token de resultado|Token de resultado de um processo de extração de texto|4YLXHLLD4IXM621P|
|Atribuir a variável|Variável onde o resultado da consulta será armazenado|var|

### Obter resultado
  
Obter informação de um resultado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Token de resultado|Token de resultado de um processo de extração de texto|RCKU2GKCUP4XB5VW|
|Atribuir resultado a variável|Variável onde o resultado será armazenado||
