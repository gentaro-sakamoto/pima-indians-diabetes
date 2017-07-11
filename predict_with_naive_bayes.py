import csv
import random

def loadCsv(filename):
  rows = csv.reader(open(filename, 'r'))
  dataset = list(rows)
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]
  return dataset

def splitDataset(dataset, splitRatio):
  trainSize = int(len(dataset) * splitRatio)
  trainSet = []
  copiedDataSet = list(dataset)
  while len(trainSet) < trainSize:
    index = random.randrange(len(copiedDataSet))
    trainSet.append(copiedDataSet.pop(index))
  return [trainSet, copiedDataSet]

train, test = splitDataset(loadCsv('pima-indians-diabetes.csv'), 0.6)
print(train)
print(test)
