# MCP Smart Manager

Implementamos com sucesso a skill **MCP Smart Manager**, que resolve o erro de limite de 100 ferramentas no Antigravity através de uma gestão dinâmica de servidores.

## Estrutura do Repositório

- `SKILL.md`: Instruções da habilidade para o Antigravity.
- `mcp_registry.json`: Registro completo de todos os servidores e tokens (Fonte da Verdade).
- `scripts/mcp_core.py`: Script de automação (opcional, já que o agente gerencia via JSON).
- `docs/profiles.md`: Detalhamento dos limites de ferramentas por perfil.

## O que foi feito

### 1. Registro de Segurança (`mcp_registry.json`)
Contém a configuração completa de todos os 8 servidores MCP. Isso garante que nenhuma configuração ou chave de API seja perdida quando um servidor for desativado no arquivo principal.

### 2. Nova Skill: `mcp-smart-manager`
Instalada globalmente, esta skill instrui o agente a:
- Monitorar a contagem de ferramentas (limite de 100).
- Manter o **GitHub** e o **Sequential Thinking** sempre ativos.
- Alternar entre perfis conforme a necessidade do usuário.

### 3. Aplicação do Perfil `research`
Ativado por padrão para resolver o erro de limite:
- **Ativos**: GitHub, Sequential Thinking, NotebookLM e Knowledge.
- **Em Standby**: Cloud Run, Prisma, Genkit e GitLens.

## Como usar

Peça ao agente para trocar o foco:

> "Mude para o modo de desenvolvimento (ops)"
> "Ative o Cloud Run"
> "Preciso usar o Genkit agora"

O agente fará o "swap" das ferramentas no `mcp_config.json`, o Antigravity recarregará os servidores, e no turno seguinte as ferramentas estarão prontas.
