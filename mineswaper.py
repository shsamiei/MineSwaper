

class mineSwaper :
    maps = [] 
    def __init__(self , col , row ):
        
        self.row = row
        self.col = col 

        for i in range(self.col) :
            mineSwaper.maps.append([])
            for j in range(self.row):
                mineSwaper.maps[i].append(0)
            

    def getList(self):
        return mineSwaper.maps 

    def BombIt(self ,x ,y):
        mineSwaper.maps[x][y] = "*"
        mineSwaper.up_adjacent(self,x,y)
        pass



    def up_adjacent(self,x,y) :
         pos = [-1, 0, 1]
         for i in pos:
                for j in pos:
                    if i != 0 or j != 0:
                        if ((x + i) >= 0 and (x + i) < self.col ) and ( (y+j) >= 0 and (y+j) < self.row ):
                            if mineSwaper.maps[x+i][y+j] != "*" :
                                 mineSwaper.maps[x+i][y+j] += 1
       
        
x, y = [int(x) for x in input().split()]
mswap = mineSwaper(x,y) 


number_of_bomb = int(input())

for t in range(number_of_bomb):
    x1 , y1 = [int(x) for x in input().split()]
    mswap.BombIt(x1-1,y1-1)

result_of_mineswaper = mswap.getList()

for  i in range(x) :
    for  j in range(y) :
        print(result_of_mineswaper[i][j],' ' , end='')
    print()



