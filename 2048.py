import numpy as np
import random
import sys
import array
import copy
import scoring

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
          
                #get 2 2s
                first=int(16*random.random())     

                while notFinished:
                        second = int(16*random.random())
                        if second!=first:
                                notFinished=False
        
                self.currentState[first/4,first%4]=2
                self.currentState[second/4,second%4]=2

                #self.currentState[0,0]=2

                #self.currentState[1,0]=4
                #self.currentState[2,0]=2
                #self.currentState[3,0]=2

                  
                self.score=0
                self.lastScore=0
                self.gameOver=False
                
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
                                                #print x,y, ([x,y] in alreadyChangedList)
                                                #print alreadyChangedList
                                        
                                                if newArray[x,y]!=0:
                                                        if(([x,y] not in alreadyChangedList) & ([x,y+1] not in alreadyChangedList)):#then check to add
                                                                if newArray[x,y+1]== newArray[x,y]:
                                                                        newArray[x,y]=2*newArray[x,y+1]
                                                                        newArray[x,y+1]=0
                                                                        score+=newArray[x,y]
                                                                        nothingChanged=False
                                                                        alreadyChangedList.append([x,y])

                                                                
                                                        
                        
 
                                        for y in range(0,3):
                                                if newArray[x,y]==0:
                                                        newArray[x,y]=newArray[x,y+1]
                                                        newArray[x,y+1]=0

                                                        if newArray[x,y]!=0:
                                                                nothingChanged=False
                                                                if [x,y+1] in alreadyChangedList:
                                                                        alreadyChangedList.remove([x,y+1])
                                                                        alreadyChangedList.append([x,y])

                                                                                
                elif direction == "E":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(3,0,-1):
                                                if newArray[x,y]!=0:#then check to add
                                                        if(([x,y] not in alreadyChangedList) & ([x,y-1] not in alreadyChangedList)):
                                                                if newArray[x,y-1]== newArray[x,y]:

                                                                        newArray[x,y]=2*newArray[x,y-1]
                                                                        newArray[x,y-1]=0
                                                                        score+=newArray[x,y]
                                                                        nothingChanged=False
                                                                        alreadyChangedList.append([x,y])



                                        for y in range(3,0,-1):
                                                if newArray[x,y]==0:
                                                        newArray[x,y]=newArray[x,y-1]
                                                        newArray[x,y-1]=0
                                                        if newArray[x,y]!=0:
                                                                nothingChanged=False
                                                                if [x,y-1] in alreadyChangedList:
                                                                        alreadyChangedList.remove([x,y-1])
                                                                        alreadyChangedList.append([x,y])


                elif direction == "N":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(0,3):
                                                if newArray[y,x]!=0:#then check to add
                                                        if(([y,x] not in alreadyChangedList) & ([y+1,x] not in alreadyChangedList)):
                                                                if newArray[y+1,x]== newArray[y,x]:
                                                                
                                                                        newArray[y,x]=2*newArray[y+1,x]
                                                                        newArray[y+1,x]=0
                                                                        score+=newArray[y,x]
                                                                        nothingChanged=False
                                                                        alreadyChangedList.append([y,x])
                                                                        
                                        for y in range(0,3):
                                                if newArray[y,x]==0:
                                                        newArray[y,x]=newArray[y+1,x]
                                                        newArray[y+1,x]=0
                                                        if newArray[y,x]!=0:
                                                                nothingChanged=False
                                                                if [y+1,x] in alreadyChangedList:
                                                                        alreadyChangedList.remove([y+1,x])
                                                                        alreadyChangedList.append([y,x])

                                                                         
                elif direction == "S":

                        for counter in range(3):#do everythig 3 times 
                                for x in range(0,4):#
                                                              
                                        for y in range(3,0,-1):
                                                if newArray[y,x]!=0:#then check to add
                                                        if(([y,x] not in alreadyChangedList) & ([y-1,x] not in alreadyChangedList)):
                                                                if newArray[y-1,x]== newArray[y,x]:
                                                                
                                                                        newArray[y,x]=2*newArray[y-1,x]
                                                                        newArray[y-1,x]=0
                                                                        score+=newArray[y,x]
                                                                        nothingChanged=False
                                                                        alreadyChangedList.append([y,x])
                                                                        
                                        for y in range(3,0,-1):
                                                if newArray[y,x]==0:
                                                        newArray[y,x]=newArray[y-1,x]
                                                        newArray[y-1,x]=0
                                                        if newArray[y,x]!=0:
                                                                nothingChanged=False
                                                                if [y-1,x] in alreadyChangedList:
                                                                        alreadyChangedList.remove([y-1,x])
                                                                        alreadyChangedList.append([y,x])
                                                                
     

                self.lastScore=score
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
                        self.gameOver=True
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
                        print "Score = ",self.score

        def isGameOver(self):
                '''not handled right yet. game over requires no legal moves, and no zeros'''

                return self.gameOver

        
