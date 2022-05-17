#libraries
import gym
import numpy as np

#functions
from src.utils.NeuralNetwork import generateNetwork

#classes
from src.classes.DeepQLearning import DeepQLearning

#constants
from src.constants.DeepQLearning import *

env = gym.make('LunarLander-v2')
env.seed(0)
np.random.seed(0)

def main():
    my_model = generateNetwork(
        input_shape=env.observation_space.shape[0],
        output_shape=env.action_space.n,
        loss_function="mse",
        learning_rate=0.001
    )
    deepQLearning = DeepQLearning()


if __name__ == "main":
    main()
