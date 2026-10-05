# Archfiend Kingdom

Projeto de construção e documentação de um deck de Yu-Gi-Oh! que combina o motor Ritual/Pêndulo Archfiend com cartas Labrynth e Armadilhas Normais.

## Estado da lista

A lista registrada atualmente contém:

- Main Deck: 50 cartas
- Extra Deck: 8 cartas
- Side Deck: 12 cartas

Consulte [a decklist completa](docs/decklist.md) para ver as cartas e quantidades. Esses números refletem os arquivos do projeto e não representam uma afirmação de legalidade para um formato ou torneio específico.

## Documentação

- [Combos](docs/combos.md): mãos iniciais, sequências e resultados esperados. As linhas assumem que o oponente não interrompe, salvo indicação contrária.
- [Categorias e funções das cartas](docs/comboscategories.json): classificação funcional das cartas e seus papéis no deck.
- [Estrutura do projeto](docs/archtecture.md): visão geral dos diretórios e arquivos.

## Dados

- `data/deck.json` é a lista estruturada do deck, incluindo Main, Extra e Side, com dados das cartas.
- `data/cardinfo.json` guarda os dados obtidos do catálogo YGOPRODeck.

## Atualizar os dados de cartas

O script requer Python 3 e a biblioteca `requests`:

```bash
python -m pip install requests
python scripts/ygoprodeck.py
```

O script consulta a API do YGOPRODeck e substitui `data/cardinfo.json` pela base completa de cartas retornada pela API. Ele não atualiza `data/deck.json`.