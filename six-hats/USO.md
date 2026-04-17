# Guia de Uso: skill six-hats

A skill `six-hats` é um framework avançado de debate multiagente projetado para extrair o máximo de valor de ideias através de perspectivas isoladas e refinamento iterativo.

## Como Iniciar uma Sessão

Para iniciar um debate, invoque a skill com o tópico e o número de rodadas desejado.

**Solicitação padrão:**
`@six-hats Preciso de 3 rodadas sobre [Visão Geral do Tópico]`

### O Loop Iterativo (1..N Rodadas)

Cada rodada consiste de três fases distintas gerenciadas pelo **Mediador (Chapéu Azul)**:

1.  **Exploração (Divergência)**:
    -   **Chapéu Branco**: Fornece dados e fatos.
    -   **Chapéu Vermelho**: Compartilha intuições e sentimentos viscerais.
    -   **Chapéu Amarelo**: Identifica benefícios lógicos e valor.
    -   **Chapéus Verde/Visionário**: Exploram alternativas criativas e tendências futuras.
2.  **Teste de Estresse (Avaliação)**:
    -   **Chapéu Preto**: Identifica todos os riscos, falhas e preocupações de segurança.
3.  **A Ponte de Resgate (Advogado do Anjo)**:
    -   O Mediador aciona esta fase imediatamente após o Chapéu Preto.
    -   Todos os agentes devem resgatar um "fragmento positivo" usando o prefixo: *"O que eu mais gosto nessa ideia é..."*
    -   *Se restam rodadas: Retorne à Fase 1 usando os fragmentos resgatados como nova base.*

## Automação com Maestro

Você pode automatizar o ciclo completo de N rodadas usando a configuração de orquestração:

```bash
/sandeco-maestro run six-hats --rounds 3
```

> [!TIP]
> Certifique-se de que o `maestro_config.json` na pasta da skill está atualizado com a lógica `repeatable` correta para a fase `PonteDoAnjo`.

## Checklist de Validação

- [ ] O **Chapéu Preto** identificou pelo menos 3 riscos críticos?
- [ ] A fase do **Advogado do Anjo** ocorreu em toda rodada?
- [ ] O **Mediador** produziu uma Matriz de Decisão ou Arquitetura final?

---
*Resultados são salvos no diretório `outputs/` do seu workspace atual.*
