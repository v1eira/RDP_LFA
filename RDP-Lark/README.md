# Parser para a linguagem MEL utilizando ferramenta

#### Autor: Ewerson Vieira Nascimento

#### Ambiente de desenvolvimento:
Programa desenvolvido em Python (3.6.7), utilizando a biblioteca [Lark](https://github.com/lark-parser/lark) e Visual Studio Code (1.33.1) com a extensão para Python da Microsoft.

#### Descriçao dos arquivos:
Os arquivos criados na construção deste trabalho estão dentro da pasta ``RDP-Lark`` e são os seguintes:
- [main.py](main.py): arquivo principal, que cria a rotina de inserção de expressões e mostra se a expressão entrada é válida ou não.
- [parser.py](parser.py): contém importação do Lark, a gramática da linguagem MEL e a função ``parser_result``, que retorna ``True`` se a expressão for válida e ``False`` caso contrário.
- [parser.sh](parser.sh): arquivo que simplesmente executa a ``main``.

#### Instalando o Lark:
Para poder instalar o Lark, primeiro precisamos instalar o [Pip](https://pypi.org/project/pip/).

1. Começamos atualizando a lista de pacotes:

    ``$ sudo apt update``

2. Como estamos utilizando o Python 3, instalaremos o Pip com o seguinte comando:

    ``$ sudo apt install python3-pip``

3. Para verificar se o Pip foi instalado corretamente, fazemos:

    ``$ pip3 --version``

    Teremos como retorno algo similar a:

    ``pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)``

4. Agora, para instalar o Lark, basta fazer:

    ``$ pip3 install lark-parser``

#### Executando o programa
Para executar o programa no Ubuntu, abra o terminal, vá até a pasta ``RDP-Lark`` e digite o comando ``./parser.sh``.