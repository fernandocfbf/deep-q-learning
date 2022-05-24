import matplotlib.pyplot as plt

def rewardsEpisodes(rewards):
    plt.plot(rewards)
    plt.xlabel('Episodes')
    plt.ylabel('# Rewards')
    plt.title('# Rewards vs Episodes')
    plt.savefig("src/results/lunar_lander_v1.jpg")     
    plt.close()