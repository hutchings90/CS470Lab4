from Node import Node
from Neighbor import Neighbor

class MDP:
	threshold = .1
	surgeryWeights30 = [
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
	surgeryWeights60 = [
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
	surveillanceWeights30 = [
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
	surveillanceWeights60 = [
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

	def __init__(self):
		self.surgeryNodes30 = self.makeSurgeryNodes(MDP.surgeryWeights30, 30)
		self.surgeryNodes60 = self.makeSurgeryNodes(MDP.surgeryWeights60, 60)
		self.surveillanceNodes30 = self.makeSurveillanceNodes(MDP.surveillanceWeights30, 30)
		self.surveillanceNodes60 = self.makeSurveillanceNodes(MDP.surveillanceWeights60, 60)

	def makeSurgeryNodes(self, weights, age):
		cure = 100 - age
		aaa = .9 * cure
		node1 = Node('Dead', [], -100);
		node1.neighbors = [Neighbor(node1, weights[0][0])]
		node2 = Node('no AAA', [], cure);
		node2.neighbors = [Neighbor(node1, weights[1][0]), Neighbor(node2, weights[1][1])]
		node3 = Node('<30 mm', [[node1, weights[2][0]], [node2, weights[2][1]]], aaa);
		node4 = Node('30-35 mm', [[node1, weights[3][0]], [node2, weights[3][1]]], aaa);
		node5 = Node('35-40 mm', [[node1, weights[4][0]], [node2, weights[4][1]]], aaa);
		node6 = Node('40-45 mm', [[node1, weights[5][0]], [node2, weights[5][1]]], aaa);
		node7 = Node('45-50 mm', [[node1, weights[6][0]], [node2, weights[6][1]]], aaa);
		node8 = Node('50-55 mm', [[node1, weights[7][0]], [node2, weights[7][1]]], aaa);
		node9 = Node('55-60 mm', [[node1, weights[8][0]], [node2, weights[8][1]]], aaa);
		node10 = Node('60-65 mm', [[node1, weights[9][0]], [node2, weights[9][1]]], aaa);
		node11 = Node('65-70 mm', [[node1, weights[10][0]], [node2, weights[10][1]]], aaa);
		node12 = Node('70-75 mm', [[node1, weights[11][0]], [node2, weights[11][1]]], aaa);
		node13 = Node('75-80 mm', [[node1, weights[12][0]], [node2, weights[12][1]]], aaa);
		node14 = Node('>80 mm', [[node1, weights[13][0]], [node2, weights[13][1]]], aaa);
		return [
			node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14
		]

	def makeSurveillanceNodes(self, weights, age):
		cure = 100 - age
		aaa = .9 * cure
		node1 = Node('Dead', [], -100);
		node1.neighbors = [Neighbor(node1, weights[0][0])]
		node2 = Node('no AAA', [], cure);
		node2.neighbors = [Neighbor(node1, weights[1][0]), Neighbor(node2, weights[1][1])]
		node14 = Node('>80 mm', [[node1, weights[13][0]]], aaa);
		node14.neighbors.append(Neighbor(node14, weights[13][1]));
		node13 = Node('75-80 mm', [[node1, weights[12][0]], [node14, weights[8][3]]], aaa);
		node13.neighbors.append(Neighbor(node13, weights[12][2]));
		node12 = Node('70-75 mm', [[node1, weights[11][0]], [node2, weights[11][1]], [node13, weights[8][3]]], aaa);
		node12.neighbors.append(Neighbor(node12, weights[11][2]));
		node11 = Node('65-70 mm', [[node1, weights[10][0]], [node2, weights[10][1]], [node12, weights[8][3]]], aaa);
		node11.neighbors.append(Neighbor(node11, weights[10][2]));
		node10 = Node('60-65 mm', [[node1, weights[9][0]], [node2, weights[9][1]], [node11, weights[8][3]]], aaa);
		node10.neighbors.append(Neighbor(node10, weights[9][2]));
		node9 = Node('55-60 mm', [[node1, weights[8][0]], [node2, weights[8][1]], [node10, weights[8][3]]], aaa);
		node9.neighbors.append(Neighbor(node9, weights[8][2]));
		node8 = Node('50-55 mm', [[node1, weights[7][0]], [node2, weights[7][1]], [node9, weights[8][3]]], aaa);
		node8.neighbors.append(Neighbor(node8, weights[7][2]));
		node7 = Node('45-50 mm', [[node1, weights[6][0]], [node2, weights[6][1]], [node8, weights[8][3]]], aaa);
		node7.neighbors.append(Neighbor(node7, weights[6][2]));
		node6 = Node('40-45 mm', [[node1, weights[5][0]], [node2, weights[5][1]], [node7, weights[8][3]]], aaa);
		node6.neighbors.append(Neighbor(node6, weights[5][2]));
		node5 = Node('35-40 mm', [[node1, weights[4][0]], [node2, weights[4][1]], [node6, weights[8][3]]], aaa);
		node5.neighbors.append(Neighbor(node5, weights[4][2]));
		node4 = Node('30-35 mm', [[node1, weights[3][0]], [node2, weights[3][1]], [node5, weights[8][3]]], aaa);
		node4.neighbors.append(Neighbor(node4, weights[3][2]));
		node3 = Node('<30 mm', [[node1, weights[2][0]], [node2, weights[2][1]], [node4, weights[8][3]]], aaa);
		node3.neighbors.append(Neighbor(node3, weights[2][2]));
		return [
			node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14
		]

	def run(self):
		ret = {
			'30': {},
			'60': {}
		}

		greatestChange = 0
		rewardIndex = 0
		tempRewardIndex = 1
		changed = True
		while(changed):
			changed = False
			for node in self.surgeryNodes30:
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

		greatestChange = 0
		rewardIndex = 0
		tempRewardIndex = 1
		changed = True
		while(changed):
			changed = False
			for node in self.surveillanceNodes30:
				total = 0
				for neighbor in node.neighbors:
					total += neighbor.weight * neighbor.node.rewards[rewardIndex]
				node.rewards[tempRewardIndex] = total
				change = abs(node.rewards[tempRewardIndex] - node.rewards[rewardIndex])
				if change > greatestChange:
					greatestChange = change
					changed = True
			rewardIndex = tempRewardIndex
			tempRewardIndex = (rewardIndex + 1) % 2

		for i in range(len(self.surgeryNodes30)):
			surgeryNode = self.surgeryNodes30[i]
			surveillanceNode = self.surveillanceNodes30[i]
			if surveillanceNode.rewards[rewardIndex] > surgeryNode.rewards[rewardIndex]:
				ret['30'][surgeryNode.name] = 'surveillance'
			else:
				ret['30'][surgeryNode.name] = 'surgery'
	
		greatestChange = 0
		rewardIndex = 0
		tempRewardIndex = 1
		changed = True
		while(changed):
			changed = False
			for node in self.surgeryNodes60:
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

		greatestChange = 0
		rewardIndex = 0
		tempRewardIndex = 1
		changed = True
		while(changed):
			changed = False
			for node in self.surveillanceNodes60:
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

		for i in range(len(self.surgeryNodes60)):
			surgeryNode = self.surgeryNodes60[i]
			surveillanceNode = self.surveillanceNodes60[i]
			if surveillanceNode.rewards[rewardIndex] > surgeryNode.rewards[rewardIndex]:
				ret['60'][surgeryNode.name] = 'surveillance'
			else:
				ret['60'][surgeryNode.name] = 'surgery'

		return ret

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
