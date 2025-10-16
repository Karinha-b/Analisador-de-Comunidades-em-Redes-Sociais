# Analisador-de-Comunidades-em-Redes-Sociais
#### Grupo: Bruna Carina de Matos Vieira e Manuele Vitoria da Conceição Ribeiro
 Objetivo: Ler um grafo de amizades (não-dirigido), encontrar todos os componentes conexos e exibir o número de comunidades encontradas, listando os membros de cada uma.


### Antes de começar, para compilar este codigo verifique:

- Que a versão do Python instalada no seu dispositivo seja Python 3.8 ou superior
- Se as bibliotecas networkx e matplotlib estao instaladas, se não ultilize pip install (biblioteca) para instalar

### Como executar a partir do codigo fonte: 
Garanta que o arquivo grafo.txt esteja na mesma pasta com o codigo para que seja possivel fazer a leitura corretamente
do grafo.

No terminal do seu dispositivo insira o caminho da pasta onde esta o arquivo.
#### Entre o local da pasta: 
exemplo: cd "C:\Users\usuario\Desktop\Codigo\Projeto_Grafo"

#### Execute o programa:
python analisador_comunidade.py ou python3 analisador_comunidade.py

Ou
Abra a pasta contendo o codigo e o arquivo grafo.txt em uma IDE de sua escolha e inicie o codigo

### Como gerar um executável (.exe):
No terminal
#### Instale o PyInstaller:
pip install pyinstaller

#### Dentro da pasta do projeto:
exemplo: cd "C:\Users\usuario\Desktop\Codigo\Projeto_Grafo"

#### Gere o executavel:
pyinstaller --onefile --hidden-import="matplotlib.backends.backend_tkagg" analisador_comunidade.py

Antes de prosseguir garanta que o arquiuvo grafo.txt esta na pasta dist criada apos a compilação

#### Entre o local da pasta dist: 
exemplo: cd "C:\Users\usuario\Desktop\dist"

#### Execute o programa:
.\analisador_comunidade.exe ou analisador_comunidade.exe

### O programa ira:

- Ler o arquivo grafo.txt
- Mostrar a matriz de adjacência
- Listar vértices, graus e vizinhos
- Exibir todas as arestas
- Abrir uma janela com a representação grafica do grafo
- Mostrar as comunidades






