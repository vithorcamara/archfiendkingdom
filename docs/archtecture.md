archfiend-kingdom/
├── .github/                  # Workflows para automação (CI/CD)
│   └── workflows/
│       └── validate-deck.yml # Valida o JSON do deck (quantidade, banlist)
├── data/                     # Dados brutos e estruturados
│   ├── deck.json             # JSON fonte do deck (Main, Extra, Side)
│   └── cardinfo.json         # Banco de dados das cartas do deck e seus detalhes
├── docs/                     # Documentação extensa e guias
│   ├── cards-effects.md      # Tabela com tipo, custo/pré-req e efeitos
│   ├── combos.md             # Guia de combos detalhado por turno/situação
│   ├── decklist.md           # Lista do deck (Main, Extra, Side)
│   ├── strategy-guide.md     # Filosofia, match-ups e plano de jogo
│   └── side-decking.md       # Guia de troca de cartas (Side Out/In)
├── scripts/                  # Automações/Ferramentas
│   ├── export_ydk.py         # Converte o JSON para arquivo .ydk (YGOPro/EDOPro)
│   └── generate_readme.py    # Atualiza partes do README.md automaticamente
├── .gitignore                # Arquivos ignorados pelo Git
├── LICENSE                   # Licença (ex: MIT)
└── README.md                 # Landing page do repositório