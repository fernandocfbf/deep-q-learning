import matplotlib.pyplot as plt

def rewardsEpisodes(rewards, algorithm="deep"):
    new_rewards = calculateMetrics(rewards)
    plt.plot(new_rewards)
    plt.xlabel('Episodes')
    plt.ylabel('# Metrics')
    plt.title('# Rewards vs Episodes')
    plt.savefig("src/results/{0}/lunar_lander_v1.jpg".format(algorithm))     
    plt.close()

def calculateMetrics(rewards):
    return rewards