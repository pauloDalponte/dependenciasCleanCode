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

3. Execute o comando
   ```bash
   python -m venv venv```
   
5. Em seguida o comando
   ```bash
   venv\Scripts\activate para ativar```
   
7. Em caso de erro, rode o comando
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process```
   
6.instalar as dependencias utilizando PIP
```bash
pip install -r requirements.txt```

9. Para executar a aplicação
 ```bash
 python main.py ```

