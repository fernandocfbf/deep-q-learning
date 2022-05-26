#libraries
import gym
import numpy as np

#functions
from src.utils.NeuralNetwork import generateNetwork, saveModel
from src.utils.PlotRewardsEpisodes import rewardsEpisodes

#classes
from src.classes.DeepQLearning import DeepQLearning

#constants
from src.constants.DeepQLearning import *

env = gym.make('LunarLander-v2')
env.reset(seed=0)
np.random.seed(0)

my_model = generateNetwork(
    input_shape=env.observation_space.shape[0],
    output_shape=env.action_space.n,
    loss_function="mse",
    learning_rate=0.001
)
deepQLearning = DeepQLearning(
    env=env,
    gamma=GAMMA,
    epsilon=EPSILON,
    epsilon_min=EPSILON_MIN,
    epsilon_dec=EPSILON_DEC,
    episodes=EPISODES,
    batch_size=BATCH_SIZE,
    memory=MEMORY,
    model=my_model)
rewards  = deepQLearning.train()
rewardsEpisodes(rewards, algorithm="double-deep")
saveModel(deepQLearning.model, algorithm="double-deep")
