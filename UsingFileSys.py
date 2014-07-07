import sys
import os
import glob
from collections import deque
print (sys.version)
print (sys.argv[1])
currentPath=sys.argv[1]
wildcard=sys.argv[2]
tmpList=deque()
tmpList.append(currentPath)


#os.chdir(currentPath)
#tmpList=deque(os.listdir(currentPath))
dirList=deque()
results=deque()
nextList=deque()
print (tmpList)
print (results)
print (dirList)
print (os.getcwd())
while(len(tmpList)>0):
    tmpDir=tmpList.popleft()
    if(os.path.isdir(tmpDir)):
        os.chdir(tmpDir)
        dirList.append(tmpDir)
        nextList=os.listdir(tmpDir)
        while(len(nextList)>0):
            tmpList.append(os.getcwd()+os.sep+nextList.pop())
print dirList

'''
while(len(tmpList)>0):
    tmpDir=tmpList.popLeft()
    if(os.path.isdir(tmpDir)):
        dirList.append(tmpDir)
while(len(dirList)>0):
    if(os.path.isdir(tmpDir)):
        dirList.append(tmpDir))
        os.chdir(tmpDir)
        results.append(glob.glob(wildcard))
'''
