*Um pipeline de dados com Streamlit para raspar, transformar e visualizar ofertas de notebooks no Mercado Livre.*


🇺🇸 [Read in English](README.md)

---

### 📸 Imagens do Dashboard

![image](https://github.com/user-attachments/assets/c518dd9b-fcfe-4bcb-be2f-583f36853413)

![image](https://github.com/user-attachments/assets/e33d9920-0c28-482b-9d7c-359a7d3a4dbf)


---

## ✨ Funcionalidades

- 🔍 **Spider Scrapy** para coletar listagens de notebooks no Mercado Livre (até 10 páginas).
- 🔧 **Script ETL** para limpar, transformar e armazenar dados no SQLite.
- 📊 **Dashboard Interativo** feito com Streamlit para KPIs e insights visuais.
- 🧼 **Limpeza e Conversão de Tipos** (preço, avaliações etc.).
- 🗃️ **Integração com SQLite** para armazenamento local e análises.

---

## 🏗️ Estrutura do Projeto

```
tielytics/
├── src/
│   ├── scrapy_spider/           # Spider para extração de dados
│   │   └── notebook_spider.py
│   ├── transform/               # Limpeza e transformação de dados
│   │   └── main.py
│   └── dashboard/               # Aplicação com Streamlit
│       └── app.py
├── data/                        # Banco SQLite e arquivos raspados
├── requirements.txt             # Dependências Python
└── README.pt-br.md
```

---

## 🔧 Requisitos

- Python 3.12+
- Scrapy
- Pandas
- Streamlit
- SQLite (já incluso no Python)
- Todas as dependências no `requirements.txt`

---

## 🚀 Instalação

### Instalação Padrão

```bash
# Clone o repositório
git clone https://github.com/seuusuario/MercadoNotebook.git
cd MercadoNotebook

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

---

## 🕷️ Rodar o Spider (Scrapy)

```bash
cd src/scrapy_spider
scrapy runspider notebook_spider.py -o ../../data/data.jsonl
```

---

## 🧹 Rodar o Processo ETL

```bash
cd ../transform
python main.py
```

---

## 📊 Rodar o Dashboard

```bash
cd ../dashboard
streamlit run app.py
```

---

## 🧪 Testes

*Testes automatizados não incluídos, mas podem ser integrados com `pytest`.*
