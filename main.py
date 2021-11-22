import urllib.request, json
import random

#/------------------------------------/#
# Json files path (questions)------------
jsonQuestionPath = 'https://d-wwts.ext.hp.com/qna/questions.json'
jsonAnswerPath = 'https://d-wwts.ext.hp.com/qna/answers.json'


def getJsonFile(jsonPath):
    try:
        with urllib.request.urlopen(jsonPath) as url:
            data = json.loads(url.read().decode())
            return data
    except:
        print("The file not exist\nPlease check and try again")

        
def reportAns (AnsResult):
    if (AnsResult):
        print("Yes, You Right It Is Correct Answer")
        print("------------------------------------")
    else:
        print("No, Wrong Answer, Please Try Again")
        print("------------------------------------")

# def getAns()

def getQuizGameQuestins(questionsFile, questionNum, exitFlag):
    ansArr = {"a":0,'A':0, 'b':1, 'B':1,"c":2,'C':2, 'd':3, 'D':3}
    answerFlag = True
    alfabet = 'A'
    numOfQuestions = len(questionsFile)
    questionIndex = random.randint(0, numOfQuestions-1)    # get random int between range

    # print(f"Question {questionNum}: {questionsFile[questionIndex]['q'] }")       #  OPTIONAL print -> Question[questionNum] increasing number
    print(f"Question {questionsFile[questionIndex]['id']}: {questionsFile[questionIndex]['q']}")
    print("Answer Options : ")

    # Display answer options
    for i in range(0, len(questionsFile[questionIndex]['a'])):
        print (f"{alfabet}. {questionsFile[questionIndex]['a'][i]}")
        alfabet = chr(ord(alfabet[0]) + 1)

    # input player answer and check
    while answerFlag:
        customerAns = input("Your Answer : ")

        if (customerAns >= 'a' and customerAns <= 'd') :
            customerAns = questionsFile[questionIndex]['a'][ansArr[customerAns]]
            answerFlag = False
        elif (customerAns >= 'A' and customerAns <= 'D') :
            customerAns = questionsFile[questionIndex]['a'][ansArr[customerAns]]
            answerFlag = False
        elif customerAns == 'X':
            answerFlag = False
            exitFlag = False
        else:
            print("Sorry, Wrong option, Please try again")
            print()

    return questionIndex,customerAns, exitFlag


def checkAnswer(answerFile, questionsNum, playerAns):
    # compering between plaryer answer and the right answer
    if answerFile[questionsNum]['a'] == playerAns:
        return True
    return False

def reportAns(AnsResult):
    if AnsResult:
        print("Good, Correct Answer")
        print("------------------------------------")
    else:
        print("Sorry, Wrong Answer")
        print("------------------------------------")


if __name__ == '__main__':
    exitFlag = True             # finish game flag
    questionCount = 0           # optional to display question counter
    # import Json files questions And answers
    questionsFile = getJsonFile(jsonQuestionPath)
    answerFile = getJsonFile(jsonAnswerPath)

    print ()
    print('-------------------------------------------------------------------------------------')
    print('-------- Welcome to "Quiz Game", in any stage press "X" to finish the game ----------')
    print('-------------------------------------------------------------------------------------')

    # main loop of questions
    while exitFlag:
        questionCount = questionCount + 1
        questionsNum, playerAns,exitFlag = getQuizGameQuestins(questionsFile, questionCount, exitFlag) # display and ask for answer
        if exitFlag:
            AnsResult = checkAnswer(answerFile, questionsNum, playerAns)
            reportAns(AnsResult)
    print("Thank You And Good Bay")






