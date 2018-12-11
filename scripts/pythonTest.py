import os

apkFiles = os.listdir("/Users/chenxiaoyu/Desktop/Project/Jeb/apks/")
windowSize = 4
apkFileList = []
while apkFiles:
    for i in range(0, windowSize):
        if apkFiles:
            apkFileList.append(apkFiles.pop())
    while apkFileList:
        print apkFileList.pop()