#GetData is used to gather the data from the txt file,
#and place it onto a list to be used later
def GetData():
    """open value.txt and place data into a list."""
    val_list = []
    with open("values.txt", "r") as f:
        for line in f:
         fields = line.split()
         rowdata = map(int, fields)
        val_list.extend(rowdata)
    return val_list

# CalcResults uses the information gatherd by GetData,
# and then uses it to calculate the max, min, and the average
def CalcResults(val_list):
    """simply do the math to get min max and average."""
    
    small = min(val_list)
    larg = max(val_list)
    avrage = sum(val_list)/len(val_list)
    return small, larg, avrage

#GradeDistribution uses another list to find the range of how many values show up,
#multiple times in the list.
def GradeDistribution():
    """create another list and do the grade distributino with it."""
    v_list = []
    with open("values.txt", "r") as f:
        for line in f:
            fields = line.split()
            rowdata = map(int, fields)
            v_list.extend(rowdata)

    scores = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for i in v_list:
        if i >= 90:
            scores["A"] += 1
        elif i >= 80:
            scores["B"] += 1
        elif i >= 70:
            scores["C"] += 1
        elif i >= 60:
            scores["D"] += 1
        elif i >= 50:
            scores["F"] += 1
    return scores['A'], scores['B'], scores['C'], scores['D'], scores['F']

#assign variables for small, large, and avrage
s, h, v = CalcResults(GetData())

#assiging a variabole to get only a specified element from the return
a = GradeDistribution()[0]
b = GradeDistribution()[1]
c = GradeDistribution()[2]
d = GradeDistribution()[3]
f = GradeDistribution()[4]  

#making the graphical interface with the important infromation to be displayed.
print("--------------------------------------------------")
print("Lowest               |Highest      |Average")
print("---------------------|-------------|--------------")
print(s,"                  |", h,"        |", v)
print("---------------------|-------------|--------------")
print("Grade Distribution   |             |              ")
print("---------------------|-------------|--------------")
print("50 ~ 59: ", f)
print("60 ~ 69: ", d)
print("70 ~ 79: ", c)
print("80 ~ 89: ", b)
print("90 ~ 100: ", a)