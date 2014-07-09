import sys
import os
import glob
import shutil
from collections import deque
'''
c copy
s show results
d delete the files
'''
print (sys.version)
try:
    params=list(sys.argv[1])
    currentPath=sys.argv[2]
    wildcard=sys.argv[3]
except Exception as ex:
    print("you params is less than neccessay")
    print("param 1 ,operation;")
    print("param 2 ,direction;")
    print("param 3 ,wildcar.")
    sys.exit()

isDelet=False
isShow=False
isCopy=False

if params.count("d"):
    isDelet=True
if params.count("s"):
    isShow=True
if params.count("c"):
    isCopy=True
if isCopy:
    try:
       copyPath=sys.argv[4]
    except Exception as ex:
        print("you params have not path for copy")
        sys.exit()

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

if isCopy:
    if os.path.exists(copyPath)==False:
        os.mkdir(copyPath)
    for tmpResults in results:
        try:
            shutil.copy(tmpResults,copyPath)
        except Exception as ex:
            print("copy file error")
            print(str(ex))
print ("copy Done")

if isDelet:
    for tmpResults in results:
        try:
            os.remove(tmpResults)
        except Exception as ex:
            print("delete file error")
results.clear()
