from Node import Node
from Neighbor import Neighbor

class MDP:
	threshold = .1
	surgeryWeights30p1 = [
		[1],
		[.05, .95],
		[.06, .94],
		[.07, .93],
		[.08, .92],
		[.09, .91],
		[.1, .9],
		[.1, .9],
		[.1, .9],
		[.1, .9],
		[.1, .9],
		[.1, .9],
		[.1, .9],
		[.1, .9]
	]
	surgeryWeights60p1 = [
		[1],
		[.05, .95],
		[.07, .93],
		[.09, .91],
		[.11, .89],
		[.13, .87],
		[.15, .85],
		[.17, .83],
		[.19, .81],
		[.21, .79],
		[.23, .77],
		[.25, .75],
		[.27, .73],
		[.29, .71]
	]
	surveillanceWeights30p1 = [
		[1],
		[.01, .99],
		[.1, .1, .6, .2],
		[.11, .09, .59, .1],
		[.12, .08, .58, .22],
		[.13, .07, .57, .23],
		[.14, .06, .56, .24],
		[.15, .05, .55, .25],
		[.16, .04, .54, .26],
		[.17, .03, .54, .26],
		[.18, .02, .54, .26],
		[.19, .01, .54, .26],
		[.2, .54, .26],
		[.16, .84]
	]
	surveillanceWeights60p1 = [
		[1],
		[.09, .91],
		[.2, .1, .5, .2],
		[.21, .09, .5, .2],
		[.22, .08, .5, .2],
		[.23, .07, .5, .2],
		[.24, .06, .5, .2],
		[.25, .05, .5, .2],
		[.26, .04, .5, .2],
		[.27, .03, .5, .2],
		[.28, .02, .5, .2],
		[.29, .01, .5, .2],
		[.30, .5, .2],
		[.31, .69]
	]

	surgeryWeights30p2 = [
		
	]
	surgeryWeights60p2 = [
		[1],
		[0.4395, 0.5605],
		[0.4234, 0.5766],
		[0.4085, 0.5915],
		[0.3948, 0.6052],
		[0.3823, 0.6177],
		[0.371, 0.629],
		[0.3609, 0.6391],
		[0.352, 0.648],
		[0.3443, 0.6557],
		[0.3378, 0.6622],
		[0.3325, 0.6675],
		[0.3284, 0.6716],
		[0.3255, 0.6745]
	]
	surveillanceWeights30p2 = [
		
	]
	surveillanceWeights60p2 = [
		[1],
		[0.09, 0.91],
		[0.2, 0.1, 0.3, 0.2, 0.2,],
		[0.21, 0.09, .3, 0.2, 0.2,],
		[0.22, 0.08, 0.3, 0.2, 0.2,],
		[0.23, 0.07, .3, 0.2, 0.2,],
		[0.24, 0.06, 0.3, 0.2, 0.2,],
		[0.25, 0.05, .3, 0.2, 0.2,],
		[0.26, 0.04, 0.3, 0.2, 0.2,],
		[0.27, 0.03, .3, 0.2, 0.2,],
		[0.28, 0.02, 0.3, 0.2, 0.2,],
		[0.29, 0.01, .3, 0.2, 0.2,],
		[0.3, .5, 0.2,],
		[0.31, 0.69]
	]

	def __init__(self):
		# self.surgeryNodes30p1 = self.makeSurgeryNodes(MDP.surgeryWeights30p1, 30)
		# self.surgeryNodes60p1 = self.makeSurgeryNodes(MDP.surgeryWeights60p1, 60)
		# self.surveillanceNodes30p1 = self.makeSurveillanceNodes(MDP.surveillanceWeights30p1, 30)
		# self.surveillanceNodes60p1 = self.makeSurveillanceNodes(MDP.surveillanceWeights60p1, 60)

		# self.surgeryNodes30p2 = self.makeSurgeryNodesp2(MDP.surgeryWeights30p2, 30)
		self.surgeryNodes60p2 = self.makeSurgeryNodes(MDP.surgeryWeights60p2, 60)
		# self.surveillanceNodes30p2 = self.makeSurveillanceNodesp2(MDP.surveillanceWeights30p2, 30)
		self.surveillanceNodes60p2 = self.makeSurveillanceNodesp2(MDP.surveillanceWeights60p2, 60)

	def makeSurgeryNodes(self, weights, age):
		cure = 100 - age
		aaa = .9 * cure
		node1 = Node('Dead', [], -100)
		node1.neighbors = [Neighbor(node1, weights[0][0])]
		node2 = Node('no AAA', [], cure)
		node2.neighbors = [Neighbor(node1, weights[1][0]), Neighbor(node2, weights[1][1])]
		node3 = Node('<30 mm', [[node1, weights[2][0]], [node2, weights[2][1]]], aaa)
		node4 = Node('30-35 mm', [[node1, weights[3][0]], [node2, weights[3][1]]], aaa)
		node5 = Node('35-40 mm', [[node1, weights[4][0]], [node2, weights[4][1]]], aaa)
		node6 = Node('40-45 mm', [[node1, weights[5][0]], [node2, weights[5][1]]], aaa)
		node7 = Node('45-50 mm', [[node1, weights[6][0]], [node2, weights[6][1]]], aaa)
		node8 = Node('50-55 mm', [[node1, weights[7][0]], [node2, weights[7][1]]], aaa)
		node9 = Node('55-60 mm', [[node1, weights[8][0]], [node2, weights[8][1]]], aaa)
		node10 = Node('60-65 mm', [[node1, weights[9][0]], [node2, weights[9][1]]], aaa)
		node11 = Node('65-70 mm', [[node1, weights[10][0]], [node2, weights[10][1]]], aaa)
		node12 = Node('70-75 mm', [[node1, weights[11][0]], [node2, weights[11][1]]], aaa)
		node13 = Node('75-80 mm', [[node1, weights[12][0]], [node2, weights[12][1]]], aaa)
		node14 = Node('>80 mm', [[node1, weights[13][0]], [node2, weights[13][1]]], aaa)
		return [
			node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14
		]

	def makeSurveillanceNodes(self, weights, age):
		cure = 100 - age
		aaa = .9 * cure
		node1 = Node('Dead', [], -100)
		node1.neighbors = [Neighbor(node1, weights[0][0])]
		node2 = Node('no AAA', [], cure)
		node2.neighbors = [Neighbor(node1, weights[1][0]), Neighbor(node2, weights[1][1])]
		node14 = Node('>80 mm', [[node1, weights[13][0]]], aaa)
		node14.neighbors.append(Neighbor(node14, weights[13][1]))
		node13 = Node('75-80 mm', [[node1, weights[12][0]], [node14, weights[12][2]]], aaa)
		node13.neighbors.append(Neighbor(node13, weights[12][1]))
		node12 = Node('70-75 mm', [[node1, weights[11][0]], [node2, weights[11][1]], [node13, weights[11][3]]], aaa)
		node12.neighbors.append(Neighbor(node12, weights[11][2]))
		node11 = Node('65-70 mm', [[node1, weights[10][0]], [node2, weights[10][1]], [node12, weights[10][3]]], aaa)
		node11.neighbors.append(Neighbor(node11, weights[10][2]))
		node10 = Node('60-65 mm', [[node1, weights[9][0]], [node2, weights[9][1]], [node11, weights[9][3]]], aaa)
		node10.neighbors.append(Neighbor(node10, weights[9][2]))
		node9 = Node('55-60 mm', [[node1, weights[8][0]], [node2, weights[8][1]], [node10, weights[8][3]]], aaa)
		node9.neighbors.append(Neighbor(node9, weights[8][2]))
		node8 = Node('50-55 mm', [[node1, weights[7][0]], [node2, weights[7][1]], [node9, weights[7][3]]], aaa)
		node8.neighbors.append(Neighbor(node8, weights[7][2]))
		node7 = Node('45-50 mm', [[node1, weights[6][0]], [node2, weights[6][1]], [node8, weights[6][3]]], aaa)
		node7.neighbors.append(Neighbor(node7, weights[6][2]))
		node6 = Node('40-45 mm', [[node1, weights[5][0]], [node2, weights[5][1]], [node7, weights[5][3]]], aaa)
		node6.neighbors.append(Neighbor(node6, weights[5][2]))
		node5 = Node('35-40 mm', [[node1, weights[4][0]], [node2, weights[4][1]], [node6, weights[4][3]]], aaa)
		node5.neighbors.append(Neighbor(node5, weights[4][2]))
		node4 = Node('30-35 mm', [[node1, weights[3][0]], [node2, weights[3][1]], [node5, weights[3][3]]], aaa)
		node4.neighbors.append(Neighbor(node4, weights[3][2]))
		node3 = Node('<30 mm', [[node1, weights[2][0]], [node2, weights[2][1]], [node4, weights[2][3]]], aaa)
		node3.neighbors.append(Neighbor(node3, weights[2][2]))
		return [
			node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14
		]

	def makeSurveillanceNodesp2(self, weights, age):
		cure = 100 - age
		aaa = .9 * cure
		node1 = Node('Dead', [], -100)
		node1.neighbors = [Neighbor(node1, weights[0][0])]
		node2 = Node('no AAA', [], cure)
		node2.neighbors = [Neighbor(node1, weights[1][0]), Neighbor(node2, weights[1][1])]
		node14 = Node('>80 mm', [[node1, weights[13][0]]], aaa)
		node14.neighbors.append(Neighbor(node14, weights[13][1]))
		node13 = Node('75-80 mm', [[node1, weights[12][0]], [node14, weights[12][2]]], aaa)
		node13.neighbors.append(Neighbor(node13, weights[12][1]))
		node12 = Node('70-75 mm', [[node1, weights[11][0]], [node2, weights[11][1]], [node13, weights[11][3]], [node14, weights[11][4]]], aaa)
		node12.neighbors.append(Neighbor(node12, weights[11][2]))
		node11 = Node('65-70 mm', [[node1, weights[10][0]], [node2, weights[10][1]], [node12, weights[10][3]], [node14, weights[10][4]]], aaa)
		node11.neighbors.append(Neighbor(node11, weights[10][2]))
		node10 = Node('60-65 mm', [[node1, weights[9][0]], [node2, weights[9][1]], [node11, weights[9][3]], [node14, weights[9][4]]], aaa)
		node10.neighbors.append(Neighbor(node10, weights[9][2]))
		node9 = Node('55-60 mm', [[node1, weights[8][0]], [node2, weights[8][1]], [node10, weights[8][3]], [node14, weights[8][4]]], aaa)
		node9.neighbors.append(Neighbor(node9, weights[8][2]))
		node8 = Node('50-55 mm', [[node1, weights[7][0]], [node2, weights[7][1]], [node9, weights[7][3]], [node14, weights[7][4]]], aaa)
		node8.neighbors.append(Neighbor(node8, weights[7][2]))
		node7 = Node('45-50 mm', [[node1, weights[6][0]], [node2, weights[6][1]], [node8, weights[6][3]], [node14, weights[6][4]]], aaa)
		node7.neighbors.append(Neighbor(node7, weights[6][2]))
		node6 = Node('40-45 mm', [[node1, weights[5][0]], [node2, weights[5][1]], [node7, weights[5][3]], [node14, weights[5][4]]], aaa)
		node6.neighbors.append(Neighbor(node6, weights[5][2]))
		node5 = Node('35-40 mm', [[node1, weights[4][0]], [node2, weights[4][1]], [node6, weights[4][3]], [node14, weights[4][4]]], aaa)
		node5.neighbors.append(Neighbor(node5, weights[4][2]))
		node4 = Node('30-35 mm', [[node1, weights[3][0]], [node2, weights[3][1]], [node5, weights[3][3]], [node14, weights[3][4]]], aaa)
		node4.neighbors.append(Neighbor(node4, weights[3][2]))
		node3 = Node('<30 mm', [[node1, weights[2][0]], [node2, weights[2][1]], [node4, weights[2][3]], [node14, weights[2][4]]], aaa)
		node3.neighbors.append(Neighbor(node3, weights[2][2]))
		return [
			node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14
		]

	def run(self):
		ret = {
			'30p1': {},
			'60p1': {},
			'30p2': {},
			'60p2': {}
		}

		# surgery30p1RewardIndex = self.solve(self.surgeryNodes30p1)
		# surgery60p1RewardIndex = self.solve(self.surgeryNodes60p1)
		# surveillance30p1RewardIndex = self.solve(self.surveillanceNodes30p1)
		# surveillance60p1RewardIndex = self.solve(self.surveillanceNodes60p1)

		# self.report(ret, '30p1', self.surgeryNodes30p1, self.surveillanceNodes30p1, surveillance30p1RewardIndex, surgery30p1RewardIndex)
		# self.report(ret, '60p1', self.surgeryNodes60p1, self.surveillanceNodes60p1, surveillance60p1RewardIndex, surgery60p1RewardIndex)

		# surgery30p2RewardIndex = self.solve(self.surgeryNodes30p2)
		print('p2 surgery utilities')
		surgery60p2RewardIndex = self.solve(self.surgeryNodes60p2)
		# surveillance30p2RewardIndex = self.solve(self.surveillanceNodes30p2)
		print('p2 surveillance utilities')
		surveillance60p2RewardIndex = self.solve(self.surveillanceNodes60p2)

		# self.report(ret, '30p2', self.surgeryNodes30p2, self.surveillanceNodes30p2, surveillance30p2RewardIndex, surgery30p2RewardIndex)
		self.report(ret, '60p2', self.surgeryNodes60p2, self.surveillanceNodes60p2, surveillance60p2RewardIndex, surgery60p2RewardIndex)

		return ret

	def solve(self, nodes):
		greatestChange = 0
		rewardIndex = 0
		tempRewardIndex = 1
		changed = True
		while(changed):
			changed = False
			for node in nodes:
				total = 0
				for neighbor in node.neighbors:
					total += neighbor.weight * neighbor.node.rewards[rewardIndex]
				node.rewards[tempRewardIndex] = total
				change = abs(node.rewards[tempRewardIndex] - node.rewards[rewardIndex])
				if change > greatestChange:
					greatestChange = change
					changed = True
			tempRewardIndex = rewardIndex
			rewardIndex = (rewardIndex + 1) % 2
			for node in nodes:
				print(node.rewards[rewardIndex])
			print('iterated\n')
		return rewardIndex

	def report(self, ret, k, surgeryNodes, surveillanceNodes, surveillanceRewardIndex, surgeryRewardIndex):
		for i in range(len(surgeryNodes)):
			surveillanceNode = surveillanceNodes[i]
			surgeryNode = surgeryNodes[i]
			if surveillanceNode.rewards[surveillanceRewardIndex] > surgeryNode.rewards[surgeryRewardIndex]:
				ret[k][surgeryNode.name] = 'surveillance'
			else:
				ret[k][surgeryNode.name] = 'surgery'

	def p(self):
		pass
		for node in self.surgeryNodes30:
			print(node)
		for node in self.surgeryNodes60:
			print(node)
		for node in self.surveillanceNodes30:
			print(node)
		for node in self.surveillanceNodes60:
			print(node)

mdp = MDP()
ret = mdp.run()
for key, val in ret.items():
	print(key)
	for key2, val2 in val.items():
		print('\t' + key2 + ': ' + val2)
