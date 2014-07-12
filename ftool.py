from FileUtil import FileTool
import sys
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
ftool=FileTool(currentPath,wildcard)
isGo=ftool.engine()
if(isGo):
    if(isShow):
        ftool.show()
    if isCopy:
        ftool.copy(copyPath)
        print("copy done")
    if isDelet:
        ftool.delete()
else:
    print("ftool engine faild")