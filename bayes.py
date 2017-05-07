# get probability of words given the line, return the list of vocab and their probabilities
def extractVocabulary(line, vocabData):
	wordCount = 0
	wordlist = line.split()
	for word in wordlist:
		wordCount +=1
		if word in vocabData:
			vocabData[word] +=1
		else:
			vocabData[word] = 1
	return wordCount

def getProbability(vocabData, totalVocab, numberOfWords):
	vocabDataProb ={}
	for word in vocabData:
		prob = (vocabData[word] + 1) / (numberOfWords + totalVocab)
		vocabDataProb [word] = prob
	return vocabDataProb

def trainMultinomial():
	with open("traindata.txt", 'r') as traindata,open("trainlabels.txt", 'r') as trainlabels:
		positiveLines = 0
		totalLines = 0
		vocabDataPositive = {}# list of vocab and occurence with positive class
		vocabDataNegative = {}# list of vocab and occurence with negative class
		positiveWordCount = 0
		negativeWordCount = 0
		traindataLines = traindata.readlines()
		for index,line in enumerate(trainlabels):
			totalLines +=1
			if line.rstrip('\n') == "1":
				positiveLines +=1
				positiveWordCount += extractVocabulary(traindataLines[index], vocabDataPositive)
			else:
				negativeWordCount += extractVocabulary(traindataLines[index], vocabDataNegative)
		probOfC = positiveLines / totalLines #probablity of positive class

		totalVocab = len(set(list(vocabDataPositive.keys()) + list(vocabDataNegative.keys())))
		vocabDataNegativeProb = getProbability(vocabDataNegative, totalVocab, negativeWordCount)
		vocabDataPositiveProb = getProbability(vocabDataPositive, totalVocab, positiveWordCount)
		return (vocabDataNegativeProb, vocabDataPositiveProb, probOfC, totalVocab, negativeWordCount, positiveWordCount )

def applyMultinomial(line, vocabPositiveData, vocabNegativeData, probOfC, totalVocab, negativeWordCount, positiveWordCount):
	positiveProb = probOfC
	negativeProb = 1 - probOfC
	for word in line.split():
		if word in vocabPositiveData.keys():
			positiveProb *= vocabPositiveData[word]
		else:
			positiveProb *= (1) / (positiveWordCount + totalVocab) 
		if word in vocabNegativeData.keys():
			negativeProb *= vocabNegativeData[word]
		else:
 			negativeProb *= (1) / (positiveWordCount + totalVocab) 
	if negativeProb >= positiveProb:
		return 0
	else:
		return 1

if __name__ == "__main__":
	trainedData = trainMultinomial()
	vocabNegativeData = trainedData[0]
	vocabPositiveData = trainedData[1]
	probOfC = trainedData[2]
	totalVocab = trainedData[3]
	negativeWordCount = trainedData [4]
	positiveWordCount = trainedData [5]
	#run through training data again
	
	with open("traindata.txt", 'r') as traindata,open("trainlabels.txt", 'r') as classlables:
		classlablesLines = classlables.readlines()
		result = []
		for index,line in enumerate(traindata):
			result.append(applyMultinomial(line, vocabPositiveData, vocabNegativeData, probOfC, totalVocab, negativeWordCount, positiveWordCount))
		correct = 0
		for index in range(0, len(result) - 1):
			if result[index] == int(classlablesLines[index].strip()):
				correct +=1
		print("The accuracy of testing with the training data is: ",  correct / len(result))

	with open("testdata.txt", 'r') as traindata,open("testlabels.txt", 'r') as classlables:
		classlablesLines = classlables.readlines()
		result = []
		for index,line in enumerate(traindata):
			result.append(applyMultinomial(line, vocabPositiveData, vocabNegativeData, probOfC, totalVocab, negativeWordCount, positiveWordCount))
		correct = 0
		for index in range(0, len(result) - 1):
			if result[index] == int(classlablesLines[index].strip()):
				correct +=1
		print("The accuracy of testing with the test data is: ", correct / len(result))
