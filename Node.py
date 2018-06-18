from Neighbor import Neighbor

class Node:
	def __init__(self, name, neighbors, reward):
		self.name = name
		self.reward = reward
		self.utility = reward
		self.tempUtility = reward
		self.policy = 'surveillance'
		self.neighbors = []
		for neighbor in neighbors:
			self.neighbors.append(Neighbor(neighbor[0], neighbor[1]))

	def __str__(self):
		string = 'Node ' + self.name
		for neighbor in self.neighbors:
			string += '\n---------\n' + str(neighbor) + '\n'
		return string + '\n*********************************\n'
