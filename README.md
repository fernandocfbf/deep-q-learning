# Lunar Lander

O presente projeto tem como obejtivo implementar dois algoritmos, deep-q-learning e double-deep-q-learning, para atuar no ambiente lunar-lander da biblioteca gym.

O ambiente simula uma nave pousando em um planeta. A nave é controlada através de propulsores e deve pousar em segurança entre duas bandeiras posicionadas no solo.

## deep-q-learning

O primeiro algoritmo foi implementado usando Deep-Q-Learning segundo a referência: https://arxiv.org/abs/1312.5602. Os parâmetros utilizados na rede neural implementada estão disponíveis dentro da pasta constants/DeepQLearning.py

## double-deep-q-learning

O segundo algoritmo foi implementado usando Double-Deep-Q-Learning. O objetivo é utilizar uma segunda rede neural que será atualizada a cada X steps, equanto a primeira rede atualiza normalmente a cada passo. Dessa forma, as decições serão tomadas pela segunda rede, e o intuito é que ela seja treinada com um batch de ações, de forma que os pesos não sejam tão afetados por decisões únicas.

## resultados
Foram testados duas redes neurais diferentes sendo elas:

- três hidden layers: 34, 21, 13
- cinco hidden layers: 512, 256, 128, 64, 32

Além disso foram treinados algoritmos com 100, 300 e 500 episódios.

Não foram identificadas diferenças significativas em relação as redes neurais implementadas, uma vez que os resultados para o mesmo número de steps foi parecido. 

O melhor resultado encontrado foi apresnetado pelo algoritmo double-deep-q-leraning com um treinamento de 300 passos. A rede salva com os pesos se encontra na branch "best-result"