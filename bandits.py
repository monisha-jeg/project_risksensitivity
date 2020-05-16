import numpy as np

class gaussian_bandit:

	def __init__(self, K, mus_sigma_squares):
		#Number of arms
		self.K = K
		#Arms - a list of tuples where the ith tuples is (mu_i, sigma_i)
		self.arms = [(mu, np.sqrt(sigma_square)) for mu, sigma_square in mus_sigma_squares]
        
        print("Bandit born")


	def pull_arm(self, arm_number):

		mean, sd = self.arms[arm_number]
		sampled_reward = np.random.normal(mean, sd)        
		return sampled_reward
    

