# Orquestração e Automação

Instruções para executar o debate six-hats com o orquestrador SandecoMaestro ou manualmente.

## Integração com o Maestro

O `maestro_config.json` na pasta da skill define a sequência de fases. As configurações principais:

```json
{
  "skill_name": "six-hats",
  "orchestration_logic": "sequential",
  "default_rounds": 1,
  "phases": [
    {
      "name": "Exploração",
      "roles": ["ChapeuBranco", "ChapeuVermelho", "ChapeuAmarelo", "ChapeuVerde", "ChapeuVisionario"],
      "output_template": "templates/01_relatorio_exploracao.md",
      "repeatable": true
    },
    {
      "name": "TesteDeEstresse",
      "roles": ["ChapeuPreto"],
      "output_template": "templates/02_relatorio_teste_estresse.md",
      "repeatable": true
    },
    {
      "name": "PonteDoAnjo",
      "roles": ["Todos"],
      "instruction": "Identifique Fragmentos Positivos usando prefixo obrigatório 'O que eu mais gosto nessa ideia é...'",
      "output_template": "templates/03_relatorio_resgate.md",
      "repeatable": true
    },
    {
      "name": "SinteseFinal",
      "roles": ["ChapeuAzul"],
      "output_template": "templates/04_sintese_final.md",
      "condition": "apenas_na_ultima_rodada"
    }
  ]
}
```

Execute via Maestro:
```bash
/sandeco-maestro run six-hats --rounds 3
```

## Execução Manual

Se o Maestro não estiver disponível, execute o debate manualmente:

1. **Início**: Anuncie o tópico e o número de rodadas.
2. **Para cada rodada**:
   - Chame os chapéus em sequência: Branco → Vermelho → Amarelo → Verde → Visionário → Preto
   - Acione imediatamente o Advogado do Anjo após o Chapéu Preto
   - Se restam rodadas, use os fragmentos resgatados como entrada para o Chapéu Branco da próxima rodada
3. **Após a rodada final**: O Mediador sintetiza todos os fragmentos na Matriz de Decisão.

## Diretório de Saída

Salve os resultados no diretório `outputs/` do seu workspace atual, seguindo os templates em `templates/`.
