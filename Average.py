numberOfTests = 0
score = 0
total = 0.0
average = 0.0
scoreCount = 0

numberofTests = int(input("Please enter the number of test you want to average: "))

#Make these next three lines repeat until scoreCount = numberOfTests
score = int(input("Please enter a score: "))
scoreCount = scoreCount + 1
total = total + score


average = total/scpreCount
print("The average is ", average)
