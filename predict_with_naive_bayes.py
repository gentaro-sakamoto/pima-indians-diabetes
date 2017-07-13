import pprint
import csv
import random

csvFileName = 'pima-indians-diabetes.csv'

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

def separateByClass(dataset):
  separated ={}
  for i in range(len(dataset)):
    verctor = dataset[i]
    classValue = verctor[-1]
    if (classValue not in separated):
      separated[classValue] = []
    separated[classValue].append(verctor)
  return separated

dataset = loadCsv(csvFileName)
separated = separateByClass(dataset)
pprint.pprint(separated)
