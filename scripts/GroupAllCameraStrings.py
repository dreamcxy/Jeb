import os
import re
import platform

STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"


def loadStringsSuitable():
    stringsList = []
    stringsFiles = os.listdir(STRINGSDIR)
    while stringsFiles:
        stringFile = stringsFiles.pop()

    return stringsList


def extractSuitableStringFromFile(stringFile):
    stringsList = []
    with open(stringFile) as strings:
        for line in strings.readlines():
            stringsList.append(re.match("<string[^>]*>([^<]*)</string>", line.strip()))
    return stringsList


def main():
    stringsList = extractSuitableStringFromFile(
        "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/a201706011153.languang.vpn 1.0.5.1 11 .apk.txt")
    for string in stringsList:
        print string
if __name__ == '__main__':
    main()
