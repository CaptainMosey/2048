import numpy as np
import random
import sys
import array
import copy
import scoring
import time

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
                
                #print self.currentState
                #print "Score = ",self.score


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
                        
                        #print self.currentState
                        #print "Score = ",self.score

        def isGameOver(self):
                '''not handled right yet. game over requires no legal moves, and no zeros'''

                return not checkForLegalMoves(self.currentState)

        def show(self):
                return self.currentState
        
def checkForLegalMoves(board):
                
                spaces=0
                ans=False
                if numOpenSpaces(board):
                        return True
                for x in ("N","S","E","W"):
                        a=checkMove(board,x)
                        if not statesAreTheSame(a[1],board):
                                return True
                return ans
        
def checkForLegalMovesAndSpaces(board):
                
                
                ans=False
                spaces=0
                for x in range(16):
                        if board[x/4,x%4]==0:
                                spaces+=1
                
                if spaces:
                        return True,spaces
                for x in ("N","S","E","W"):
                        a=checkMove(board,x)
                        if not statesAreTheSame(a[1],board):
                                return True,spaces
                return ans,spaces


          



def statesAreTheSame(board1,board2):
        #returns True is the states are the same
        ans=True
        for x in range(16):
                #print x/4,x%4,"\n",board1,"\n",board2
                if board1[x/4][x%4]!=board2[x/4][x%4]:ans=False
        return ans
                
def value(board,score=0,levels=0,w1=1,w2=0,w3=5,w4=20,w5=-20,w6=30,w7=2):
        '''decide on value for state
        possible heruisitics:
            points for last move
            is highest tile in corner or edge
            number of open spaces (if 0, score is low...)
            want 2 and 4 next to open space

        try:

        S=w1(points)+w2(high on edge)+w3(num open spaces) +w4(2 and 4 near open)+w5(is the game over)


        '''
        #to start
        #1=1
        #w2=0
        #w3=5
        #w4=20
        #w5=-20 
        #w6=30
        #w7=2. number of tiles 
        Q=0

        likelihood2=0.9
        a=checkForLegalMovesAndSpaces(board)
        spaces=a[1]
        over=not a[0]
        #ans=w1*(score)+w2*isHighestTileOnEdge(board)+w3*spaces+w4*twoAndFourNearOpen(board)+w5*over
        #ans=w1*(score)+w3*spaces+w4*twoAndFourNearOpen(board)+w5*over
        ans=w1*(score)+w3*spaces+w4*twoAndFourNearOpen(board)+w5*over+w6*areHighestTilesOnEdge(board,w7)

        #just trying this out -  cant imagine when the board is empty we need to do 3 level search of (2new tile possibilitiesx15locationx4 moves)^3 = 1.7 million options)
        # here i wait until it is 2x5x4, whichis still 500,000 options
        #if spaces>5:levels-=1        

         
        if levels<=0:return ans
        
        #for levels>0, need expectimax

        zeroList=[]
        for x in range(16):
                if board[x/4,x%4]==0:
  
                        zeroList.append([x/4,x%4])
        temp=copy.copy(board)
        for x in zeroList:
                #value is going to be equal weighting of chance of 2 and 4 at each site
                
                
                temp[x[0],x[1]]=2
                Q+=(likelihood2*expectimax(temp,levels-1)[1])/len(zeroList)
                temp[x[0],x[1]]=4
                Q+=((1-likelihood2)*expectimax(temp,levels-1)[1])/len(zeroList)
                temp[x[0],x[1]]=0
        ans=(ans+Q)
        
        
        

        
        return ans


def findHighestTile(board):
        highest=-1
        index=[]
        for x in range(16):
                if board[x/4,x%4]>highest:
                        highest = board[x/4,x%4]
                        index=[x/4,x%4]
        return(highest,index)
                        
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

def areHighestTilesOnEdge(board,tiles=2):
        #search for highest tile, save index
        highest=np.zeros((tiles+1))
        index=[(1,1)]*(tiles+1)
        #print index
        ans=0

        for x in range(16):
                for y in range(tiles-1,-1,-1):
                        if board[x/4,x%4]>highest[y]:#if better, lowert the old one in rank
                                highest[y+1]=highest[y]
                                index[y+1]=index[y]
                                highest[y] = board[x/4,x%4]
                                index[y]=(x/4,x%4)






        #evaluate
        for y in range(tiles):
                #print "\n",highest[y],index[y]
                if index[y][0]==0:
                        ans+=1
                if index[y][0]==3:
                        ans+=1
                if index[y][1]==0:
                        ans+=1
                if index[y][1]==3:
                        ans+=1
                
                
        

        if tiles:
                return (float(ans)/float(tiles))
        else:return 0



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
   
                                if y[0] in range(0,4):

                                        if (y[1] in range(0,4)):

                                                
                                                if board[y[0],y[1]]==2:
                                                        ans2=True                                                        
                                                if board[y[0],y[1]]==4:
                                                        ans4=True

                if ans2&ans4:
                        return True
        


        
       
       
        return (False)



