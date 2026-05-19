# jogo-da-forca-imperativo
Este repositório tem como objetivo armazenar arquivos que dizem respeito ao desenvolvimento da primeira atividade da disciplina "Paradigmas de Linguagens de Programação" com foco no Paradigma Imperativo, utilizando a implementação do Jogo da Forca.

## Divisão de Tarefas e Arquitetura do Projeto

O desenvolvimento do jogo foi dividido em três frentes de trabalho, garantindo o isolamento das responsabilidades e minimizando conflitos de versão:

### Yuri: Lógica do Jogo (Controlador)
**Arquivo de trabalho principal:** `engine.py`
* Lida com a lógica do jogo em si, os fluxos de controle e o estado da partida em execução. 
* **Atribuições:** Vai criar as estruturas de estado (palavra a ser adivinhada, letras que já foram usadas, quantidade de erros). Implementar a atualização do estado da palavra (se uma letra já foi acertada, retornar a lista de letras escolhidas que não fazem parte da palavra secreta). Implementar a função de inicializar o jogo, processar a jogada com a letra enviada e fazer a contagem de jogadas (passou de 5 erros, perdeu o jogo).

### Taygo: Interface Visual (Visão / GUI)
**Arquivo de trabalho principal:** `interface.py`
* Lida estritamente com a renderização da interface e interação com o usuário.
* **Atribuições:** Vai construir a janela do jogo, criar a área de renderização do menu e da partida (com a forca, bonequinho, espaçamento de letras e lista visual de letras já utilizadas que não estão na palavra). Será responsável por vincular os eventos dos botões de clique às funções lógicas implementadas na Lógica do Jogo.

### Itallo: Persistência e Estrutura de Dados (Modelo)
**Arquivos de trabalho principais:** `dados.py` e `ranking.json`
* Lida com a persistência dos dados e com a organização deles em categorias.
* **Atribuições:** Vai criar repositórios de palavras de acordo com a categoria e dificuldade. Cada categoria terá uma lista para a dificuldade fácil e outra para a difícil, utilizando como parâmetro o tamanho da palavra (palavras com mais de 5 letras são consideradas difíceis). Com 3 categorias definidas, haverá 6 listas (2 dificuldades para cada). Lida também com a lógica de pontuação (vitória em single-player conta 1 ponto; vitória multiplayer conta 2 pontos). Os pontos devem persistir junto ao nome do jogador em um arquivo do tipo `.json`.
