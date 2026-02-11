# Análise de Dados Aplicada à Dosimetria em Diagnóstico por Imagem

## Objetivo

Este projeto simula um banco de dados hospitalar para análise de dose de radiação recebida por pacientes em exames de diagnóstico por imagem.

O objetivo é aplicar conceitos de SQL e Python para:

- Modelagem relacional
- Consultas com JOIN
- Agregações e estatística descritiva
- Aplicação de regra de negócio (classificação de risco)
- Visualização de dados

---

## Estrutura do Banco de Dados

O banco é composto por quatro tabelas relacionais:

- pacientes  
- exames  
- equipamentos  
- registros_exames  

A tabela `registros_exames` integra as demais por meio de chaves estrangeiras.

Os dados são simulados automaticamente para o ano de 2025.

---

## Tecnologias Utilizadas

- Python 3  
- SQLite  
- Pandas  
- Matplotlib  

---

## Como Executar

1. Clone o repositório:

git clone <link-do-repositorio>


2. Execute a criação do banco:

python criacao_banco.py


3. Execute a análise:

python analise_dados.py


O script exibirá:

- Resumo estatístico das doses
- Classificação de risco anual por paciente
- Gráfico da dose acumulada anual

---

## Regra de Negócio Aplicada

Foi definido um limite anual hipotético de 100 mSv.

Pacientes acima desse valor são classificados como:

ACIMA DO LIMITE

Demais pacientes:

DENTRO DO LIMITE

No gráfico, pacientes acima do limite são destacados em vermelho.

---

## Resultados Obtidos

A análise permite identificar:

- Pacientes com maior dose acumulada
- Impacto de exames de maior intensidade (ex: Tomografia)
- Distribuição estatística das doses

---

## Objetivo Profissional

Este projeto foi desenvolvido com foco em:

- Consolidação de SQL aplicado
- Integração SQL + Python
- Estruturação de projeto para portfólio em Análise de Dados
- Aplicação de raciocínio quantitativo na área da saúde

---

## Autor

Wildenbergue Jr.
Graduando em Física  
Foco em Física Médica, Dosimetria e Perícia Científica
