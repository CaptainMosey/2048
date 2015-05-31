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







    


    


