# 🔐 LockScore - Verificador de Senhas

[![CI](https://github.com/PalatinoMakaveli/Bootcamp2-LockScore/actions/workflows/ci.yml/badge.svg)](https://github.com/PalatinoMakaveli/Bootcamp2-LockScore/actions/workflows/ci.yml)

---

## - Nome do Projeto:

**LockScore - Verificador de Força de Senhas**

---

## - Descrição do Problema:

A utilização de senhas fracas ou reutilizadas continua sendo uma das principais vulnerabilidades exploradas em ataques cibernéticos.
De acordo com uma reportagem da BBC (2025), ataques recentes demonstraram como criminosos conseguem comprometer contas utilizando técnicas como **credential stuffing** e **ataques de força bruta**, explorando bases de dados vazadas contendo milhões de credenciais.
Referência: https://www.bbc.com/portuguese/articles/c17wknlw75zo

Esses ataques são altamente eficazes porque muitos usuários:
* reutilizam senhas em múltiplos serviços
* utilizam padrões previsíveis (ex: “123456”, “senha123”)
* não adotam boas práticas de complexidade

Ferramentas automatizadas conseguem testar milhares de combinações por segundo, tornando senhas simples vulneráveis em **questão de segundos**.
O problema central não é apenas técnico, mas também comportamental:
usuários não possuem ferramentas acessíveis para avaliar a robustez de suas senhas de forma prática.

---

## - Proposta de Solução:

O LockScore foi desenvolvido como uma ferramenta de apoio à **conscientização em segurança digital**, permitindo que usuários avaliem a força de suas senhas de forma imediata.
A aplicação realiza validações baseadas em critérios amplamente adotados na indústria, fornecendo:
* classificação da senha
* feedback técnico
* estimativa de tempo de quebra
* sugestões de fortalecimento
O objetivo é incentivar a criação de senhas mais seguras e reduzir a exposição a ataques comuns.

---

## - Público-Alvo:
* Usuários finais preocupados com segurança digital
* Estudantes de tecnologia e cibersegurança
* Desenvolvedores iniciantes

---

## - Funcionalidades Principais:
*  Classificação de senha (Fraca, Média, Forte)
*  Barra visual de força (feedback em tempo real)
*  Estimativa de tempo para quebra
*  Sugestões automáticas de melhoria
*  Visualização/ocultação da senha
*  Interface web interativa

---

## - Tecnologias Utilizadas:
* Python 3
* Flask
* HTML5
* CSS3
* Pytest (testes automatizados)
* Ruff (linting e qualidade de código)
* GitHub Actions (Integração Contínua - CI)

---

## - Estrutura do Projeto:

password-checker/
│
├── .github/workflows/ci.yml
├── src/
│   ├── app.py
│   ├── password_checker.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── tests/
│   └── test_password.py
│
├── requirements.txt
├── README.md
├── .gitignore

---

## - Instruções de Instalação:

### 1. Clonar o repositório:

Abra seu Git e digite:
git clone https://github.com/PalatinoMakaveli/Bootcamp2-LockScore.git
cd Bootcamp2-LockScore


---

### 2. Criar ambiente virtual (recomendado)

No seu terminal do VS Code digite:
python -m venv .venv

---

### 3. Ativar o ambiente virtual:

**Windows:**
No seu terminal do VS Code digite:
.venv\Scripts\activate

---

### 4. Instalar dependências:
Após essa etapa, no seu terminal do VS Code digite:
pip install -r requirements.txt

---

## ▶️ Instruções de Execução:

No seu terminal do VS Code digite:
python src/app.py

Acesse no navegador:
http://127.0.0.1:5000
E digite para parar a execução do código: (Ctrl + C)
---

## 🧪 Instruções para Rodar os Testes:
No seu terminal do VS Code digite:
python -m pytest

---

## Instruções para Rodar o Lint:
No seu terminal do VS Code digite:
ruff check .

---

## Critérios de Avaliação da Senha:

A aplicação utiliza uma abordagem baseada em regras, considerando:

* comprimento mínimo (≥ 12 caracteres)
* presença de letras maiúsculas
* presença de letras minúsculas
* presença de números
* presença de caracteres especiais

A pontuação acumulada define a classificação final da senha.

---

## - Integração Contínua (CI):

O projeto utiliza GitHub Actions para:
* execução automática de testes
* verificação de qualidade de código
* validação em ambiente limpo

---

## - Versão Atual:
**v1.0.0**

---

## 👨‍💻 Autor

**Gustavo Augusto D. Braga**

---

## Link do Repositório Público:
https://github.com/PalatinoMakaveli/Bootcamp2-LockScore

---

## 📄 Licença

Este projeto está sob a licença MIT.

---
