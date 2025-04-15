# 📦 Controle de Estoque – Daluz Sushi

Sistema web desenvolvido como projeto de extensão universitária, com o objetivo de organizar o controle de estoque do restaurante **Daluz Sushi**, localizado em Itajaí/SC.

## 🎯 Funcionalidades

- Cadastro e visualização por categoria (Sushi, Bebidas, Cozinha, Gerais)
- Registro de entrada e saída de produtos
- Alerta de itens abaixo do estoque mínimo
- Exportação de itens mínimos para Excel
- Interface web simples e acessível via navegador

## 🛠 Tecnologias utilizadas

- Python 3.10
- Flask
- SQLite
- Bootstrap 5
- Pandas / Openpyxl
- Fly.io (deploy online)
- Visual Studio Code

## 🚀 Como rodar localmente

```bash
# Clone o projeto
git clone https://github.com/FabioMelo10/controle_estoque_daluzsushi.git

# Acesse a pasta
cd controle_estoque_daluzsushi

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode o sistema
python app.py
```

Acesse em: `http://127.0.0.1:5000`

## ☁️ Sistema online

O sistema também está disponível via navegador, hospedado gratuitamente em nuvem:

🔗 [https://daluzsushi.fly.dev](https://daluzsushi.fly.dev)

## 👨‍🍳 Sobre o projeto

Este projeto foi desenvolvido em parceria com o restaurante **Daluz Sushi**, como ação extensionista aplicada à disciplina de desenvolvimento de sistemas. A proposta nasceu de uma necessidade real do parceiro em organizar seus processos internos com o uso de tecnologia acessível e gratuita.
