#reading excel data's
import pandas as pd
pcd = pd.read_excel("./ProvinceCenterDistances.xlsx")
pcdsl = pd.read_excel("./ProvinceCentersStraightLineDistances.xlsx")
neibours = pd.read_excel("./ProvinceCentersNeighbours.xlsx")

#define a dictionary for working with files
city_id = {'arak':0 ,'ardabil':1,'urmia':2,'esfahan':3,'ahvaz':4,	'eylam':5,	'bojnord':6,	'bandar abbas':7,	'bushehr':8,	'birjand':9,	'tabriz':10,	'tehran':11,	'khoram abad':12	,'rasht':13,	'zahedan':14,	'zanjan':15,\
            	'sari':16,	'semnan':17,	'sanandaj':18,	'shahre kord':19,	'shiraz':20,	'qazvin':21,	'qom':22,	'karaj':23,	'kerman':24,	'kermanshah':25,'gorgan':26,	'mashhad':27,	'hamedan':28,	'yasuj':29,	'yazd':30}


class Node():
    """A Node class for A* Pathfinding"""
    def __init__(self, parent=None, state=None):
        self.parent = parent
        self.state = state

        self.g = self.h = self.f = 0
    def __eq__(self, temp):
        return self.state == temp.state


# A* algorithm function
def A_Star(src, dest):
    srcNode = Node(None, src)
    destNode = Node(None, dest)

    openList = []
    closedList = []

    openList.append(srcNode)

    while len(openList) > 0:


        currentNode = openList[0]
        currentIndex = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        openList.pop(currentIndex)
        closedList.append(currentNode)


        if currentNode == destNode:

            path = []
            current = currentNode

            while current is not None:
                path.append(current.state)
                current = current.parent

            return path[::-1] 


        #generate children
        children = []
        #dirs for finding new state
        dirs = ['arak','ardabil','urmia','esfahan','ahvaz',	'eylam',	'bojnord',	'bandar abbas',	'bushehr',	'birjand',	'tabriz',	'tehran',	'khoram abad'	,'rasht',	'zahedan',	'zanjan',\
            	'sari',	'semnan',	'sanandaj',	'shahre kord',	'shiraz',	'qazvin',	'qom',	'karaj',	'kerman',	'kermanshah','gorgan',	'mashhad',	'hamedan',	'yasuj',	'yazd'
]
        for newState in dirs: 

            nodeState = newState

            if (neibours.at[city_id[currentNode.state],nodeState] != 1):
                continue

            children.append(Node(currentNode, nodeState))

        for child in children:
            err = None
            for closedChild in closedList:
                if closedChild == child:
                    err = 1
            if (err != None):
                continue

            child.g = pcd.at[city_id[srcNode.state],child.state]
            child.h =pcdsl.at[city_id[child.state],destNode.state]
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    err =1
            if (err != None):
                continue

            openList.append(child)

        if (len(openList) > 35 ** 2): 
           return None

def main():

    src = input("Enter source:")
    dest = input("Enter Destination:")

    pathSrcToDest = A_Star(src, dest)
    print(pathSrcToDest)


if __name__ == '__main__':
    main()
