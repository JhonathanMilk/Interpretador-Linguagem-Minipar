# Interpretador MiniPar

Projeto desenvolvido para a disciplina de Compiladores <p>
**Aluno:** Jonatan Leite Alves

# Instalação de dependências
É obrigatório ter o [Python](https://www.python.org/) instalado.<p>
Deve-se instalar a biblioteca [Ply](https://www.dabeaz.com/ply/ply.html). Comando para instalação:
```sh
pip install ply
```
# Instalação do MiniPar e execução de programas

Antes de tudo, faça o download do [interpretador MiniPar](https://github.com/JhonathanMilk/Interpretador-Linguagem-Minipar/archive/refs/heads/main.zip) para o seu computador, extraia o ZIP na pasta de sua preferência e, em seguida, siga uma das maneiras descritas abaixo para executar programas com o interpretador MiniPar.
### Maneira 1
Abra o terminal, navegue até a pasta do projeto e digite o seguinte comando:
```sh
<Versão_Python> main.py <nome_do_programa.mp>
```
***Exemplo:***
```sh
python3 main.py program2.mp
```
O programa a ser executado deve estar obrigatoriamente na pasta do projeto. Caso contrário, especifique o caminho completo até o programa (*não se esqueça da extensão .mp*).
### Maneira 2
***Passo 1:*** Na pasta do projeto, há um arquivo chamado `minipar`. Abra este arquivo em um editor de texto e substitua a parte da linha que contém o endereço até o arquivo `main.py` (```/home/jhonathanmilk/interpretador-minipar/main.py```), pelo endereço do `main.py` do projeto no seu computador.

***Exemplo:***
suponha que o endereço para o arquivo `main.py` no seu computador seja:
```
/home/usuario/downloads/interpretador-linguagem-minipar/main.py
```
Então, o arquivo minipar ficará assim:
```sh
#!/bin/bash
python3 /home/usuario/downloads/interpretador-linguagem-minipar/main.py "$@"
```
Salve as alterações feitas. <p> 
***Passo 2:*** Abra o terminal e navegue até a pasta do interpretador MiniPar. Agora, você deve atualizar temporariamente a variável de ambiente PATH para incluir o diretório atual (.). Para fazer isso, use o seguinte comando:
```sh
export PATH=$PATH:.
```
***Passo 3:*** Agora, você pode executar os programas MiniPar (apenas nesta sessão do terminal) com o seguinte comando:
```sh
minipar <nome_do_programa.mp>
```
***Exemplo***:
```sh
minipar program2.mp
```
Lembre-se de que essas configurações não são permanentes e, ao fechar o terminal, elas não funcionarão mais, logo você precisará refazer o processo. No entanto, você pode usar a Maneira 3 a seguir para aplicar as configurações permanentemente e poder executar os programas minipar em qualquer diretório usando o comando `minipar`.
### Maneira 3
***Passo 1:*** Execute o Passo 1 realizado na Maneira 2. <p>
***Passo 2:*** Adicione o diretório onde está o arquivo `minipar` ao PATH. Para fazer isso, edite o arquivo `.bashrc` (script de inicialização do shell Bash que configura o ambiente do terminal) usando qualquer editor de texto. Neste exemplo, usaremos o nano. Então no terminal execute o seguinte comando:
```nano ~/.bashrc
```
Vá até a última linha do arquivo bashrc e adicione o caminho até o diretório onde está o arquivo `minipar`:
```sh
export PATH=/seu/endereco/aqui:$PATH
```
###### *obs.: voce pode ter o arquivo minipar em qualquer diretório, até mesmo fora da pasta do projeto* <p>
***Exemplo***
```sh
export PATH=/home/usuario/downloads/interpretador-linguagem-minipar:$PATH
```
Salve as alterações no arquivo e saia do editor. No caso do nano, pressione `Ctrl+O` para salvar, `Enter` para confirmar e, em seguida, `Ctrl+X` para sair. <p>
***Passo 3:*** Reinicie o terminal (feche e abra novamente). O comando minipar deve ser reconhecido no terminal. Para testar, digite no terminal `which minipar` e este comando retornará o endereço completo até o interpretador MiniPar
***Passo 4:*** Execute os programas.mp em qualquer diretório apenas executando o comando:
```sh
minipar <nome_do_programa.mp>
```
***Exemplo:***
```sh
minipar program2.mp
```
