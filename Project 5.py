
import sys

fp = open("data.txt")
fp.readline()
outfile = open("output.txt",'w')

heightTotal = 0
weightTotal = 0
BMITotal = 0
peopleTotal = 0

maxHeight = 0
minHeight = sys.maxsize
maxWeight = 0
minWeight = sys.maxsize
maxBMI = 0
minBMI = sys.maxsize

print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"))

for line in fp:
    height = float(line[12:24])
    weight = float(line[24:])
    heightTotal += height
    weightTotal += weight
    BMI = weight/height ** 2
    BMITotal += BMI
    peopleTotal += 1

    if height > maxHeight:
        maxHeight = height
    if height < minHeight:
        minHeight = height

    if weight > maxWeight:
        maxWeight = weight
    if weight < minWeight:
        minWeight = weight

    if BMI > maxBMI:
        maxBMI = BMI
    if BMI < minBMI:
        minBMI = BMI

    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(line[0:12],height,weight,BMI))

heightAverage = heightTotal / peopleTotal
weightAverage = weightTotal / peopleTotal
BMIAverage = BMITotal / peopleTotal

print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",heightAverage,weightAverage,BMIAverage))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",maxHeight,maxWeight,maxBMI))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",minHeight,minWeight,minBMI))
