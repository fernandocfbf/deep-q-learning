from collections import deque

GAMMA = 0.99 # 0.99 > 0.9
EPSILON = 1.0
EPSILON_MIN = 0.01
EPSILON_DEC = 0.99
EPISODES = 4
BATCH_SIZE = 64
MEMORY = deque(maxlen=500000)