def checkMove(board,direction):# direction = [-1,0],[1,0],[0,-1],[0,1]
                #board is just the grid
                newArray=copy.copy(board)
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
                return(not nothingChanged,newArray,score)
                                                                
     

def expectimax(board,levels=1,w1=1,w2=0,w3=5,w4=20,w5=-20,w6=30,w7=2):
        #checks board through x levels, returns bext move,value
        #value is value of next move plus sum of probabilities*values for next moves

        bestMove=""
        bestValue=-10000000
        
        moves=("N","S","E","W")
        for x in moves:
                temp= checkMove(board,x)
                if temp[0]:
                        if value(temp[1],temp[2],levels,w1,w2,w3,w4,w5,w6,w7)>bestValue:
                                bestMove=x
                                bestValue=value(temp[1],temp[2])
        if bestValue==-1:
                print board,"\n",temp
                k=raw_input("")
        return bestMove,bestValue
                        
        
        

def run(numTrials=1,showGames=False,levels=1,w1=1,w2=0,w3=5,w4=20,w5=-20,w6=30,w7=2):
        start= time.time()
        averageScore=0
        topScore=0
        lowScore=1000000



        for x in range(numTrials):
                a=GameState()

                while checkForLegalMoves(a.currentState):
                        #k=expectimax(a.currentState,levels)
                        k=expectimax(a.currentState,levels,w1,w3,w4,w5,w6,w7)
                        if showGames:
                                print a.show()
                                print"Score = ",a.score
                        #q=raw_input("best move "+k[0])
                        if a.move(k[0]):
  
                                a.addNumber()

                        else:
                                print "No MOve?"
                                print a.currentState
                                print "Expectimax chose",k[0],"at valuye",k[1]
                #print a.show()
                end= time.time()
                print x,a.score,findHighestTile(a.currentState)[0],end-start
                start=end
                averageScore+=a.score/numTrials
                if a.score>topScore:topScore=a.score
                if a.score<lowScore:lowScore=a.score
        print "Average Score=",averageScore," in ",numTrials," trials"
        print "Top Score was",topScore,". Low Score was",lowScore


                
def runTest(numTrials=1,showGames=False,levels=1):
        start= time.time()
        averageScore=0
        topScore=0
        lowScore=1000000
        duration=0
        filename="output"+str(int(time.time()))+".csv"
        outputFile=open(filename,"w")
        print(filename)
        header=str("Number,Time,w1,w3,w4,w5,w6,w7,AvScore,HighScore,LowScore,HighestTile,numTrials = "+str(numTrials)+" levels = "+str(levels))
        print(header)
        
        outputFile.write(header+"\n")
        for f in range(1,2):#score, w1
                for g in (0,5,10):#w3, value per space
                        for b in range(0,1):#,20,40,60): #w4, 2and4 near open
                                for c in range(-30,-29):#w5 game over
                                        for d in range(30,31):#w6 higest  on edges
                                                for e in range(0,2):#w7, number of tiles
                                                        averageScore=0
                                                        topScore=0
                                                        lowScore=10000000
                                                        highestTile=0
                                                        for x in range(numTrials):
                                                                a=GameState()

                                                                while checkForLegalMoves(a.currentState):
                                                                        #k=expectimax(a.currentState,levels)
                                                                        k=expectimax(a.currentState,levels,w1=f,w3=g,w4=b,w5=c,w6=d,w7=e)
                                                                        if showGames:
                                                                                print a.show()
                                                                                print"Score = ",a.score
                                                                        #q=raw_input("best move "+k[0])
                                                                        if a.move(k[0]):
          
                                                                                a.addNumber()
        
                                                                        else:
                                                                                print "No MOve?"
                                                                                print a.currentState
                                                                                print "Expectimax chose",k[0],"at valuye",k[1]
                                                                #print a.show()
                                                                
                                                                #to write
                                                                highTile=findHighestTile(a.currentState)[0]
                                                                print x,a.score,highTile,time.time()-start
                                                                
                                                                averageScore+=a.score/numTrials
                                                                if a.score>topScore:topScore=a.score
                                                                if a.score<lowScore:lowScore=a.score
                                                                if highTile>highestTile:highestTile=highTile

                                                                
                                                        end= time.time()
                                                        duration=end-start
                                                        start=end
                                                        writeString=str(x)+","+str(duration)+","+str(f)+","+str(g)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(averageScore)+","+str(topScore)+","+str(lowScore)+","+str(highestTile)
                                                        print writeString
                                                        outputFile.write(writeString+"\n")
        outputFile.close()
                                                
  
                

def manual():

                a=GameState()

                while checkForLegalMoves(a.currentState):

                        
                        print a.show()
                        print"Score = ",a.score
                        q=raw_input("")
                        if a.move(q):
  
                                a.addNumber()
                        #print "tile score:",areHighestTilesOnEdge(a.currentState)
                        
                print "Your score was ",a.score,"highest tile was",findHighestTile(a.currentState)[0]

#manual()   
#run()




