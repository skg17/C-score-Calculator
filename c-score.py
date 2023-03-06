import numpy as np
import pandas as pd

def check(grade):
    if type(grade) != float:
        return False

    elif grade > 100:
        return False

    elif grade < 0:
        return False

    else:
        return True
        
def get_grade(module):
    valid = False

    while valid == False:
        print("Please enter your grade for '{0}': ".format(module))
        grade = float(input())

        valid = check(grade)

    return grade

def check_options(opt5, opt6):
    opt5 = opt5.split(" ")
    opt6 = opt6.split(" ")

    optionals = ["Experimental Physics", "Stellar Structure and Evolution", "Introduction to Numerical Modelling", "Symmetry in Physics", "Mathematical Methods for Theoretical Physics", "Group Project in Applied Physics", "Principles of Biophysics", "Introduction to Medical Physics", "Advanced Mathematical Methods for Theoretical Physics", "Fundamentals of Nanotechnology", "General Relativity and Cosmology", "Advanced Biophysics", "Medical Imaging", "Modelling Flow and Transport"]

    level5o = []
    level6o = []

    for i in opt5:
        level5o.append(optionals[int(i)-1])

    for i in opt6:
        level6o.append(optionals[int(i)-1])

    return level5o, level6o

level5 = ["Quantum Mechanics I", "Electromagnetism", "Mathematical Methods for Physics", "Thermal Physics and Properties of Matter", "Relativity and Sub-atomic Physics"]
level6 = ["Condensed Matter Physics I", "Third Year Project in Physics", "Statistical Mechanics", "Quantum Mechanics II", "Particle Physics", "Optics"]
best = []

print("Before your C-score can be calculated I need to know what optional modules you took.\nPlease enter the number corresponding to your optional module (separated by a space): ")
print("\nLet's start with Year 2, which modules did you take?")
print("1. Experimental Physics")
print("2. Stellar Structure and Evolution")
print("3. Introduction to Numerical Modelling")
print("4. Symmetry in Physics")
print("5. Mathematical Methods for Theoretical Physics")
print("6. Group Project in Applied Physics")
print("7. Principles of Biophysics")
print("8. Introduction to Medical Physics")
opt5 = input()

print("\nLet's move on to Year 3, which modules did you take?")
print("9. Advanced Mathematical Methods for Theoretical Physics")
print("10. Fundamentals of Nanotechnology")
print("11. General Relativity and Cosmology")
print("12. Advanced Biophysics")
print("13. Medical Imaging")
print("14. Modelling Flow and Transport")
opt6 = input()

level5o, level6o = check_options(opt5, opt6)

level5 += level5o
level6 += level6o

#print(level5, level6)

print("\nNow we're gonna take a look at how you did in your Year 2 modules.\nPlease enter these results one at a time when they're asked for. Just include the number, and no symbols other than a decimal point.")
print("e.g. If you got 45.67% on an exam, only type in '45.67'")

grades5 = []

for module in level5:
    grade = get_grade(module)
    grades5.append(grade)

year2 = pd.DataFrame(data = {'Module':level5, 'Grade':grades5, 'Weight': [3 for i in range(len(level5))], 'Credits': [15 for i in range(len(level5))]})
#'Credits' assignation assumes all modules were passed 

print("\nFinally, let's take a look at your Year 3 results. If you have not gotten your final module grades yet just put in what you're hoping/expecting to get.\nPlease enter these results one at a time when they're asked for, in the same format as before.")

grades6 = []

for module in level6:
    grade = get_grade(module)
    grades6.append(grade)

year3 = pd.DataFrame(data = {'Module':level6, 'Grade':grades6})
year3 = year3.sort_values(by='Grade', ascending=False)

weight6 = [5 for i in range(6)]
weight6 += [3 for i in range(len(level6)-6)]

year3['Weight'] = weight6
year3['Credits'] = [15 for i in range(len(level6))]

final_grades = pd.concat([year2, year3])

denom = 15 * (10 * 3 + 6 * 5)

partial_c = (final_grades['Grade'] * final_grades['Weight'] * final_grades['Credits'])

final_grades['Partial C'] = partial_c

c_score = (final_grades['Partial C'].sum()) / denom
c_score = round(c_score, 2)

print(final_grades)
print("\nYour final C-score is: {0}".format(c_score))
