# P7 - Inatel

Materiais do **7º período** de Engenharia no Inatel: anotações de aula, listas de exercícios, laboratórios, trabalhos e preparação para provas.

O repositório também é um vault do [Obsidian](https://obsidian.md/). As notas `.md` usam links internos (`[[nota]]`) e imagens coladas (`Pasted image ....png`), então ficam melhor quando abertas nele.

## Disciplinas

| Pasta | Disciplina | Conteúdo |
|-------|------------|----------|
| [`C09/`](C09) | Computação Gráfica e Multimídia | Transformações geométricas, cores, curvas e superfícies, iluminação, dispositivos gráficos, dados multimídia, processamento de imagens. Em `Atividades/`: listas e reposições |
| [`C09-Lab/`](C09-Lab) | Laboratório de C09 | Notebooks Jupyter das aulas práticas (imagens vetoriais e matriciais, espaço de cores, histogramas, detecção de bordas...), trabalhos e provas práticas |
| [`C24/`](C24) | Inteligência Artificial | Notas de EDA, pré-processamento, regressão, classificação, kNN, K-means, MLP, CNN, Fuzzy, algoritmo genético e Q-Learning. Em `Listas/`: listas resolvidas |
| [`IA/`](IA) | Material de apoio de C24 | Slides das aulas, listas de exercícios, laboratórios (`Lab/`) e exercício avaliativo (preditor de imóveis com MLP) |
| [`S02/`](S02) | Banco de Dados NoSQL | MongoDB (`01`), Neo4j (`02`), Cassandra/colunar (`03`), Redis (`04`), além de NP1, NP2 e revisões |
| [`S07/`](S07) | Qualidade de Software | Modelo ISO/IEC 25010, tipos de testes, metodologias, planejamento de testes. `S07-Nome-Temporario/` é o projeto em grupo de testes automatizados de API com Postman/Newman, Docker e Jenkins |
| [`H01/`](H01) | Administração | Notas dos módulos 1 a 8, slides e série de exercícios |

## Outras pastas

- `Excalidraw/`: desenhos feitos com o plugin Excalidraw do Obsidian
- `copilot/`: conversas e prompts do plugin Copilot do Obsidian
- `Pasted image *.png` (raiz): imagens referenciadas pelas notas

## Como usar

- **Notas:** abra a pasta como vault no Obsidian.
- **Notebooks (C09-Lab, IA/Lab):** use Jupyter ou VS Code com Python. As dependências mais comuns são `numpy`, `pandas`, `matplotlib`, `opencv-python` e `scikit-learn`.
- **Scripts de S02:** cada atividade precisa do banco correspondente (MongoDB, Neo4j, Cassandra/Astra DB ou Redis) rodando. Veja o enunciado (`*_enunciado.md`) e o `requirements.txt` da pasta.
- **Projeto de S07:** veja as instruções em [`S07/S07-Nome-Temporario/README.md`](S07/S07-Nome-Temporario/README.md).

## Autor

Felipe Silva Loschi
