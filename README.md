# 🏭 Automação Industrial: Gestão de Qualidade

Este projeto consiste em um sistema desenvolvido em Python para controle de qualidade em uma linha de produção industrial.

O sistema permite cadastrar peças, validar automaticamente se estão dentro do padrão estabelecido e gerar relatórios de produtividade, simulando um ambiente real de automação industrial.

---

## 🎯 Objetivo

Desenvolver um sistema simples de automação industrial que simule o controle de qualidade de peças em uma linha de produção, aplicando conceitos de lógica de programação, validação de dados e organização de processos.

---

## 📋 Regras de Aprovação

Uma peça será considerada **APROVADA** se atender aos seguintes critérios:

- **Peso:** entre 95g e 105g  
- **Cor:** Azul ou Verde  
- **Comprimento:** entre 10cm e 20cm  

Caso algum critério não seja atendido, a peça será automaticamente **REPROVADA**, e o sistema informará o motivo.

---

## ⚙️ Funcionalidades do Sistema

O sistema possui as seguintes funcionalidades:

1. Cadastrar nova peça
2. Listar peças aprovadas e reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final de produtividade
6. Validação automática de qualidade
7. Controle de peças por caixa (10 peças por caixa)

---

## 📊 Relatório de Produtividade

O sistema gera automaticamente um relatório contendo:

- Total de peças cadastradas
- Total de peças aprovadas
- Total de peças reprovadas
- Percentual de aprovação
- Percentual de reprovação
- Quantidade de caixas fechadas
- Peças fora de caixa
- Motivos de reprovação

---

## 🧪 Exemplos de Execução

### Cadastro de Peça Aprovada

![Cadastro de peça aprovada](prints/cadastro.png)

---

### Cadastro de Peça Reprovada

![Cadastro de peça reprovada](prints/reprovacao.png)

---

### Relatório Final de Produtividade

![Relatório final](prints/relatorio.png)

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Lógica de programação
- Estruturas condicionais
- Listas e dicionários
- Funções
- Controle de fluxo

---

## 👩‍💻 Autora

Tatiana Maschio  

Projeto desenvolvido para a disciplina:

**Algoritmos e Lógica de Programação**

Curso:

**Inteligência Artificial e Data Science**

Instituição:

**UNIFECAF**

---

## ▶️ Como Executar o Projeto

1. Abrir o terminal
2. Navegar até a pasta do projeto
3. Executar o arquivo principal:

```bash
python main.py