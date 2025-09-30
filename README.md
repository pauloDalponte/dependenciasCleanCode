# 📦 Sistema de Gerenciamento de Usuários

Este projeto é uma refatoração de um sistema simples de gerenciamento de usuários. As mudanças visam melhorar a organização, reduzir dependências e aumentar a testabilidade.

## ✅ Mudanças realizadas

- Separação em módulos (`models`, `services`, `repositories`, `utils`);
- Substituição de escrita de logs manual por `loguru`;
- Remoção de variáveis globais;
- Uso de `pip` como gerenciador de pacotes;
- Código orientado a objetos e mais testável;
- Nova estrutura de pastas.

## 🚀 Como executar

1. Baixe ou clone o repositório:

2. Navegue até a pasta que se encontra o projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Execute o comando para criar o ambiente virtual
   ```bash
   python -m venv venv
   ```
   
5. Em seguida o comando para ativar o ambiente virtual
   ```bash
   venv\Scripts\activate
   ```
   
6. Em caso de erro, rode o comando
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```
   
7.instalar as dependencias utilizando PIP
   ```bash
   pip install -r requirements.txt
   ```

8. Para executar a aplicação
 ```bash
 python main.py ```

