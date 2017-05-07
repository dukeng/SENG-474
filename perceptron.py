import numpy as np
import random

class TrainingTuple:
	def __init__(self, data, expected):
		self.data = data
		self.expected = expected


class Perceptron:
	def __init__(self, learningRate):
		self.trainingData = self.getTrainingData()
		self.learningRate = learningRate

		# initial weights provided with training data
		self.weights = [0.3, 0.8, -2.2]


	def getTrainingData(self):
		return [
			TrainingTuple([3, 0.2, 1], -1),
			TrainingTuple([1, 0.3, 1], -1),
			TrainingTuple([4, 0.5, 1], -1),
			TrainingTuple([2, 0.7, 1], -1),
			TrainingTuple([0, 1.0, 1], -1),
			TrainingTuple([1, 1.2, 1], -1),
			TrainingTuple([1, 1.7, 1], -1),
			TrainingTuple([6, 0.2, 1], 1),
			TrainingTuple([7, 0.3, 1], 1),
			TrainingTuple([6, 0.7, 1], 1),
			TrainingTuple([3, 1.1, 1], 1),
			TrainingTuple([2, 1.5, 1], 1),
			TrainingTuple([4, 1.7, 1], 1),
			TrainingTuple([2, 1.9, 1], 1)
		]

	# returns a list of misclassified training tuples
	def misclassifiedTuples(self):
		misclassified = []
		for trainingTuple in self.trainingData:
			if np.sign(np.dot(self.weights, trainingTuple.data)) is not trainingTuple.expected:
				misclassified.append(trainingTuple)
		return misclassified


	def updateWeights(self, trainingTuple):
		weightUpdates = [self.learningRate * trainingTuple.expected * i for i in trainingTuple.data]
		self.weights = [sum(elements) for elements in zip(self.weights, weightUpdates)]
		print(self.weights)


	def train(self):
		for misclassifiedTuple in self.misclassifiedTuples():
			self.updateWeights(misclassifiedTuple)


if __name__ == "__main__":
	perceptron = Perceptron(0.01)
	perceptron.train()
	print(perceptron.weights)



