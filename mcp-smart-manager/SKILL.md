---
name: mcp-smart-manager
description: "Gerencia dinamicamente servidores MCP para respeitar o limite de 100 ferramentas, ativando/desativando servidores sob demanda."
category: system
risk: safe
tags: "[mcp, optimization, automation]"
---

# MCP Smart Manager

## Purpose
Esta skill automatiza a gestão do `mcp_config.json` para contornar o limite de 100 ferramentas do Antigravity. Como o agente (eu) tem permissões de escrita no sistema que scripts externos não possuem, eu assumo o papel de "Gerenciador" usando o `mcp_registry.json` como fonte da verdade.

## Core Capabilities
1. **Dynamic Profiling**: O agente alterna entre perfis (`research`, `ops`, `ai-dev`) editando o arquivo de configuração diretamente.
2. **Base Invariante**: Garante que o **GitHub MCP** e o **Sequential Thinking** estejam sempre ligados.
3. **Registry Sync**: Mantém todas as suas chaves de API e configurações salvas com segurança no registro, mesmo quando um servidor está "desligado" no arquivo principal.

## Como usar
Basta me pedir para trocar de foco ou realizar uma tarefa que exija uma ferramenta específica.
Exemplos:
- *"Mude para o perfil de pesquisa"*
- *"Ative as ferramentas do Cloud Run"*
- *"Analise esse documento usando o NotebookLM"* (Eu ativarei automaticamente se necessário).

## Perfis Configurados
- **research** (97 tools): GitHub + Sequential + NotebookLM + Knowledge.
- **ops** (92 tools): GitHub + Sequential + GitLens + Cloud Run + Prisma.
- **ai-dev** (67 tools): GitHub + Sequential + Genkit.

> [!TIP]
> Se você adicionar um novo servidor manualmente ao `mcp_config.json`, peça para eu "atualizar o registro" para que eu não perca essa configuração na próxima troca.
