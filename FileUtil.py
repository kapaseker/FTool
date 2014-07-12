import os
import glob
import shutil
from collections import deque

print ("i'm not ready")

class FileTool:
    '''
    this is a FileTool for file batch
    for example ,delet ,copy,find and etc.
    '''
    results=deque()
    rootdir=""
    wildcard=""
    resultDirs=deque()
    def __init__(self,rootdir,wildcard):
        self.rootdir=rootdir
        self.wildcard=wildcard

    def engine(self):
        tmpDirs=deque()
        tmpDirs.append(self.rootdir)
        if(False==os.path.isdir(self.rootdir)):
            return False
        while(len(tmpDirs)>0):
            tmpDir=tmpDirs.popleft()
            if(os.path.isdir(tmpDir)):
                os.chdir(tmpDir)
                self.resultDirs.append(tmpDir)
                nextList=os.listdir(tmpDir)
                while(len(nextList)>0):
                    tmpDirs.append(os.getcwd()+os.sep+nextList.pop())
        while(len(self.resultDirs)>0):
            tmpDir=self.resultDirs.popleft()
            os.chdir(tmpDir)
            tmpResults=glob.glob(self.wildcard)
            for tmpres in tmpResults:
                self.results.append(os.getcwd()+os.sep+tmpres)
        return True
    def show(self):
        for res in self.results:
            print(res)
        print("all results is :",str(len(self.results)))

    def copy(self,destDir):
        if(False==os.path.exists(destDir)):
            os.mkdir(destDir)
        for res in self.results:
            try:
                shutil.copy(res,destDir)
            except Exception as ex:
                print("copy file error")
                print(str(ex))

    def delete(self):
        for res in self.results:
            try:
                os.remove(res)
            except:
                print("delete file error")
                print(str(ex))

        
