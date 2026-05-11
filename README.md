🦇 Flappy Bat

Um jogo inspirado em Flappy Bird desenvolvido em Python utilizando exclusivamente a biblioteca Pygame.

O projeto recria a jogabilidade clássica de desviar obstáculos, mas com uma temática sombria envolvendo um morcego em um cenário pixel art.

🎮 Gameplay
Controle um morcego voando por obstáculos infinitos
Sistema de colisão utilizando máscaras (pygame.mask)
Física simples com gravidade e impulso
Animações do personagem
Contador de pontos
Sons e música de fundo
Cenário com movimentação contínua (parallax)
📸 Recursos do Projeto
Estrutura principal
bat.py             -> lógica do jogador
obstacles.py       -> geração e controle dos obstáculos
game_objects.py    -> fundo, chão, sons e score
main.py            -> loop principal do jogo
settings.py        -> configurações gerais
Outros arquivos
assets/            -> sprites, sons e fontes
FlappyBat.exe      -> versão executável do jogo
requirements.txt   -> dependências do projeto
🛠 Tecnologias Utilizadas
Python 3
Pygame
▶️ Como executar
1. Clone o repositório
git clone https://github.com/AllanMartinz/att-facull-pygame
2. Entre na pasta
cd att-facull-pygame
3. Instale as dependências
pip install -r requirements.txt
4. Execute o jogo
python main.py
🎯 Controles
Ação	Controle
Voar	Clique do mouse
📦 Dependências
pygame==2.6.1
🎨 Créditos
Assets

Sprites base utilizados no projeto:

Demonstick Games Assets

Fonte

Fonte pixel utilizada no score:

Jersey 10 - Google Fonts

📌 Observações
Alguns sprites foram levemente modificados para o projeto.
Este projeto foi desenvolvido para fins de estudo e prática com desenvolvimento de jogos em Python.
