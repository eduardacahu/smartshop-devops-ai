# SmartShop Cloud - DevOps Inteligente com Integração de Inteligência Artificial Generativa

Este projeto apresenta a evolução de uma esteira tradicional de CI/CD para um fluxo DevOps Inteligente, utilizando o GitHub Actions integrado à API do Google Gemini para automação de decisões, gerenciamento de incidentes e auditoria de código fonte.

## Objetivo do Projeto
O objetivo principal é simular o ecossistema de operações de uma startup (SmartShop Cloud), onde agentes autônomos de Inteligência Artificial atuam como tomadores de decisão em pontos críticos do ciclo de vida do software: validação de qualidade, triagem de observabilidade e segurança da informação.

---

## Descrição das Pipelines Desenvolvidas

### 1. Quality Gate Inteligente (quality_gate.yml)
* **Funcionamento:** Executa os testes unitários automatizados utilizando a biblioteca pytest e gera relatórios de cobertura com o plugin pytest-cov. O relatório textual resultante é enviado via API para a Inteligência Artificial, que atua como uma barreira de qualidade (Quality Gatekeeper), decidindo de forma opinativa se o deploy deve ser APROVADO ou BLOQUEADO com base nos índices de cobertura obtidos.
![Execução do Quality Gate](
https://github.com/user-attachments/assets/941146ef-29c6-4db7-a712-b8044f0b9191)
### 2. Observabilidade Automatizada (observability.yml)
* **Funcionamento:** Realiza o monitoramento contínuo através da leitura estruturada dos arquivos de logs do sistema (logs/app.log) e métricas de infraestrutura (metrics/metrics.json). Ao interceptar anomalias configuradas — como erros de severidade CRITICAL ou picos de uso de CPU de 92% —, a Inteligência Artificial executa a triagem do incidente e faz a abertura automatizada de uma Issue detalhada no GitHub para a equipe de engenharia.
![Painel de Issues de Observabilidade]((https://github.com/user-attachments/assets/a4f319bc-c220-476f-9574-af1f38d028ce))
### 3. Agente de Segurança Autônomo (security_agent.yml)
* **Funcionamento:** Atua como um auditor automatizado de código focado no diretório principal (src/). O agente realiza uma análise estática no arquivo app.py buscando por vulnerabilidades e más práticas de desenvolvimento (como credenciais expostas diretamente no código). Ao detectar a falha, o agente classifica o nível de risco operacional e gera um chamado técnico sugerindo a refatoração segura do trecho impactado.
  ![Relatório do Agente de Segurança](https://github.com/user-attachments/assets/5cd909d1-0e58-45d5-8991-3a2a2180e9d2)
(https://github.com/user-attachments/assets/8060f01d-d34a-4e31-944e-dbdf3aea5f06)
---

## Tecnologias Utilizadas
* **Linguagem de Programação:** Python 3.10
* **Framework de Testes:** Pytest & Pytest-cov
* **Orquestração de CI/CD:** GitHub Actions
* **Processamento de Linguagem Natural:** Google Gemini API (modelo gemini-2.5-flash)
* **Interface de Automação:** GitHub CLI (gh issue) para gerenciamento de ocorrências via fluxo de trabalho.

---

## Organização do Grupo
* **Integrante 1:** Maria Eduarda Cahu
