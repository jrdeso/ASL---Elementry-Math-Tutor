from constants import CONSTANTS
import pygame
import time
class PYGAME_WINDOW:
    def __init__(self):
        constants = CONSTANTS()
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))
        
    def Prepare(self):
        self.screen.fill((255, 255, 255))

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self,x,y):
        pygame.draw.circle(self.screen,(0,0,0),(x,y),15)

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, fingerWidth):    
        pygame.draw.line(self.screen,(0,0,0),(xBase,yBase),(xTip,yTip),fingerWidth)
    
    def Show_Help_Image(self):
        ## DEL 7 image
        ## helpful image to be shown to make them put hand over
        handImage = pygame.image.load('images/help_image.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))
        
    def Hand_Too_Low(self):
        handImage = pygame.image.load('images/toolow.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))
        
    def Hand_Too_High(self):
        handImage = pygame.image.load('images/toohigh.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))

    def Hand_Too_Left(self):
        handImage = pygame.image.load('images/tooleft.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))

    def Hand_Too_Right(self):
        handImage = pygame.image.load('images/tooright.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))

    def Hand_Too_Forward(self):
        handImage = pygame.image.load('images/tooforward.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))

    def Hand_Too_Backward(self):
        handImage = pygame.image.load('images/tooback.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))
        
    def Hand_Good_Work(self):
        handImage = pygame.image.load('images/goodwork.jpg')
        handImage = pygame.transform.scale(handImage,(300,300))
        self.screen.blit(handImage,(300,0))
        
    def Digit_Good(self):
        DigitGood = pygame.image.load('images/digitgood.jpg')
        DigitGood = pygame.transform.scale(DigitGood,(300,300))
        self.screen.blit(DigitGood,(300,0))

##################ASL IMAGES##############################
    def Hide_Hint(self):
        DigitGood = pygame.image.load('images/white.jpg')
        DigitGood = pygame.transform.scale(DigitGood,(300,300))
        self.screen.blit(DigitGood,(300,300))
    
    def Show_ASL_Sign(self, mode):
        if mode == 0:
            pic = pygame.image.load('images/ASLZero.jpg')
        elif mode == 1:
            pic = pygame.image.load('images/ASLOne.jpg')
        elif mode == 2:
            pic = pygame.image.load('images/ASLTwo.jpg')
        elif mode == 3:
            pic = pygame.image.load('images/ASLThree.jpg')
        elif mode == 4:
            pic = pygame.image.load('images/ASLFour.jpg')
        elif mode == 5:
            pic = pygame.image.load('images/ASLFive.jpg')
        elif mode == 6:
            pic = pygame.image.load('images/ASLSix.jpg')
        elif mode == 7:
            pic = pygame.image.load('images/ASLSeven.jpg')
        elif mode == 8:
            pic = pygame.image.load('images/ASLEight.jpg')
        else:
            pic = pygame.image.load('images/ASLNine.jpg')
            
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (300,300))
            
    def Show_ASL_Digit(self, mode):
        if mode == 0:
            pic = pygame.image.load('images/zero.jpg')
        elif mode == 1:
            pic = pygame.image.load('images/one.jpg')
        elif mode == 2:
            pic = pygame.image.load('images/two.jpg')
        elif mode == 3:
            pic = pygame.image.load('images/three.jpg')
        elif mode == 4:
            pic = pygame.image.load('images/four.jpg')
        elif mode == 5:
            pic = pygame.image.load('images/five.jpg')
        elif mode == 6:
            pic = pygame.image.load('images/six.jpg')
        elif mode == 7:
            pic = pygame.image.load('images/seven.jpg')
        elif mode == 8:
            pic = pygame.image.load('images/eight.jpg')
        else:
            pic = pygame.image.load('images/nine.jpg')
            
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (300,0))

    def Warmer(self):
        pic = pygame.image.load('images/warmer.jpg')
            
        pic = pygame.transform.scale(pic, (100,100))
        self.screen.blit(pic, (300,250))

    def Colder(self):
        pic = pygame.image.load('images/Colder.jpg')
            
        pic = pygame.transform.scale(pic, (100,100))
        self.screen.blit(pic, (300,250))

    def Level_Leaderboard(self, first,firstIndex, second,secondIndex, third,thirdIndex, User_Names):
        font = pygame.font.Font('freesansbold.ttf', 12)

        RED = (255,0,0)
        BLUE = (0,0,255)
        GREEN = (0,255,0)

        lvlPrac = (105, 320)
        lvl7 = (105, 350)
        lvl6 = (105, 380)
        lvl5 = (105, 410)
        lvl4 = (105, 440)
        lvl3 = (105, 470)
        lvl2 = (105, 500)
        lvl1 = (105, 530)
        
        firstSpot = font.render("o", True, RED)
        if first == 1:
            self.screen.blit(firstSpot, (lvl1))
        if first == 2:
            self.screen.blit(firstSpot, (lvl2))
        if first == 3:
            self.screen.blit(firstSpot, (lvl3))
        if first == 4:
            self.screen.blit(firstSpot, (lvl4))
        if first == 5:
            self.screen.blit(firstSpot, (lvl5))
        if first == 6:
            self.screen.blit(firstSpot, (lvl6))
        if first == 7:
            self.screen.blit(firstSpot, (lvl7))
        if first == 8:
            self.screen.blit(firstSpot, (lvlPrac))
            
        secondSpot = font.render("o", True, BLUE)
        if second == 1:
            self.screen.blit(secondSpot, (lvl1))
        if second == 2:
            self.screen.blit(secondSpot, (lvl2))
        if second == 3:
            self.screen.blit(secondSpot, (lvl3))
        if second == 4:
            self.screen.blit(secondSpot, (lvl4))
        if second == 5:
            self.screen.blit(secondSpot, (lvl5))
        if second == 6:
            self.screen.blit(secondSpot, (lvl6))
        if second == 7:
            self.screen.blit(secondSpot, (lvl7))
        if second == 8:
            self.screen.blit(secondSpot, (lvlPrac))

        thirdSpot = font.render("o", True, GREEN)
        if third == 1:
            self.screen.blit(thirdSpot, (lvl1))
        if third == 2:
            self.screen.blit(thirdSpot, (lvl2))
        if third == 3:
            self.screen.blit(thirdSpot, (lvl3))
        if third == 4:
            self.screen.blit(thirdSpot, (lvl4))
        if third == 5:
            self.screen.blit(thirdSpot, (lvl5))
        if third == 6:
            self.screen.blit(thirdSpot, (lvl6))
        if third == 7:
            self.screen.blit(thirdSpot, (lvl7))
        if third == 8:
            self.screen.blit(thirdSpot, (lvlPrac))
        
        description = font.render("TOP THREE:", True, (0, 0, 0))
        bestUser = font.render(str(User_Names[firstIndex]), True, RED)
        secondUser = font.render(str(User_Names[secondIndex]), True, BLUE)
        thirdUser = font.render(str(User_Names[thirdIndex]), True, GREEN)

        # SHOW USERS
        self.screen.blit(description, (15, 560))
        self.screen.blit(bestUser, (15, 580))
        self.screen.blit(secondUser, (95, 580))
        self.screen.blit(thirdUser, (205, 580))
        

    def Success_Timeline(self, numSuccesses):
        successTimeline = pygame.image.load('images/successtimeline.jpg')
        successTimeline = pygame.transform.scale(successTimeline,(240,95))
        # Show timeline
        self.screen.blit(successTimeline, (115,410))
        numSuccesses *= 5 # increment successes to show movement better
        # show successes as "|" moving across line
        if numSuccesses >= 160:
            numSuccesses = 160
        font = pygame.font.Font('freesansbold.ttf', 22)
        text = font.render("|", True, (255, 0, 0))
        self.screen.blit(text, (125+numSuccesses, 445))


    def Show_Equation(self, num1, num2, pos_neg):
        font = pygame.font.Font('freesansbold.ttf', 40)
        
        # sum
        if pos_neg == 0:
            eqn = font.render(str(num1) + " + " + str(num2) + " = ?", True, (0, 0, 0))
        elif pos_neg == 1:
            eqn = font.render(str(num1) + " - " + str(num2) + " = ?", True, (0, 0, 0))
        
        self.screen.blit(eqn, (350, 150))

    def Show_EquationLvl8(self, num1, num2, pos_neg):
        font = pygame.font.Font('freesansbold.ttf', 40)
        #GET PIC 1
        if num1 == 0:
            pic1 = pygame.image.load('images/ASLZero.jpg')
        elif num1 == 1:
            pic1 = pygame.image.load('images/ASLOne.jpg')
        elif num1 == 2:
            pic1 = pygame.image.load('images/ASLTwo.jpg')
        elif num1 == 3:
            pic1 = pygame.image.load('images/ASLThree.jpg')
        elif num1 == 4:
            pic1 = pygame.image.load('images/ASLFour.jpg')
        elif num1 == 5:
            pic1 = pygame.image.load('images/ASLFive.jpg')
        elif num1 == 6:
            pic1 = pygame.image.load('images/ASLSix.jpg')
        elif num1 == 7:
            pic1 = pygame.image.load('images/ASLSeven.jpg')
        elif num1 == 8:
            pic1 = pygame.image.load('images/ASLEight.jpg')
        else:
            pic1 = pygame.image.load('images/ASLNine.jpg')
        # GET PIC 2
        if num2 == 0:
            pic2 = pygame.image.load('images/ASLZero.jpg')
        elif num2 == 1:
            pic2 = pygame.image.load('images/ASLOne.jpg')
        elif num2 == 2:
            pic2 = pygame.image.load('images/ASLTwo.jpg')
        elif num2 == 3:
            pic2 = pygame.image.load('images/ASLThree.jpg')
        elif num2 == 4:
            pic2 = pygame.image.load('images/ASLFour.jpg')
        elif num2 == 5:
            pic2 = pygame.image.load('images/ASLFive.jpg')
        elif num2 == 6:
            pic2 = pygame.image.load('images/ASLSix.jpg')
        elif num2 == 7:
            pic2 = pygame.image.load('images/ASLSeven.jpg')
        elif num2 == 8:
            pic2 = pygame.image.load('images/ASLEight.jpg')
        else:
            pic2 = pygame.image.load('images/ASLNine.jpg')

        # display eqn
        if pos_neg == 0:
            eqnSign = font.render(" + ", True, (0, 0, 0))
        elif pos_neg == 1:
            eqnSign = font.render(" - ", True, (0, 0, 0))
            
        question = font.render(" = ?", True, (0, 0, 0))

        # ADJUST BLIT TO SHOW PROPERLY
        #PIC 1
        pic1 = pygame.transform.scale(pic1, (110,110))
        # pic 2
        pic2 = pygame.transform.scale(pic2, (110,110))
        
        self.screen.blit(pic1, (250, 100))
        self.screen.blit(eqnSign, (360, 130))
        self.screen.blit(pic2, (400, 100))
        self.screen.blit(question, (510, 130))
        

    def Number_Of_Times_Digit_Signed(self, number):
        # Digit (# seen) visual
        font = pygame.font.Font('freesansbold.ttf', 16)
        if number == 1:
            text = font.render("1st time seeing this number. ", True, (0, 0, 0))
        elif number == 2:
            text = font.render("2nd time seeing this number. ", True, (0, 0, 0))
        elif number == 3:
            text = font.render("3rd time seeing this number. ", True, (0, 0, 0))
        else:
            text = font.render(str(number) + "th time seeing this number. ", True, (0, 0, 0))
        self.screen.blit(text, (115, 390))

    def Current_Level(self, levelNumber):
        font = pygame.font.Font('freesansbold.ttf', 16)
        ## Replaced with level graphic
        #levelText = font.render("You're on level: " + str(levelNumber) + "!", True, (0, 255, 0))
        levelNumber = 7
        # SHOW THEIR TASK
        if levelNumber == 1:
            levelpic = pygame.image.load('images/lvl1prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("Digits: 0,1,2", True, (0, 0, 0))
            taskText2 = font.render("", True, (0, 0, 0))
            taskText3 = font.render("", True, (0, 0, 0))
        elif levelNumber == 2:
            levelpic = pygame.image.load('images/lvl2prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("Continue: 0,1,2", True, (0, 0, 0))
            taskText2 = font.render("New: 3,4,5,6", True, (0, 0, 0))
            taskText3 = font.render("", True, (0, 0, 0))
        elif levelNumber == 3:
            levelpic = pygame.image.load('images/lvl3prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("Continue: 0,1,2,3,4,5,6", True, (0, 0, 0))
            taskText2 = font.render("New: 7,8,9", True, (0, 0, 0))
            taskText3 = font.render("", True, (0, 0, 0))
        elif levelNumber == 4:
            levelpic = pygame.image.load('images/lvl4prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("Now your hint is temporary", True, (0, 0, 0))
            taskText2 = font.render("Good Luck!", True, (0, 0, 0))
            taskText3 = font.render("", True, (0, 0, 0))
        elif levelNumber == 5:
            levelpic = pygame.image.load('images/lvl5prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("No more hints!", True, (0, 0, 0))
            taskText2 = font.render("Good Luck!", True, (0, 0, 0))
            taskText3 = font.render("", True, (0, 0, 0))
        elif levelNumber == 6:
            levelpic = pygame.image.load('images/lvl6prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("You have 10 seconds", True, (0, 0, 0))
            taskText2 = font.render("to sign each digit!", True, (0, 0, 0))
            taskText3 = font.render("Good Luck!", True, (0, 0, 0))
        elif levelNumber == 7:
            levelpic = pygame.image.load('images/lvl7prog.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("You have 10 seconds", True, (0, 0, 0))
            taskText2 = font.render("to solve the equation!", True, (0, 0, 0))
            taskText3 = font.render("Good Luck!", True, (0, 0, 0))
        elif levelNumber == 8:
            levelpic = pygame.image.load('images/lvladdprac.jpg')
            levelpic = pygame.transform.scale(levelpic,(100,240))
            taskText1 = font.render("Additional timed", True, (0, 0, 0))
            taskText2 = font.render("practice!", True, (0, 0, 0))
            taskText3 = font.render("Thanks for learning!", True, (0, 0, 0))

        self.screen.blit(levelpic, (5,310)) 
        self.screen.blit(taskText1, (115,310))
        self.screen.blit(taskText2, (115,330))
        self.screen.blit(taskText3, (115,350))

    def Time_Remaining(self, time):
        font = pygame.font.Font('freesansbold.ttf', 16)
        timeLeft = font.render(str(time) + " seconds left! " , True, (255, 0, 0))
        self.screen.blit(timeLeft, (115,370))

    def Time_Up(self):
        time_up = pygame.image.load('images/time_up.jpg')
        time_up = pygame.transform.scale(time_up,(300,300))
        self.screen.blit(time_up,(300,0))    
            
    def Draw_Never(self):
        pic =  pygame.image.load('images/never.PNG')
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (0,300))
    
    def Draw_First(self):
        pic =  pygame.image.load('images/first.PNG')
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (0,300))
        
    def Draw_Second(self):
        pic =  pygame.image.load('images/second.PNG')
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (0,300))

    def Draw_Third(self):
        pic =  pygame.image.load('images/third.PNG')
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (0,300))
    def Draw_More(self):
        pic =  pygame.image.load('images/more.PNG')
        pic = pygame.transform.scale(pic, (300,300))
        self.screen.blit(pic, (0,300))
