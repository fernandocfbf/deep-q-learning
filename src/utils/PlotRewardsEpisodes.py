import matplotlib.pyplot as plt

def rewardsEpisodes(rewards):
    new_rewards = calculateMetrics(rewards)
    plt.plot(new_rewards)
    plt.xlabel('Episodes')
    plt.ylabel('# Metrics')
    plt.title('# Rewards vs Episodes')
    plt.savefig("src/results/lunar_lander_v1.jpg")     
    plt.close()

def calculateMetrics(rewards):
    res = list()
    for i in range(len(rewards)):
        if i != 0: 
            compute = (rewards[i-1] - rewards[1])/(rewards[i-1])
            res.append(compute)
    return res