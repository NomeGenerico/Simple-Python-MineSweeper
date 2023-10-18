# -*- coding: utf-8 -*-


# Doesn't work as intended. Too bad
# 
#
#

def add2list(renderboard,mineboard):
    
    for i in range(renderboard):
        for j in range(mineboard):
            renderboard[i][j] = renderboard[i][j] + renderboard[i][j]
    
    
    

donearray = []
waitarray = []

import Generator

# Both RemoveDuplicates and RemoveOverFlow were Geting into an infinite loop. Just slaped 

#   if i > len(waitarray) - 2:
#   ended = True
#   return waitarray

# Until it worked

def RemoveDupliacates():
    global waitarray
    
    ended = False
    i = 2
    while ended == False:
        if waitarray != []:
            if i > len(waitarray) - 2:
                ended = True
                return waitarray
            if waitarray[0] == waitarray [i] and waitarray[1] == waitarray [i+1]:
                waitarray.pop(0)
                waitarray.pop(0)
                i = 2
            else:
                i = i + 2
                if i > len(waitarray) - 2:
                    ended = True
        else:
            ended = True
    return waitarray



### NOT WORKING, IDK WHY


def RemoveDone(tam):
    
    global waitarray
    global donearray
    keeparray = []

    i = 0
    while i < len(waitarray) - 1:
        pair_found_in_donearray = False

        j = 0
        while j < len(donearray) - 1:
            if donearray[j] == waitarray[i] and donearray[j + 1] == waitarray[i + 1]:
                pair_found_in_donearray = True
                break
            j += 2

        if not pair_found_in_donearray:
            keeparray.extend(waitarray[i:i + 2])

        i += 2

    waitarray = keeparray
    return waitarray

    
    
    
    
    
    
    return waitarray
            
    

def RemoveOverflow(tam):
    global waitarray
    ended = False
    i = 0
    while ended == False:
        if i > len(waitarray) - 2:
            ended = True
            return waitarray
        if waitarray != []:
            if waitarray[i] == 0 or waitarray[i] == tam + 1 or waitarray[i+1] == 0 or waitarray[i+1] == tam + 1:
                waitarray.pop(i)
                waitarray.pop(i)
            else:
                i = i + 2
                if i > len(waitarray) - 2:
                    ended = True
    return waitarray

# Yes, Best Function. You cant wait to see UpdateRenderBoard
def DefRenderBoard(tam):
    renderboard = Generator.Gerar0Board(tam)
    return renderboard

def adjacent(numboard,renderboard,x,y,tam):
    global waitarray
    global donearray
    
    if waitarray != [] and numboard[y][x] == 0:
          
        
        waitarray.append(y-1)
        waitarray.append(x-1)
        renderboard[y-1][x-1] = 1
         
        waitarray.append(y-1)
        waitarray.append(x)
        renderboard[y-1][x] = 1
                 
        waitarray.append(y-1)
        waitarray.append(x+1)
        renderboard[y-1][x + 1] = 1
            
        waitarray.append(y)
        waitarray.append(x-1)
        renderboard[y][x-1] = 1
        
        waitarray.append(y)
        waitarray.append(x+1)
        renderboard[y][x+1] = 1
           
        waitarray.append(y+1)
        waitarray.append(x-1)
        renderboard[y+1][x-1] = 1
            
        waitarray.append(y+1)
        waitarray.append(x)
        renderboard[y+1][x] = 1
        
        waitarray.append(y+1)
        waitarray.append(x+1)
        renderboard[y+1][x+1] = 1
        
    renderboard[y][x] = 1
    donearray.append(y)
    donearray.append(x)
    
    
    waitarray = RemoveDupliacates()
    waitarray = RemoveOverflow(tam)
    waitarray = RemoveDone(tam)
        
    return renderboard

def FLoodFill(renderboard,numboard,x,y,tam):
    global waitarray
    waitarray.append(y)
    waitarray.append(x)
    ended = False
    if numboard[y][x] == 0:
        while ended == False:
            
            renderboard = adjacent(numboard,renderboard,x,y,tam)
            
            if waitarray != []:
                y = waitarray[0]
                x = waitarray[1]
                waitarray.pop(0)
                waitarray.pop(0)
            else:
                ended = True
                ended = True
    return renderboard



# Almost Wrote a 1 line function, but removed the renderboard = 1 from somewhere
def updateRenderBoard(numboard,renderboard,x,y,tam):
    FLoodFill(renderboard, numboard, x, y, tam)
    renderboard[y][x]=1
    
    return renderboard           
                
                
                
" |  |  |  | | ──────── "
                

def Numboard(numboard, renderboard, tam):
    i = 1
    j = 1
    while i < (tam + 1):     
        print(i," | ",end="")
        while j < (tam + 1):
            if renderboard[i][j] == 1:
                print(numboard[i][j],"| ",end="")                      
            else:
                print("▢ | ",end="")           
            j = j + 1
        j = 1
        i = i + 1
        print("")
    return

















                