numberOfTests = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberOfTests = int(input("Please enter the number of test you want to average: "))

#Make these next three lines repeat until scoreCount = numberOfTests
while scoreCount < numberOfTests:
    score1 = int(input("Please enter a score: "))
    scoreCount = scoreCount + 1
    total = (score1 + total)
    if scoreCount == numberOfTests:
        break
    
average = total / numberOfTest
print("The average is ", average)
