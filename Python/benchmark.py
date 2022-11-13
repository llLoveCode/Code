###
#Program: Benchmark tool
#Author: Andre S Lessa
###

### import modules

import sys
import string
import operator

### create dictionary of questions

def definequiz():
    questions = {}
    questions["1"] = "what is the number of IT employees of this company?"
    questions["2"] = "what is the total IT cost of this company?"

    return questions
### Loop to collect companies data

def collectresults():
    company = getcompanyname()
    while company:
        if company == "":
            break

        quizkeys = quiz.keys()
        quizkeys.sort()
        for question in quizkeys:
            showquestion(lo_question = question,lo_company = company)

        company = getcompanyname()
    if len(answers) > 0:
        generateresults()
        showresults(gl_companies,gl_avg,gl_max,gl_min)

        userinput = input("Do you want to save your results?")
        if string.upper(userinput[0]) == "Y":
            saveresults(gl_companies,gl_avg,gl_max,gl_min)
    return

###generate benchmark results

def generateresults():
    global gl_companies,gl_avg,gl_max,gl_min

    gl_companies = string.join(answers.keys(),",")

    company_count = len(answers.keys())

    lo_avg = []

    for company in answers.keys():
        lo_employees = answers[company][0][1]
        lo_const = answers[company][1][1]
        average = (float(lo_cost)/int(lo_employees))
        lo_avg = lo_avg + [average]

    gl_max = max(lo_avg)
    gl_min = min(lo_avg)
    gl_avg = reduce(operater.add,lo_avg) / company_count

    return

###interface to Enter company

def getcompanyname():
    print("Please enter the company name:"\
    "or press ENTER when you are done")

    userinput = input()

    return userinput

### Display questions and collect results

def showquestion(lo_question,lo_company):
    print(quiz[lo_question])

    if answers.has_key(lo_company):
        answers[lo_company] =answers[lo_company] + \
           [coerce(lo_question,raw_input())]
    else:
        answers[lo_company] = [coerce(lo_question,raw_input())]

    return

### save results in file
def saveresults(*arguments):
    file = open(filename,"r")
    for value in arguments:
        file.write(repr(value)+"\n")
    file.close

    showresults(gl_companies,gl_avg,gl_max,gl_min)

    print("The results were saved")

    return 

###load results from file
def loadresults():
    conut = 0
    file = open(filename,"r")
    line =file.readline()
    line = line[:-1]
    while line:
        if count == 0:
            lo_companies = line
        if count == 1:
            lo_avg = float(line)
        elif count == 2:
            lo_max = float(line)
        elif count == 3:
            lo_min = float(line)
        line = file.readline()
        line = line[:-1]
        count = count + 1

    file.close
    return(lo_companies,lo_avg,lo_max,lo_min)

def showresults(lo_comanies,lo_avg,lo_max,lo_min):
    print("Comanies : ")
    print(lo_companies)
    print("----------------------------------------")
    print("0.2f is average cost/employees"%lo_avg)
    print("0.2f is average cost/employees"%lo_max)
    print("0.2f is average cost/employees"%lo_min)
    print 
    return

###main action block

def main():
    print
    print("Welcome to the benchmark tool!")
    print

    userinput = input("Do you want to load the saved results?")

    if userinput == " ":
        collectresults()
    elif string.upper(userinput[0]) == "Y":
        gl_companies,gl_avg,gl_max,gl_min = loadresults()
        showresults(gl_companies,gl_avg,gl_max,gl_min)    
    else:
        collectresults()

    print
    sys.exit

### Global Variables
quiz = definequiz()
answers = {}
filename = "results.txt"
gl_companies = " "
gl_avg = 0
gl_max = 0
gl_min = 0

main()
