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

## - Instruções de Instalação:

1. Instale o Git;

2. No terminal do Git digite: "git --version";

3. Instale o VS Code;

4. Instale a extensão oficial do python;

5. Instale o Python; 

6. Digite: "python --version" no CMD;

7. Abra o VS Code;

8. Aperte as teclas: Ctrl + Shift + P;

9. Digite: "Git: Clone";

10. Cole o link do github no VS Code na aba do Git Clone: https://github.com/PalatinoMakaveli/Bootcamp2-LockScore

11. Crie uma pasta chamada "lockscore";

12. Clique em open;

13. Abra o terminal do VS Code e digite: "pip install -r requirements.txt";

14. digite "cd src" e aperte enter;

15. para rodar o projeto digite: "python app.py";

16. depois abra no navegador: "http://127.0.0.1:5000";

17. após testar a aplicação aperte CTRL + C para encerrar o programa;

18. para rodar os testes saia do domain src digitando "cd .." e aperte enter;

19. Apos isso digite: "python -m pytest";

20. Para rodar o lint digite: "pip install ruff";

21. depois digite: "ruff check .";

## - Critérios de Avaliação da Senha:
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

## - Autor:

**Gustavo Augusto D. Braga**

---

## - Link do Repositório Público:
https://github.com/PalatinoMakaveli/Bootcamp2-LockScore

---

## - Licença:

Este projeto está sob a licença MIT.

---
