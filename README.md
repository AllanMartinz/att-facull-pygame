# 🦇 Flappy Bat

Um jogo inspirado em Flappy Bird desenvolvido em Python utilizando exclusivamente a biblioteca Pygame.

O projeto recria a jogabilidade de desviar obstáculos.

---

# 🎮 Gameplay

- Controle um morcego voando por obstáculos infinitos
- Sistema de colisão utilizando máscaras (`pygame.mask`)
- Física simples com gravidade e impulso
- Animações do personagem
- Contador de pontos
- Sons e música de fundo
- Cenário com movimentação contínua (parallax)

---

# 📁 Estrutura do Projeto

```txt
.
├── assets/
│   ├── audio/
│   ├── images/
│   └── font/
├── bat.py
├── obstacles.py
├── game_objects.py
├── settings.py
├── main.py
├── FlappyBat.exe
├── requirements.txt
└── README.md
```

---

# 🧠 Organização dos Scripts

## `main.py`
Responsável pelo loop principal do jogo:

- Inicialização do Pygame
- Carregamento dos assets
- Atualização dos objetos
- Renderização da tela
- Controle de eventos

---

## `bat.py`
Controla o personagem principal:

- Física e gravidade
- Pulo
- Rotação do morcego
- Animação
- Colisão

---

## `obstacles.py`
Responsável pelos obstáculos:

- Criação dos obstáculos superiores e inferiores
- Movimentação
- Sistema de pontuação
- Spawn procedural

---

## `game_objects.py`
Gerencia objetos auxiliares:

- Fundo
- Chão
- Sons
- Sistema de score

---

## `settings.py`
Arquivo com todas as configurações do jogo

---

# 🛠 Tecnologias Utilizadas

- Python 3
- Pygame 2.6.1

---

# ▶️ Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/AllanMartinz/att-facull-pygame
```

---

## 2. Entre na pasta do projeto

```bash
cd att-facull-pygame
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Execute o jogo

```bash
python main.py
```

---

# 🎯 Controles

| Ação | Controle |
|------|-----------|
| Voar | Clique do mouse |

---

# 📦 Dependências

```txt
pygame==2.6.1
```

---

# 🎨 Créditos

## Assets
https://demonstick-games.itch.io/pixel-art-2d-flappy-bird-like

## Fonte
https://fonts.google.com/specimen/Jersey+10

---

# 📌 Observações

- Alguns sprites foram levemente modificados.
- Projeto desenvolvido para fins de estudo utilizando Pygame.
- Inspirado no Flappy Bird.
