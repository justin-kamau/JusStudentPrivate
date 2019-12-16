from tkinter import *
from tkinter.messagebox import *
from validation import*
from tkinter import ttk
import time
from tkinter import ttk, messagebox
import csv
from tkinter.simpledialog import*

class MathGame(Frame):
    def __init__(self,master):
        
        super(MathGame,self).__init__(master)
        
        self.grid()
        #creating menu frame
        self.menuFrame = Frame(self)
        self.multiplicationFrame=Frame(self)
        self.ParentsReport =Frame(self)
        self.DetailedReportScreenFrame=Frame(self)
        #self.additionFrame=Frame(self)
        
        #method create widets to go on the frame
        self.HScore = 0
        self.QNumber = 1
        self.UserName = askstring("User Name","Whats your name?")
        self.create_menu_widgets()
        self.create_multiplicationWidgets()
        #self.create_subtractionWidgets()
        #self.create_additionWidgets()
        #self.create_divisionWidgets()
    #gridding the menu framw
        self.menuFrame.config(width=1000,height = 600)
        self.menuFrame.grid()
    def HintButton(self,WhichFrame,first_number):
        x = self.QOne
        if WhichFrame == "M":
            if x == 2:
                showinfo("TWO TABLE HELP" ,"add the number to itself in other words, double it, FOR Example 2×9 = 9+9 = 18")
            elif x == 4:
                showinfo("FOUR TABLE HELP","double, then double again, FOR Example 4×9: double 9 is 18, double 18 is 36")
            elif x == 5:
                showinfo("FIVE TABLE HELP" ,"The last digit goes 5, 0, 5, 0, ... like this: 5, 10, 15, 20, ...")
            elif x == 6:
                showinfo("SIX TABLE HELP" ,"When you multiply 6 by an even number, they both end in the same digit, FOR Examples: 6×2=12, 6×4=24, 6×6=36")
            elif x == 7 and x == 8:
                showinfo("Seven and Eight TABLE HELP","Think ""5,6,7,8"": 56=7×8")
            elif x == 9:
                showinfo("Nine TABLE HELP" ,"double, then double again, FOR Example 4×9: double 9 is 18, double 18 is 36")
            else:
                showinfo("TIMES TABLE HELP", "Try making a song to help you learn these times tables better")
        elif WhichFrame == "S":
            showinfo("SUBTRACTION HELP","If the question is too difficult try splitting it up.")
        elif WhichFrame == "D":
            showinfo("DIVISION HELP","Try usong long division.")
        else:
            showinfo("ADDITION HELP","When a number is close to ten we can borrow from the other number so it reaches ten FOR Example: 9 + 79 is only 1 away from 10",)
            
    def SubmitAnswer(self,QOne,QTwo,UserAnswer,lblresult,WhichFrame,lblHScore,WHealth,lblWHealth): 
        
        #lblresult.config(text="")
        print("Worked Submit button")
        ValidCalcalulation(UserAnswer)
        x = int(self.QOne)
        y = int(self.QTwo)
        
        z = int(UserAnswer.get())
        print(x,y,z)
     
        
        if WhichFrame == "M":
            QAns = x * y
        elif WhichFrame =="A":
            QAns = x + y
        elif WhichFrame == "S":
            QAns = x - y
        else:
            QAns = x/y
        if z == QAns:
            lblresult.config(text ="Well done",font=["Arial",20],bg="white")
            self.HScore = self.HScore + 1
            lblHScore.config(text= "Score: "+ str(self.HScore),font=["Arial",20],bg="white")
            WHealth = WHealth + 100
            lblWHealth.config(text = "Wall Health is: " + str(WHealth),bg="white")
            Question = "Correct"
        else:
            lblresult.config(text="Try again!",font=["Arial",20],bg="white")
            Question = "Wrong"
            WHealth = WHealth - 100
            print(WHealth)
            lblWHealth.config(text = "Wall Health is: " + str(WHealth),bg="white")
        if z != "":
            self.SaveQuestions(x,y,z,WhichFrame,Question)
        if WHealth == 600:
            WHealth = 500
            lblWHealth.config(text = "Wall Health is: " + str(WHealth),bg="white")
        #root.after(1000, root)
        

        
    def Save(self,UserAnswer):
        ValidSave(self.QNumber)
        LeaderboardFile = open("Leaderboard.txt","a")
        print(self.UserName,self.QNumber,self.HScore,file=LeaderboardFile, sep=",")
        LeaderboardFile.close()
    def SaveQuestions(self,x,y,z,WhichFrame,Question):
        count = 0
        str(x)
        str(y)
        print(z)
        #x is the first number
        #y is the second
        #z is user entry
        if WhichFrame == "M":
            Operation = "X"
        elif WhichFrame == "A":
            Operation = "+"
        elif WhichFrame == "D":
            Operation = "/"
        elif WhichFrame == "S":
            Operation = "-"
        else:
            print("FAILED")
        
        
        ReportFile = open("Report.txt","a")
        print(self.UserName,Question,x,Operation,y,z,file=ReportFile, sep=",")
        ReportFile.close()
        count = count + 1
    def ShowScore(self):
        LeaderboardFile = open("Leaderboard.txt","a")
        csv_reader = csv.DictReader(LeaderboardFile)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'mColumn names are {", ".join(row)}')
                line_count += 1
            line_count += 1
        LeaderboardFile.close()
    def NextQuestion(self,QOne,QTwo,UserAnswer,lblresult,WFrame,Question,lblQNumber):
        lblresult.config(text="",bg="white")
        import random
        
        self.multiplicationFrame.grid_remove()
        self.QNumber = self.QNumber + 1
        lblQNumber.config(text="Question: " +str(self.QNumber),font=["Arial",20],bg="white")
        print("next q")
        if WFrame == "M":
            self.multiplicationFrame.grid()
            self.QOne = random.randint(1,12)
            self.QTwo = random.randint(1,12)
        elif WFrame == "A":
            self.multiplicationFrame.grid()
            self.QOne = random.randint(10,100)
            self.QTwo = random.randint(10,100)
        elif WFrame == "D":
            self.multiplicationFrame.grid()
            self.QOne = random.randint(1,99)
            self.QTwo = random.randint(1,99)
            while self.QOne % self.QTwo != 0 and self.QOne != self.QTwo:
                print("not this time")
                self.QOne = random.randint(1,99)
                self.QTwo = random.randint(1,99)
        else:
            self.multiplicationFrame.grid()
            self.QOne = random.randint(1,99)
            self.QTwo = random.randint(1,99)
            while self.QTwo > self.QOne:
                print("not this time")
                self.QOne = random.randint(1,99)
                self.QTwo = random.randint(1,99)


        if WFrame == "M":
            Operator = "X"
        elif WFrame == "A":
            Operator = "+"
        elif WFrame == "S":
            Operator = "-"
        elif WFrame == "D":
            Operator = "/"
        else:
            print("Failed")
        Question.config(text=str(self.QOne) + "   " + Operator +"   " + str(self.QTwo)+ "   " ,width=10 , font=["Arial",20],bg="white")
        
        
        
        #second_number.config(text =str(QTwo))
        #operation.config(text = "X")
        UserAnswer.delete(0,END)
        
        
        
        #first_number.grid(row=1,column=1)
        #second_number.grid(row=1,column=3)
        #operation.grid(row=1,column=2)
        #UserAnswer.grid(row=1,column=4)
        
    
    def create_multiplicationWidgets(self):
        import random
    
    
        
    def goToMultiplicationScreen(self,WhichFrame):
        print("Gone to multiplications screen")
        self.menuFrame.grid_remove()
        self.multiplicationFrame.grid()
        print("frame is" +WhichFrame)
        import random
        self.multiplicationFrame.config(height=1000,width=1000,bg="white")
        #create the buttons and label in the menu Frame
        self.canvas=Canvas(self.multiplicationFrame,height=800,width=800,bg="white")
        lblTitle = Label(self.multiplicationFrame,text="Multiplication")
        #lblTitle.grid(row=0,column=0)
        #CANVASS SECTION        123             123     123     123     123     123         123         123         123         123
        self.canvas.grid(row=0,column=0,columnspan=6)
        self.brickIMG = PhotoImage(file="brickCARTOON.gif")
        #COUNTER AND ARRAY 
        self.canvas.create_image(400,750,image=self.brickIMG,tag="brick")
        self.canvas.create_image(400,700,image=self.brickIMG,tag="brick")
        
        
        
            
         
        #self.FireBlastImage = PhotoImage(file="FireBlast.gif")
        
        #self.canvas.create_image(x,y,image=self)

        self.DragonImage = PhotoImage(file="Dragon.gif")
        self.canvas.create_image(100,500,image=self.DragonImage,tag="Dragon")
        #END OF CANVAS                                                                   123         123             123         123
    
        btnBack = Button(self.multiplicationFrame,text="Back",command=lambda:self.goToMenu(lblresult))
        #self.QOne = random.randint(1,12)
        #self.QTwo = random.randint(1,12)
        if WhichFrame == "M":
            Operation = "X"
        elif WhichFrame == "A":
            Operation = "+"
        elif WhichFrame == "D":
            Operation = "/"
        elif WhichFrame == "S":
            Operation = "-"
        else:
            print("FAILED")
        if WhichFrame == "M":
            self.multiplicationFrame.grid()
            self.QOne = random.randint(1,12)
            self.QTwo = random.randint(1,12)
        elif WhichFrame == "A":
            self.multiplicationFrame.grid()
            self.QOne = random.randint(10,100)
            self.QTwo = random.randint(10,100)
        elif WhichFrame == "D":
            self.multiplicationFrame.grid()
            self.QOne = random.randint(1,99)
            self.QTwo = random.randint(1,99)
            while self.QOne % self.QTwo != 0 and self.QOne != self.QTwo:
                print("not this time")
                self.QOne = random.randint(1,99)
                self.QTwo = random.randint(1,99)
        else:
            self.multiplicationFrame.grid()
            self.QOne = random.randint(1,99)
            self.QTwo = random.randint(1,99)
            while self.QTwo > self.QOne:
                print("not this time")
                self.QOne = random.randint(1,99)
                self.QTwo = random.randint(1,99)

        Question = Label(self.multiplicationFrame,text = str(self.QOne) + "   " + Operation +"   " + str(self.QTwo)+ "   " ,width=10 , font=["Arial",20],bg="white")
        #second_number = Label(self.multiplicationFrame,text = str(QTwo),width= 2 , font=["Arial",20])
        #operation = Label(self.multiplicationFrame,text = "X",width=2 , font=["Arial",20])
        WHealth = 500
        lblWHealth = Label(self.multiplicationFrame,text = "Wall Health is: " + str(WHealth),bg="white")
        UserAnswer= Entry(self.multiplicationFrame,width= 10, font=["Arial",20])
        QAns = self.QOne * self.QTwo
        
        
        Question.grid(row=1,column=1,sticky=E)
        lblWHealth.grid(row=1,column=0)
        #second_number.grid(row=1,column=3)
        #operation.grid(row=1,column=2)
        UserAnswer.grid(row=1,column=4)
        lblHScore = Label(self.multiplicationFrame, text= "Score: "+ str(self.HScore),font=["Arial",20],bg="white")
        lblQNumber = Label(self.multiplicationFrame,text="Question: " +str(self.QNumber),font=["Arial",20],bg="white")
        
        ##Submit Button
        lblHScore.grid(row=0,column =6)
        lblQNumber.grid(row=0,column=7)
        WFrame = WhichFrame
        btnSubmit = Button(self.multiplicationFrame,text="Submit",command=lambda:self.SubmitAnswer(self.QOne,self.QTwo,UserAnswer,lblresult,WhichFrame,lblHScore,WHealth,lblWHealth))
        lblresult = Label(self.multiplicationFrame,text="",font=["Arial",20],bg="white")
        lblresult.grid(row=2,column=3)
        btnNextQ = Button(self.multiplicationFrame,text="Next Question",command=lambda:self.NextQuestion(self.QOne,self.QTwo,UserAnswer,lblresult,WFrame,Question,lblQNumber))
        btnSave = Button(self.multiplicationFrame,text="Save",command=lambda:self.Save(UserAnswer))

        btnHint = Button(self.multiplicationFrame,text="Hint (Only use if you REALLY need help)",command=lambda:self.HintButton(WhichFrame,self.QOne))
        btnHint.grid(row=2,column=6)
        btnSubmit.grid(row=1,column=5)
        btnBack.grid(row=2,column = 5)
        btnNextQ.grid(row=1,column=6)
        btnSave.grid(row=1,column=7)

    
        
        
        
    def goToSubtractionScreen(self):
        print("Gone to subtractions screen")
        self.menuFrame.grid_remove()
        self.subtractionFrame.grid()
        
    def goToAdditionScreen(self):
        self.menuFrame.grid_remove()
        self.additionFrame.grid()
    def goToDivisionScreen(self):
        print("Division")
        self.menuFrame.grid_remove()
        self.divisionFrame.grid()
    def goToMenu(self,lblresult,lblQuestion):
        if lblresult != "":
            lblresult.config(text="",bg="white")
            

        self.multiplicationFrame.grid_remove()
        self.ParentsReport.grid_remove()
        self.DetailedReportScreenFrame.grid_remove()
        #self.divisionFrame.grid_remove()
        self.menuFrame.grid()
    def ParentsReports(self,WhichFrame):
        self.multiplicationFrame.grid_remove()
        self.menuFrame.grid_remove()
        self.ParentsReport.grid()
        IncorrectList =  []
        ChildsName = ""
        ChildsName =askstring("Parents Report","Whats your childs name?")
        lblTitle = Label(self.ParentsReport,text="PARENTS REPORT",font=["Arial",20],bg="white")
        self.ParentsReport.config(height=1000,width=1000,bg="white")
        lblChildsName= Label(self.ParentsReport,text = str(ChildsName))
        with open('Report.txt') as ReportFile:
            csv_reader = csv.reader(ReportFile, delimiter=',')
            line_count = 0
            count = 0
            AnsWrong = 0
            AnsCorrect = 0
            for row in csv_reader:
                    count = count + 1
                    if row[1]== "Wrong":
                        AnsWrong = AnsWrong + 1
                        a = row[2]
                        b = row[3]
                        c = row[4]
                        IncorrectList.append(a)
                        IncorrectList.append(b)
                        IncorrectList.append(c)
                    if row[1]=="Correct":
                        AnsCorrect = AnsCorrect + 1
            print(IncorrectList)
        MWrong = IncorrectList.count('X')
        AWrong = IncorrectList.count('+') 
        SWrong = IncorrectList.count('-') 
        DWrong = IncorrectList.count('/')
        print(MWrong)
        
        ReportFile.close()
        lblQAnswered = Label(self.ParentsReport,text="Your child has answered a total of " +str(count)+" Questions",font=["Arial",15],bg="white" )
        lblCorrectRatio = Label(self.ParentsReport,text= " "+str(AnsCorrect) + " correct and "+str(AnsWrong)+" incorrect answers.",font=["Arial",15],bg="white")
        lblOWrong = Label(self.ParentsReport,text=str(ChildsName) + " has got these type of questions qrong as follows: ",font=["Arial",15],bg="white") 
        lblWrong = Label(self.ParentsReport,text="Multiplication: "+str(MWrong) + "    Addition "+str(AWrong)+ "    Subtraction "+str(SWrong) + "    Dvivision "+str(DWrong),font=["Arial",15],bg="white")
        lblDirect = Label(self.ParentsReport,text="To see the full detailed questions they got wrong press any of the buttons to see  where they went wrong",font=["Arial",15],bg="white")

        btnMultiplication = Button(self.ParentsReport,text = "Detailed Screen",font=["Arial",10],bg="white",command=lambda: self.DetailedReportScreen("M",IncorrectList))
     
      
        lblTitle.grid(row=0,column=0)
        lblQAnswered.grid(row=1,column=0)
        lblCorrectRatio.grid(row=1,column=1)
        lblOWrong.grid(row=2,column = 0)
        lblWrong.grid(row = 3,column = 0)
        lblDirect.grid(row=4,column = 0)

        btnMultiplication.grid(row=5,column=0)
       
        
        self.ParentsReport.config(height=1000,width=1000,bg="WHITE")
        lblresult = ""
        btnBack = Button(self.ParentsReport,text="Back",command=lambda:self.goToMenu(lblresult))
        btnBack.grid(row=2,column=2)
    def DetailedReportScreen(self,WhichFrame,IncorrectList):
        count = 0
        self.multiplicationFrame.grid_remove()
        self.menuFrame.grid_remove()
        
        self.ParentsReport.grid_remove()
        
        self.DetailedReportScreenFrame.grid()
        
        lblTitle = Label(self.DetailedReportScreenFrame,text="Your child has got the following questions wrong",font=["Arial",20],bg="white")
        self.DetailedReportScreenFrame.config(height=1000,width=1000,bg="white")
        LengthOfList = len(IncorrectList)
        i = 1

        
        
           

        
        for Item in IncorrectList:
            count = 1
            print(Item)
            if Item == "X":
                
                z = str(i)
                QOne = IncorrectList[i-2]
                print("q one is " + QOne)
                Operator = IncorrectList[i]
                if count >= LengthOfList:
                    QTwo = "Done"
                else:
                    QTwo = IncorrectList[i]
            
                Question = str(QOne) + " " + str(Item) + " " + str(QTwo)
                lblQuestion = Label(self.DetailedReportScreenFrame,text=Question,font=["Arial",20],bg="white")
                lblQuestion.grid(row=i,column=0)
            elif Item == "+":
                
                z = str(i)
                QOne = IncorrectList[i-2]
                print("q one is " + QOne)
                Operator = IncorrectList[i]
                if count >= LengthOfList:
                    QTwo = "Done"
                else:
                    QTwo = IncorrectList[i]
        
                Question = str(QOne) + " " + str(Item) + " " + str(QTwo)
                lblQuestion = Label(self.DetailedReportScreenFrame,text=Question,font=["Arial",20],bg="white")
                lblQuestion.grid(row=i,column=0)
            elif Item == "-":
                
                z = str(i)
                QOne = IncorrectList[i-2]
                print("q one is " + QOne)
                Operator = IncorrectList[i]
                if count >= LengthOfList:
                    QTwo = "Done"
                else:
                    QTwo = IncorrectList[i]
              
                Question = str(QOne) + " " + str(Item) + " " + str(QTwo)
                lblQuestion = Label(self.DetailedReportScreenFrame,text=Question,font=["Arial",20],bg="white")
                lblQuestion.grid(row=i,column=0)
            elif Item == "/":
                
                z = str(i)
                QOne = IncorrectList[i-2]
                print("q one is " + QOne)
                Operator = IncorrectList[i]
                if count >= LengthOfList:
                    QTwo = "Done"
                else:
                    QTwo = IncorrectList[i]
         
                Question = str(QOne) + " " + str(Item) + " " + str(QTwo)
                lblQuestion = Label(self.DetailedReportScreenFrame,text=Question,font=["Arial",20],bg="white")
                lblQuestion.grid(row=i,column=0)
            else:
                 print("FAILED")
            i = i + 1
        lblresult = ""
        btnBack = Button(self.DetailedReportScreenFrame,text="Back",command=lambda:self.goToMenu(lblresult,lblQuestion))
        btnBack.grid(row=2,column=2)
        lblTitle.grid(row=0,column=0)

        
    def create_menu_widgets(self):
        #create the buttons and label in the menu Frame
        lblTitle = Label(self.menuFrame,text="Main Menu",width = 110)
        btnMultiplication = Button(self.menuFrame,text = "Multiplication",command=lambda: self.goToMultiplicationScreen("M"))
        btnSubtraction = Button(self.menuFrame,text = "Subtraction",command=lambda: self.goToMultiplicationScreen("S"))
        btnDivision = Button(self.menuFrame,text = "Division",command=lambda: self.goToMultiplicationScreen("D"))
        btnAddition = Button(self.menuFrame,text = "Addition",command=lambda: self.goToMultiplicationScreen("A"))
        btnParentsReport = Button(self.menuFrame,text = "Parents Section",command=lambda: self.ParentsReports("P"))
        
        #Grid the widgets CHIEF
        lblTitle.grid(row=0,column=0,pady=12,padx=50)
        btnMultiplication.grid(row=1,column=0)
        btnAddition.grid(row=2,column=0)
        btnSubtraction.grid(row=3,column=0)
        btnDivision.grid(row=4,column=0)
        btnParentsReport.grid(row=5,column=0)
        
        self.menuFrame.config(bg="PURPLE")
        lblTitle.config(bg="red",fg="White")
    def notCodedPrint(self,widgetName):
        print(widgetName," is not coded yet")
    def notCodedDialog(self ,widgetName):
        showinfo(" GUI",widgetName +" is not coded yet")
#Main program
root = Tk()
root.title("Math Game")
root.geometry("1000x1000")
myGUI = MathGame(root)
root.mainloop()

