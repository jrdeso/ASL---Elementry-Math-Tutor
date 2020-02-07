import sys

sys.path.insert(0, 'C:\Users\hocke\Desktop\LeapDeveloperKit_2.3.1+31549_win\LeapSDK\lib')
import Leap
import pickle
from pygameWindow import PYGAME_WINDOW
import random
import constants
import numpy as np
import time

database = pickle.load(open('userData\database.p', 'rb'))
#print(database)
userName = raw_input('Please enter your name: ')
if userName in database:
    print('Welcome back, ' + userName + '.')
    database[userName]['logins'] += 1

else:
    # Initialize the user's database
    database[userName] = {
        'logins' : 1,
        'Current Level' : 0,
        }
    print('Welcome, ' + userName + '.')
    
userRecord = database[userName]

# DEL 10 progress
successfulDigitsSigned = 0
User_Levels = []
User_Names = []
for username in database:
    User_Levels.append(database[username]['Current Level'])
    User_Names.append(username)

# EQUATIONS INITIALIZE
num1 = 0
num2 = 0
pos_neg = 0

# Find leaderboard top three
copy_data = User_Levels[:]
if len(User_Levels) > 2:
    # FIND TOP USER
    BEST = max(User_Levels)
    User_Levels.remove(BEST)

    # FIND SECOND BEST
    SECOND = max(User_Levels)
    User_Levels.remove(SECOND)

    # FIND THIRD BEST
    THIRD = max(User_Levels)
    User_Levels.remove(THIRD)

    BEST_AT = -1
    SECOND_AT = -1
    THIRD_AT = -1

    # FIND INDEXES of users
    for a in range(len(copy_data)):
        if BEST == copy_data[a]:
            BEST_AT = a
            break

    for b in range(len(copy_data)):
        if SECOND == copy_data[b]:
            if BEST_AT != b:
                SECOND_AT = b
                break

    for c in range(len(copy_data)):
        if THIRD == copy_data[c]:
            if BEST_AT != c:
                if SECOND_AT != c:
                    THIRD_AT = c
                    break

    
pickle.dump(database, open('userData/database.p', 'wb'))


clf = pickle.load(open('userData/classifier.p', 'rb'))

testData = np.zeros((1,30),dtype='f')

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0
x = 300
y = 300
            
pygameWindow = PYGAME_WINDOW()
controller = Leap.Controller()

programState = 0

timer = 0

handCenteredTimer = 0
greenCheckTimer = 0
randDigitTimer = 0
signCorrect = 0

numIndex = 0
currDigitList = [0, 1, 2]
digitToSign = currDigitList[numIndex]
currentLevel = 1
level4hintTimer = 0

level6count = 0
level6timeleft = 20
level6timeLeftActual = 11

#digitToSign = random.randint(0,10) - unorganized given random int to sign

def Handle_Frame(frame):
    global x, y, xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    
    for finger in fingers:
        Handle_Finger(finger)


def Handle_Finger(finger):
    for b in range(4):
        draw = 4 - b #bones are drawn 1 to 4, fingers first
        Handle_Bone(finger.bone(b), draw)


def Handle_Bone(bone, draw):
    base = bone.prev_joint
    tip = bone.next_joint
    
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)

    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, draw) #draw is b variable


def Handle_Vector_From_Leap(v):
    global x, y, xMin, xMax, yMin, yMax

    x = v[0]
    y = v[2]
    x = Scale(x,xMin,xMax,0, 750)
    y = Scale(y,yMin,yMax,0, 750)

    return x, y

    
def Scale(value, tempMin, tempMax, scaledMin, scaledMax):
    global xMin, xMax, yMin, yMax, timer
    timer += 1
    if (timer >= 10000):     #added timer because hand lags and shrinks in start
        if (value >= xMax):
            value = xMax
            xMax += 0.5
        elif (value >= yMax):
            value = yMax
            yMax += 0.5
        elif (value <= xMin):
            value = xMin
            xMin -= 0.5
        elif (value <= yMin):
            value = yMin
            yMin -= 0.5


    range1 = tempMax - tempMin
    range2 = scaledMax - scaledMin
    if (range1 != 0):
        value = int((((value - tempMin)*range2)/range1)+scaledMin)
    else:
        value = int((((value - tempMin)*range2))+scaledMin)

    return value/2


