#libraries
import gym
import numpy as np

#functions
from src.utils.NeuralNetwork import loadModel

#classes
from src.classes.DeepQLearning import DeepQLearning

#constants
from src.constants.DeepQLearning import *

env = gym.make('LunarLander-v2')
state = env.reset()
env.reset(seed=0)
np.random.seed(0)

my_model = loadModel(algorithm="double-deep")
done = False
rewards = 0
steps = 0

while not done and steps < MAX_STEPS:
    Q_values = my_model.predict(state[np.newaxis])
    action = np.argmax(Q_values[0])
    state, reward, done, info = env.step(action)
    rewards += reward
    env.render()
    steps += 1

print(f'Score = {rewards}')
input('hit enter to exit...')


