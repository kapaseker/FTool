import sys
import os
import glob
from collections import deque
'''
s show results
d delete the files
'''
print (sys.version)
params=list(sys.argv[1])
isDelet=False
isShow=False

if params.count("d"):
    isDelet=True
if params.count("s"):
    isShow=True
currentPath=sys.argv[2]
wildcard=sys.argv[3]

tmpList=deque()
tmpList.append(currentPath)
#os.chdir(currentPath)
#tmpList=deque(os.listdir(currentPath))
dirList=deque()
results=[]
nextList=deque()
while(len(tmpList)>0):
    tmpDir=tmpList.popleft()
    if(os.path.isdir(tmpDir)):
        os.chdir(tmpDir)
        dirList.append(tmpDir)
        nextList=os.listdir(tmpDir)
        while(len(nextList)>0):
            tmpList.append(os.getcwd()+os.sep+nextList.pop())
del tmpDir
while(len(dirList)>0):
    tmpDir=dirList.popleft()
    os.chdir(tmpDir)
    tmpResults=glob.glob(wildcard)
    for tmpres in tmpResults:
        results.append(os.getcwd()+os.sep+tmpres)
del tmpDir
del tmpResults

print("result is ----------------------------------------")
if isShow:
    for tmpResult in results:
        print(tmpResult)
del tmpResult
if isDelet:
    for tmpResults in results:
        try:
            os.remove(tmpResults)
        except Exception as ex:
            print("delete file error")
results.clear()
