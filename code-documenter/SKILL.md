---
name: code-documenter
description: Documentação avançada de código. Lê diferenças (git diff), analisa o contexto usando RAG/MCPs, e produz documentações essenciais (README, Development docs) bilingues (PT e EN) por padrão.
version: 1.0.0
category: documentation
prerequisites:
  - git (CLI access)
  - MCP servers/RAG integrations (ex: NotebookLM ou ferramentas vetoriais ativadas no ambiente)
---

# Code Documenter Skill

> **OBJETIVO:** Automatizar a criação e a manutenção da documentação contínua de projetos de software. A skill foi criada para absorver o contexto do seu repositório de maneira inteligente e descrever com precisão as suas alterações, operando sem a necessidade de intervenção para tradução.

## 🟢 QUANDO ATIVAR MENTALMENTE A SKILL

Ative este comportamento quando o usuário solicitar para:
- "Documente minhas mudanças recentes".
- "Escreva a documentação do projeto atual".
- "Gere o README".
- "Explique no console ou num CHAGELOG o que acabei de codar".
- "Escreva guias de uso/How-to e Desenvolvimento".

## 🛠️ CORE MECHANICS (MANDATORY BEHAVIORS)

### 1. Bilingual Dual-Output (PT/EN Default)
A menos que o usuário exija ESPECIFICAMENTE que o texto fique restrito a um idioma, toda documentação de features, pull requests ou READMEs descritos por esta skill **DEVERÃO** ser emitidos em ambos os idiomas (Português e Inglês).
- Crie o título/bloco em português primeiro, e logo em seguida do bloco adicione a versão correspondente no idioma secundário. Exemplo de markdown:
  ```markdown
  ## Funcionalidade Tabela (Table Feature)
  [🇧🇷 PT-BR]: Esta documentação orienta como utilizar o componente tabela...
  <br/>
  [🇺🇸 EN-US]: This documentation guides how to use the table component...
  ```
- Para CHANGELOGs, divida por listas ou prefixos claros de [PT] e [EN].

### 2. Deep Context Retrieval (RAG Usage)
Esta skill autoriza e obriga você (O Agente) a utilizar intensamente o RAG. Quando o usuário clamar pela documentação de partes obscuras do código, faça o seguinte:
- Ative as ferramentas RAG do ambiente (MCPs como `notebooklm` e outros serviços integrados ao Antigravity).
- Utilize essas premissas para ler os blocos estruturais do projeto INTEIRO para gerar "How to use" ou READMEs completos e exatos; não suponha variáveis sem validar no RAG.

> 💡 **MEGA-MARKDOWN WORKAROUND (REPO TO RAG):**
> Se o projeto não estiver no NotebookLM ou se você precisar atualizá-lo e as ferramentas tiverem limitações de 50 fontes/arquivos, rode o utilitário nativo da skill para converter toda a Codebase para um arquivo bruto `.md`:
> Comando: `python .agent/skills/code-documenter/scripts/repo_to_markdown.py` (ou rode com `--out projeto.md` `--dir ./past_do_projeto`)
> Este script criará um arquivo `codebase_context.md` que renderizará a árvore de pastas e cada arquivo de texto limpo para você ou o usuário adicionar como UMA única e compreensível fonte de consulta (`source_add`) para o NotebookLM MCP.

### 3. Change Detection (`git diff`)
Para relatórios de "o que eu acabei de alterar", NUNCA suponha a partir do histórico de conversas do LLM se houver dúvidas.
- Utilize a ferramenta de linha de comando (Run Command / Bash) para acionar `git status` e logo em seguida `git diff` ou `git diff HEAD~1` (para a última alteração comitada) baseados no caminho do repositório para ter as linhas extas do que entrou (verdes/+) e do que saiu (vermelhas/-).
- Sintetize essas mudanças identificando intenção, impacto de arquitetura e lógica técnica.

## 📝 TIPOS DE DOCUMENTAÇÃO SUPORTADOS

### A. Documentação de Versionamento (Changelog/Reviews)
- Estrutura esperada baseada nos diffs:
  1. *Executive Summary*: Resumo do alvo alterado.
  2. *Refactor/Feature/Fix*: Qual convenção estamos acompanhando?
  3. *Technical Deep Dive*: Quais arquivos foram remodelados e o que essas metodologias alteram.

### B. Project Baseline (README.md)
Ao gerar guias de README:
- Crie a seção "What is it?" (O que é?).
- "Stack & Pre-requisites".
- "Installation".
- "Quick Start/Usage".
- Indique os crachás/badges do projeto.

### C. Contribution & Development (DEVELOPMENT.md)
Guia focado no time da engenharia:
- Arquitetura principal (pastas).
- Comandos cruciais do repositório (Testes, Linters).
- Padronização de commit.

## 🛑 REGRAS NEGATIVAS
- **NÃO** sobrescreva documentos de Changelogs inteiros; use o método de edição do append ou substituição parcial na hora de atualizar logs diários.
- **NÃO** produza sumários superficiais. Exija de si mesmo precisão técnica: cite nomes de funções, rotas, variáveis de ambiente ou arquivos concretos descobertos através do RAG e Diff.
