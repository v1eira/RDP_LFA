# Recursive Descent Parser

#### Autor: Ewerson Vieira Nascimento

#### Ambiente de desenvolvimento:
Programa desenvolvido em Python (3.6.7), utilizando Visual Studio Code (1.33.1) com a extensão para Python da Microsoft.

#### Descriçao dos arquivos:
Os arquivos criados na construção deste trabalho estão dentro da pasta ``RDP`` e são os seguintes:
- [main.py](main.py): arquivo principal, que cria a rotina de inserção de expressões e exibe os resultados.
- [parser.py](parser.py): contém todas as funções necessárias para validar as expressões capturadas na ``main``, são elas:
    - ``is_expr``: verifica se a string de entrada é uma expressão válida.
    - ``is_term``: verifica se a string de entrada é um termo válido.
    - ``is_factor``: verifica se a string de entrada é um fator válido.
    - ``is_base``: verifica se a string de entrada é uma base válida.
    - ``is_number``: verifica se a string de entrada é um número válido.
    - ``is_digit``: verifica se o caracter de entrada é um dígito válido.
    - ``calc``: retorna o resultado das operações (+, -, *, /, // e %) entre dois números.
    - ``verify_parenthesis``: verifica se todos os parênteses que foram abertos na expressão foram fechados.
    - ``filter_expression``: remove espaços em branco e torna a string de entrada minúscula.
- [parser.sh](parser.sh): arquivo que simplesmente executa a ``main``.

#### Executando o programa
Para executar o programa no Ubuntu, abra o terminal, vá até a pasta ``RDP`` e digite o comando ``./parser.sh``.