def checkForLegalMoves(gameState):
                
                
                temp=copy.copy(gameState)

                for x in ("N","S","E","W"):
                        temp.move(x)
                        
                return statesAreTheSame(temp.currentState,gameState.currentState)
                


          
def run():
        a=GameState()
        movesAvailable=True
        
        while movesAvailable:
                k=raw_input("move (N,S,E,W)")
                if a.move(k):
  
                        a.addNumber()
                        #movesAvailable=checkForLegalMoves(a)
                        print "high tile",isHighestTileOnEdge(a.currentState),"num zero",numOpenSpaces(a.currentState),"2s and 4s",twoAndFourNearOpen(a.currentState)
                        print value(a)



def statesAreTheSame(state1,state2):
        #returns True is the states are the same
        ans=True
        for x in range(16):
                if state1[x/4,x%4]!=state2[x/4,x%4]:ans=False
        return ans
                
def value(gameState):
        '''decide on value for state
        possible heruisitics:
            points for last move
            is highest tile in corner or edge
            number of open spaces (if 0, score is low...)
            want 2 and 4 next to open space

        try:

        S=w1(points)+w2(high on edge)+w3(num open spaces) +w4(2 and 4 near open)


        '''
        #to start
        w1=1
        w2=5
        w3=5
        w4=10

        ans=w1*(gameState.lastScore)+w2*isHighestTileOnEdge(gameState.currentState)+w3*numOpenSpaces(gameState.currentState)+w4*twoAndFourNearOpen(gameState.currentState)
        return ans

def isHighestTileOnEdge(board):
        #search for highest tile, save index
        highest=-1
        index=[]
        ans=0

        for x in range(16):
                if board[x/4,x%4]>highest:
                        highest = board[x/4,x%4]
                        index=[x/4,x%4]

        #evaluate
        if index[0]==0:
                ans+=1
        if index[0]==3:
                ans+=1
        if index[1]==0:
                ans+=1
        if index[1]==3:
                ans+=1
                
                
        

        return ans

def numOpenSpaces(board):
        counter=0
        for x in range(16):
                if board[x/4,x%4]==0:
                        counter+=1
        return counter

def twoAndFourNearOpen(board):
        ans2=False
        ans4=False
       
        for x in range(16):
                
                if board[x/4,x%4]==0:
                        
                        #check nearby
                        for y in ([x/4+1,x%4],[x/4-1,x%4],[x/4,x%4+1],[x/4,x%4-1]):
                                
                                if y[0] in range(0,2):
                                        if (y[1]<4 & y[1]>=0):
                                                
                                                if board[y[0],y[1]]==2:
                                                        ans2=True
                                                  
                                                        
                                                if board[y[0],y[1]]==4:
                                                        ans4=True
                if ans2&ans4:
                        return True
        


        
       
       
        return (ans2 & ans4)




run()




