# LockScore 🔐

Sistema web desenvolvido em Flask para análise de força de senhas e verificação de credenciais comprometidas através de integração com API pública.

[![CI](https://github.com/PalatinoMakaveli/Bootcamp2-LockScore/actions/workflows/ci.yml/badge.svg)](https://github.com/PalatinoMakaveli/Bootcamp2-LockScore/actions/workflows/ci.yml)

---

# 🌐 Aplicação Online

https://lockscore.onrender.com/

---

# Sobre o Projeto

O LockScore foi desenvolvido como uma ferramenta de apoio à conscientização em segurança digital, permitindo que usuários avaliem a força de suas senhas e verifiquem possíveis comprometimentos de credenciais através de integração com API pública.

O projeto foi desenvolvido durante a Etapa Intermediária do Bootcamp 2, aplicando conceitos de:

- Git Flow
- GitHub Issues
- Integração com APIs REST
- Testes automatizados
- CI/CD
- Deploy em nuvem

---

# Descrição do Problema

A utilização de senhas fracas ou reutilizadas continua sendo uma das principais vulnerabilidades exploradas em ataques cibernéticos.

De acordo com uma reportagem da BBC (2025), ataques recentes demonstraram como criminosos conseguem comprometer contas utilizando técnicas como credential stuffing e ataques de força bruta, explorando bases de dados vazadas contendo milhões de credenciais.

Referência:
https://www.bbc.com/portuguese/articles/c17wknlw75zo

Esses ataques são altamente eficazes porque muitos usuários:

- reutilizam senhas em múltiplos serviços
- utilizam padrões previsíveis (ex: “123456”, “senha123”)
- não adotam boas práticas de complexidade

Ferramentas automatizadas conseguem testar milhares de combinações por segundo, tornando senhas simples vulneráveis em questão de segundos.

O problema central não é apenas técnico, mas também comportamental:
usuários não possuem ferramentas acessíveis para avaliar a robustez de suas senhas de forma prática.

---

# Proposta de Solução

O LockScore foi desenvolvido como uma ferramenta de apoio à conscientização em segurança digital, permitindo que usuários avaliem a força de suas senhas de forma imediata.

A aplicação realiza validações baseadas em critérios amplamente adotados na indústria, fornecendo:

- classificação da senha
- feedback técnico
- estimativa de tempo de quebra
- sugestões de fortalecimento
- verificação de possíveis credenciais comprometidas

O objetivo é incentivar a criação de senhas mais seguras e reduzir a exposição a ataques comuns.

---

# Público-Alvo

- Usuários finais preocupados com segurança digital
- Estudantes de tecnologia e cibersegurança
- Desenvolvedores iniciantes

---

# Funcionalidades Principais

- Classificação de senha (Fraca, Média, Forte)
- Barra visual de força
- Estimativa de tempo para quebra
- Sugestões automáticas de melhoria
- Visualização/ocultação da senha
- Interface web interativa
- Integração com API pública
- Verificação de credenciais comprometidas

---

# 🌐 Integração com API Pública

A aplicação utiliza integração com API pública para verificar possíveis vazamentos de credenciais.

API utilizada:

- Hudson Rock API

A integração é realizada através de requisições HTTP utilizando a biblioteca `requests`.

---

# 🧪 Teste de Integração

Foi implementado teste automatizado para validar:

- comunicação com API externa
- resposta da API
- fluxo de dados da aplicação
- estabilidade da integração

Ferramentas utilizadas:

- Pytest
- Mock

---

# 🌳 Estratégia de Branching

Durante o desenvolvimento da Etapa Intermediária foram utilizadas boas práticas de versionamento:

- criação de Issue no GitHub
- desenvolvimento em branch separada
- Pull Request para merge
- resolução da Issue vinculada ao PR

Branch utilizada:

```text
entrega-intermediaria
```

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- Requests
- Pytest
- Ruff
- Gunicorn
- GitHub Actions
- Render

---

# 📂 Estrutura do Projeto

```text
Bootcamp2-LockScore/
│
├── src/
│   ├── app.py
│   ├── password_checker.py
│   ├── services/
│   │   └── hudsonrock_service.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── tests/
├── requirements.txt
├── README.md
├── Procfile
├── pytest.ini
└── runtime.txt
```

---

# ⚙️ Instruções de Instalação na máquina pessoal

## 1. Clonar o repositório

```bash
git clone https://github.com/PalatinoMakaveli/Bootcamp2-LockScore.git
```

```bash
cd Bootcamp2-LockScore
```

---

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv .venv
```

---

## 3. Ativar ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando a Aplicação

```bash
flask --app src.app run
```

ou

```bash
python src/app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

Para parar a execução:

```text
Ctrl + C
```

---

# 🧪 Executando os Testes

```bash
pytest
```

---

# 🔍 Executando o Lint

```bash
ruff check .
```

---

# 🔐 Critérios de Avaliação da Senha

A aplicação utiliza uma abordagem baseada em regras, considerando:

- comprimento mínimo (≥ 12 caracteres)
- presença de letras maiúsculas
- presença de letras minúsculas
- presença de números
- presença de caracteres especiais

A pontuação acumulada define a classificação final da senha.

---

# Deploy

O deploy da aplicação foi realizado utilizando:

- Render

Tecnologias utilizadas no deploy:

- Gunicorn
- Ambiente Python
- Integração contínua com GitHub

---

# 🔄 Integração Contínua (CI/CD)

O projeto utiliza GitHub Actions para:

- execução automática de testes
- validação da aplicação
- verificação de qualidade de código
- linting automatizado
- integração contínua


---

# 📌 Versão Atual

**v1.1.0 - Entrega Intermediária**

---

# Autor

**Gustavo Augusto D. Braga**

GitHub:
https://github.com/PalatinoMakaveli

---

# Repositório Público

https://github.com/PalatinoMakaveli/Bootcamp2-LockScore

---

# Melhorias Futuras

- autenticação de usuários
- histórico de análises
- dashboard de segurança
- banco de dados
- relatórios de segurança
- sistema de usuários

---

# Licença

Este projeto está sob a licença MIT.