def HandOverDevice():
    frame = controller.frame()
    return len(frame.hands) > 0


def HandCentered():
    frame = controller.frame() 
    centered = True
    hand = frame.hands[0]
    fingers = hand.fingers
    targetFinger = fingers[2]
    targetBone = targetFinger.bone(0) 
    targetJoint = targetBone.prev_joint
    xBaseJoint, yBaseJoint = Handle_Vector_From_Leap(targetJoint)
    if (xBaseJoint <= 0):
        centered = False
    if (xBaseJoint >= 300):
        centered = False
    if (yBaseJoint <= 0):
        centered = False
    if (yBaseJoint >= 300):
        centered = False
    return centered


def CenterData(X):
	allXCoordinates = X[0,::3]
	XmeanValue  = allXCoordinates.mean()
	X[0,::3] = allXCoordinates - XmeanValue

	allYCoordinates = X[0,1::3]
	YmeanValue  = allYCoordinates.mean()
	X[0,1::3] = allYCoordinates - YmeanValue

	allZCoordinates = X[0,2::3]
	ZmeanValue  = allZCoordinates.mean()
	X[0,2::3] = allZCoordinates - ZmeanValue

	return X


def Assign_Addition_Problem():
    first_num = random.randint(0,9)
    second_num = random.randint(0,9)
    
    # Check sum is 9 or below -> so it can be signed
    while first_num + second_num > 9:
        first_num = random.randint(0,9)
        second_num = random.randint(0,9)
        
    return first_num, second_num


def Assign_Subtraction_Problem():
    first_num = random.randint(0,9)
    second_num = random.randint(0,9)

    # Check difference is greater than 0 -> so it can be signed
    while first_num - second_num < 0:
        first_num = random.randint(0,9)
        second_num = random.randint(0,9)
        
    return first_num, second_num


def HandleState0(): # Hand not present
    global programState
    
    pygameWindow.Prepare()
    pygameWindow.Show_Help_Image()
    pygameWindow.Reveal()
    
    if HandOverDevice():
        programState = 1


def HandleState1():
    global programState, handCenteredTimer
    pygameWindow.Prepare() 
    frame = controller.frame()
    
    if (handCenteredTimer > 100):
            programState = 2
    hand = frame.hands[0]
    
    Handle_Frame(frame)
        
    fingers = hand.fingers
    targetFinger = fingers[2]
    targetBone = targetFinger.bone(0) # Middle Metacarpal
    targetJoint = targetBone.prev_joint

    xBase = targetJoint[0]
    yBase = targetJoint[1]
    zBase = targetJoint[2]

    

    if(yBase < 50):  
        pygameWindow.Hand_Too_Low() #ground
        timer = 0
    elif(yBase > 250): #ceiling
        pygameWindow.Hand_Too_High()
        timer = 0
    elif(xBase < -125):
        pygameWindow.Hand_Too_Left()
        timer = 0
    elif(xBase > 100):
        pygameWindow.Hand_Too_Right()
        timer = 0
    elif(zBase < -50):
        pygameWindow.Hand_Too_Forward()
        timer = 0
    elif(zBase > 150):
        pygameWindow.Hand_Too_Backward()
        timer = 0
        
    else:
        pygameWindow.Hand_Good_Work()
        handCenteredTimer += 1
                                            
    if HandOverDevice() == False:
        programState = 0
        handCenteredTimer = 0

    pygameWindow.Reveal()


