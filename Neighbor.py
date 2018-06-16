class Neighbor:
	def __init__(self, node, weight):
		self.node = node
		self.weight = weight

	def __str__(self):
		return 'Neighbor ' + self.node.name + '\nweight: ' + str(self.weight)
