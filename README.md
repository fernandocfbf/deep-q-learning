# deep-q-learning

O presente projeto tem como obejtivo implementar dois algoritmos para atuar no ambiente lunar-lander da biblioteca gym.

O primeiro algoritmo foi implementado usando Deep-Q-Learning segundo a referência: https://arxiv.org/abs/1312.5602

O segundo algoritmo foi implementado usando Double-Deep-Q-Learning. O objetivo é utilizar uma segunda rede neural que será atualizada a cada X steps, equanto a primeira rede atualiza normalmente a cada passo. Dessa forma, as decições serão tomadas pela segunda rede, e o intuito é que ela seja treinada com um batch de ações, de forma que os pesos não sejam tão afetados por decisões únicas.