def HandleState2():
    global BEST,BEST_AT,SECOND,SECOND_AT,THIRD,THIRD_AT, copy_data, User_Names, successfulDigitsSigned, num1, num2, pos_neg
    global level6timeLeftActual, level6timeleft, level6count, level4hintTimer, currentLevel, programState, digitToSign
    global testData, clf, signCorrect, randDigitTimer, handCenteredTimer, currDigitList, numIndex
    
    
    
    randDigitTimer += 1 # Time viewing random digit
    # MOD TIME TO MAKE TIMER MORE REALISTIC
    if (level6timeleft % 2 == 0):
        level6timeLeftActual -= 1
        
    level6timeleft -= 1
    
    database = pickle.load(open('userData/database.p', 'rb'))
    pygameWindow.Prepare() 
    if HandOverDevice(): 
        frame = controller.frame() 
        hand = frame.hands[0]
        Handle_Frame(frame)
        if (HandCentered() == False):
            handCenteredTimer = 0
            programState = 1

        currentLevel = 8############################################################
        
        # FOR LEVEL 4 + 5 MUST CHANGE TIME THE HINT IS ON THE SCREEN
        if currentLevel == 4 or currentLevel == 5 or currentLevel == 6 or currentLevel == 7 or currentLevel == 8:
            # IF ON LEVEL 4
            if currentLevel == 4:
                # Only show hint for a few seconds
                if level4hintTimer >= 8:
                    pygameWindow.Hide_Hint()
                else:
                    level4hintTimer += 1
                    #print("Incremented now: " +str(level4hintTimer))
                    pygameWindow.Show_ASL_Sign(digitToSign)
            elif currentLevel == 5 or currentLevel == 6 or currentLevel == 7 or currentLevel == 8:
                # NO HINT ON LEVEL 5, 6, 7, 8
                pygameWindow.Hide_Hint()
        else:
            pygameWindow.Show_ASL_Sign(digitToSign)

        # show digit unless level 7
        if currentLevel != 7 and currentLevel != 8:
            pygameWindow.Show_ASL_Digit(digitToSign)

        attemptsDict = 'digit' + str(digitToSign) + 'attempts'
        successesDict = 'digit' + str(digitToSign) + 'successes'

        # Get number of times user has been presented with digit
        userRecord = database[userName]
        try:
            numSeen = database[userName][attemptsDict]
        except:
            userRecord[attemptsDict] = 1
            numSeen = 1
                    
        # pygameWindow.Number_Of_Times_Digit_Signed(numSeen)

        # KNN
        k = 0
        for finger in range(5):
            finger = hand.fingers[finger]
            for b in range(4):
                if b == 0:
                    bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                elif b == 1:
                    bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                elif b == 2:
                    bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
                elif b == 3:
                    bone = finger.bone(Leap.Bone.TYPE_DISTAL)

                boneBase = bone.prev_joint
                boneTip = bone.next_joint

                xBase = boneBase[0]
                yBase = boneBase[1]
                zBase = boneBase[2]
                xTip  = boneTip[0]
                yTip  = boneTip[1]
                zTip  = boneTip[2]
                
                if ((b == 0)or(b == 3)):
                    testData[0, k] = xTip
                    testData[0, k+1] = yTip
                    testData[0, k+2] = zTip
                    k = k+3
        testData = CenterData(testData)
        predictedClass = clf.Predict(testData)
        
        if (predictedClass == digitToSign):
            signCorrect += 1
            pygameWindow.Warmer()
        else:
            signCorrect = 0
            pygameWindow.Colder()

        # Check if user passed 'level one' (digits 0 through 2)
        levelOnePass = False
        for digit in range(3):
            try:
                digitDict = 'digit' + str(digit) + 'successes'
                if (database[userName][digitDict] > 0):
                    levelOnePass = True
                else:
                    levelOnePass = False
                    break
            except:
                levelOnePass = False
                
        if (levelOnePass): # Increment number of digits to sign
            #print("Level two start!")
            currentLevel = 2
            currDigitList = [0, 1, 2, 3, 4, 5, 6]
            
        currentLevel = 8############################################################

        # Check if user passed 'level two' (digits 0 through 6)
        levelTwoPass = False
        for digit in range(3, 7):
            try:
                digitDict = 'digit' + str(digit) + 'successes'
                if (database[userName][digitDict] > 0):
                    levelTwoPass = True
                else:
                    levelTwoPass = False
                    break
            except:
                levelTwoPass = False
                
        if (levelTwoPass): # Increment number of digits to sign (all ten)
            levelTwoPass = False
            #print("Level three start!")
            currentLevel = 3
            currDigitList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        currentLevel = 8############################################################

        # Check if user passed 'level three' (digits 0 through 9)
        levelThreePass = False
        for digit in range(6, 10):
            try:
                digitDict = 'digit' + str(digit) + 'successes'
                if (database[userName][digitDict] > 0):
                    levelThreePass = True
                else:
                    levelThreePass = False
                    break
            except:
                levelThreePass = False
                
        if (levelThreePass): # Increment number of digits to sign (all ten)
            levelThreePass = False
            #print("Level three start!")
            currentLevel = 4

        currentLevel = 8############################################################

        # Check if user passed 'level four' (digits 0 through 9 with hint only shown for a few sec)
        levelFourPass = False
        for digit in range(6, 10):
            try:
                digitDict = 'digit' + str(digit) + 'successes'
                if (database[userName][digitDict] > 1): 
                    levelFourPass = True
                else:
                    levelFourPass = False
                    break
            except:
                levelFourPass = False
                
        if (levelFourPass): 
            levelFourPass = False
            #print("Level three start!")
            currentLevel = 5

        # Check if user passed 'level five' (digits 0 through 9 with no hint)
        levelFivePass = False
        try:
            digitDict = 'digit' + str(9) + 'successes'
            if database[userName][digitDict] >= 3:
                levelFivePass = True
            else:
                levelFivePass = False
        except:
            levelFivePass = False

        if (levelFivePass):
            levelFivePass = False
            currentLevel = 6

        currentLevel = 8############################################################

        if (currentLevel == 6):
            if (level6timeleft <= 0):
                level6timeleft = 0
            if (level6timeLeftActual <= 0):
                level6timeLeftActual = 0
            pygameWindow.Time_Remaining(level6timeLeftActual)
            level6count += 1
            if (randDigitTimer > 21): # Change digit and increment attempt if not signed correctly
                database[userName][attemptsDict] += 1 # Increment user attempt at digit 
                pickle.dump(database, open('userData/database.p', 'wb'))
                # Change digit 
                if (numIndex == len(currDigitList) - 1):
                    numIndex = 0
                else:
                    numIndex += 1
                level6timeleft = 20
                level6timeLeftActual = 11
                pygameWindow.Time_Up()
                successfulDigitsSigned -= 1
                digitToSign = currDigitList[numIndex]
                randDigitTimer = 0
                level4hintTimer = 0

        # CHECK IF USER HAS GONE THROUGH LEVEL 6 IF SO SHOW ADD PRACTICE
        levelSixComplete = False
        try:
            digitDict = 'digit' + str(9) + 'attempts' # TODO: EDIT SO IT GOES THROUHG AND REQUIRES DIGITS TO BE CORRECTLY
            if database[userName][digitDict] >= 6:      # SIGNED A CERTAIN AMOUNT INSTEAD OF SEEING 9 5 TIMES
                levelSixComplete = True
            else:
                levelSixComplete = False
        except:
            levelSixComplete = False

        if (levelSixComplete):
            levelSixComplete = False
            currentLevel = 7

        if currentLevel == 7:
            if (level6timeleft <= 0):
                level6timeleft = 0
            if (level6timeLeftActual <= 0):
                level6timeLeftActual = 0
            pygameWindow.Time_Remaining(level6timeLeftActual)
            level6count += 1

            if (randDigitTimer > 21): # Change digit and increment attempt if not signed correctly
                database[userName][attemptsDict] += 1 # Increment user attempt at digit 
                pickle.dump(database, open('userData/database.p', 'wb'))
                # Change digit 
                # whether or not user gets sum or subtraction prob
                pos_neg = random.randint(0,1)
                #SUM
                if pos_neg == 0:
                    num1, num2 = Assign_Addition_Problem()
                    digitToSign = (num1 + num2)
                # Difference
                if pos_neg == 1:
                    num1, num2 = Assign_Subtraction_Problem()
                    digitToSign = (num1 - num2)
                
                level6timeleft = 20
                level6timeLeftActual = 11
                pygameWindow.Time_Up()
                successfulDigitsSigned -= 1
                
                randDigitTimer = 0
                level4hintTimer = 0
                pygameWindow.Show_Equation(num1,num2,pos_neg)
            pygameWindow.Show_Equation(num1,num2,pos_neg)

        if currentLevel == 8:
            if (randDigitTimer > 21): # Change digit and increment attempt if not signed correctly
                database[userName][attemptsDict] += 1 # Increment user attempt at digit 
                pickle.dump(database, open('userData/database.p', 'wb'))
                # Change digit 
                # whether or not user gets sum or subtraction prob
                pos_neg = random.randint(0,1)
                #SUM
                if pos_neg == 0:
                    num1, num2 = Assign_Addition_Problem()
                    digitToSign = (num1 + num2)
                # Difference
                if pos_neg == 1:
                    num1, num2 = Assign_Subtraction_Problem()
                    digitToSign = (num1 - num2)
                
                level6timeleft = 20
                level6timeLeftActual = 11
                # pygameWindow.Time_Up()
                successfulDigitsSigned -= 1
                
                randDigitTimer = 0
                level4hintTimer = 0
                pygameWindow.Show_EquationLvl8(num1,num2,pos_neg)
            pygameWindow.Show_EquationLvl8(num1,num2,pos_neg)
            
        
        database[userName]['Current Level'] = currentLevel
        pygameWindow.Current_Level(currentLevel)

        
        #if (len(copy_data) > 2):         
            #pygameWindow.Level_Leaderboard(BEST,BEST_AT, SECOND,SECOND_AT, THIRD,THIRD_AT, User_Names)

        
        if (signCorrect >= 10): # User successfully signed digit (recognized by KNN 10 times)
            try:
                database[userName][successesDict] += 1
                successfulDigitsSigned += 1            # INTERIM 3 STUFF
            except:
                userRecord[successesDict] = 1
            
            database[userName][attemptsDict] += 1 # Increment user attempt at digit
            pickle.dump(database, open('userData/database.p', 'wb'))
            randDigitTimer = 0
            # Change digit
            if (currentLevel != 7 and currentLevel != 8):
                if (numIndex == len(currDigitList) - 1):
                    numIndex = 0
                else:
                    numIndex += 1
                digitToSign = currDigitList[numIndex]
                
            else:
                # whether or not user gets sum or subtraction prob
                pos_neg = random.randint(0,1)
                #SUM
                if pos_neg == 0:
                    num1, num2 = Assign_Addition_Problem()
                    digitToSign = (num1 + num2)
                # Difference
                if pos_neg == 1:
                    num1, num2 = Assign_Subtraction_Problem()
                    digitToSign = (num1 - num2)
                    
            programState = 3
            
        print(digitToSign)      
        # pygameWindow.Success_Timeline(successfulDigitsSigned) 
    else:
        programState = 0
        
    pygameWindow.Reveal()


def HandleState3(): # To show 'success' check mark when user correctly signs digit 
    global level6timeLeftActual, level6timeleft, level6count, level4hintTimer, programState, randNum, greenCheckTimer, numIndex, levelOneNums
    level6timeleft = 20
    level6timeLeftActual = 11
    
    level6count = 0
    level4hintTimer = 0
    greenCheckTimer += 1
    pygameWindow.Prepare()
    frame = controller.frame()
    Handle_Frame(frame)
    
    pygameWindow.Digit_Good()
    
    if HandOverDevice():
        if HandCentered():
            if (greenCheckTimer > 100):
                programState = 2
                greenCheckTimer = 0
        else:
            programState = 1
            greenCheckTimer = 0
    else:
        programState = 0
        greenCheckTimer = 0
    pygameWindow.Reveal()

    
while True:
    if programState == 0:
        HandleState0()
    elif programState == 1:
        HandleState1()
    elif programState == 2:
        HandleState2()
    elif programState == 3:
        HandleState3()

    
    

