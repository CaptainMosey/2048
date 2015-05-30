import numpy as np
import random
import array



class GameState(object):
        """
          Stores the 16 values in 2048
          initializes to (2) random placed 2s
        """

        def __init__(self):
                notFinished=True
                self.currentState=np.zeros((4,4))
                for x in range(0,15):
                        self.currentState[int(x/4),x%4]=0
                #random.seed(47)
          
                #get 2 2s
                first=int(16*random.random())
                #print self.currentState
        

                while notFinished:
                        second = int(16*random.random())
                        if second!=first:
                                notFinished=False

                #print first,second
        
                self.currentState[first/4,first%4]=2
                self.currentState[second/4,second%4]=2


                #self.currentState[1,1]=2
                #self.currentState[3,1]=2

                                
                self.score=0
                
                print self.currentState
                print "Score = ",self.score


        def move(self,direction):# direction = [-1,0],[1,0],[0,-1],[0,1]
                newArray=self.currentState
                score=0
                nothingChanged=True
                alreadyChangedList=[]
                
                
                #set direction
                if direction == "W":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(0,3):
                                                if newArray[x,y]!=0:#then check to add
                                                        if newArray[x,y+1]== newArray[x,y]:
                                                                newArray[x,y]=2*newArray[x,y+1]
                                                                newArray[x,y+1]=0
                                                                score+=newArray[x,y]
                                                                nothingChanged=False

                                        for y in range(0,3):
                                                if newArray[x,y]==0:
                                                        newArray[x,y]=newArray[x,y+1]
                                                        newArray[x,y+1]=0
                                                        if newArray[x,y]!=0:nothingChanged=False
                elif direction == "E":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(3,0,-1):
                                                if newArray[x,y]!=0:#then check to add
                                                        if newArray[x,y-1]== newArray[x,y]:
                                                                newArray[x,y]=2*newArray[x,y-1]
                                                                newArray[x,y-1]=0
                                                                score+=newArray[x,y]
                                                                nothingChanged=False

                                        for y in range(3,0,-1):
                                                if newArray[x,y]==0:
                                                        newArray[x,y]=newArray[x,y-1]
                                                        newArray[x,y-1]=0
                                                        if newArray[x,y]!=0:nothingChanged=False


                elif direction == "N":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(0,3):
                                                if newArray[y,x]!=0:#then check to add
                                                        if newArray[y+1,x]== newArray[y,x]:
                                                                newArray[y,x]=2*newArray[y+1,x]
                                                                newArray[y+1,x]=0
                                                                score+=newArray[y,x]
                                                                nothingChanged=False

                                        for y in range(0,3):
                                                if newArray[y,x]==0:
                                                        newArray[y,x]=newArray[y+1,x]
                                                        newArray[y+1,x]=0
                                                        if newArray[y,x]!=0:nothingChanged=False
                                                                         
                elif direction == "S":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(3,0,-1):
                                                if newArray[y,x]!=0:#then check to add
                                                        if newArray[y-1,x]== newArray[y,x]:
                                                                newArray[y,x]=2*newArray[y-1,x]
                                                                newArray[y-1,x]=0
                                                                score+=newArray[y,x]
                                                                nothingChanged=False

                                        for y in range(3,0,-1):
                                                if newArray[y,x]==0:
                                                        newArray[y,x]=newArray[y-1,x]
                                                        newArray[y-1,x]=0
                                                        if newArray[y,x]!=0:nothingChanged=False
     


                self.score+=score
                self.currentState=newArray
                
                if nothingChanged:#then nothing moved, not legal
                        return False
                return True
        def addNumber(self):
                
                #figure out how many open spaces there are
 
                zeroList=[]
                for x in range(16):
                        if self.currentState[x/4,x%4]==0:
  
                                zeroList.append([x/4,x%4])
                if len(zeroList)==0:#then game is over
                        print"Game Over"
                        #really end
                else:
                        #print zeroList
                        newPosition=int(random.random()*len(zeroList))
                        #print "New position", newPosition,zeroList[newPosition]
        
                        #decide is adding a 2 or 4
                        #90% 2
                        if random.random()<0.9:
                                newNum=2
                        else:
                                newNum=4
                        #i have no idea why just adding "zeroList[newPosition]" isnt working here!
                        self.currentState[zeroList[newPosition][0],zeroList[newPosition][1]]=newNum
                        
                        print self.currentState
                        print self.score
                     



          
def a():
        a=GameState()
        
        while True:
                k=raw_input("move (N,S,E,W)")
                if a.move(k):
  
                        a.addNumber()

        
a()     
