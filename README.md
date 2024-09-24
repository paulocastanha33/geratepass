# Gerador de Senhas com PyQt5 - GeratePass

Este projeto é um aplicativo GUI de geração de senhas criado com **Python** e **PyQt5**. O aplicativo permite que o usuário selecione os tipos de caracteres para incluir (maiúsculas, minúsculas, dígitos e símbolos) e o tamanho da senha gerada. Além disso, a senha gerada pode ser copiada para a área de transferência e os campos podem ser limpos com um botão.

## Funcionalidades

- Geração de senha personalizada com opções de:
  - Incluir letras maiúsculas
  - Incluir letras minúsculas
  - Incluir dígitos
  - Incluir símbolos
  - Definir o tamanho da senha
- Copiar a senha gerada para a área de transferência
- Limpar todos os campos e opções
- Fechar o aplicativo via botão

## Pré-requisitos

- Python 3.x
- PyQt5 (Instalar conforme o arquivo `requirements.txt`)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/paulocastanha33/geratepass.git
    ```
   
2. Navegue até o diretório do projeto:
    ```bash
    cd repo-gerador-senhas
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Abra o aplicativo executando o arquivo principal:
    ```bash
    python app.py
    ```

## Interface Gráfica

A interface gráfica foi criada utilizando o **Qt Designer** e carregada via arquivo `.ui`. Para visualizar ou modificar a interface, você pode abrir o arquivo `splash.ui` no Qt Designer.

## Como Usar

1. Defina o tamanho da senha no campo "Tamanho".
2. Selecione as opções de caracteres que deseja incluir (letras maiúsculas, minúsculas, dígitos e/ou símbolos).
3. Clique em "Gerar Senha" para gerar uma senha aleatória.
4. Clique em "Copiar Senha" para copiar a senha gerada para a área de transferência.
5. Para limpar todos os campos e reiniciar as seleções, clique em "Limpar Campos".
6. Para fechar o aplicativo, clique no botão "Sair".

## Dependências

Veja o arquivo `requirements.txt` para as dependências do projeto.

## Contribuições

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests com melhorias ou correções. Sugestões também são bem-vindas!

## Licença

Este projeto é licenciado sob a Licença MIT.
