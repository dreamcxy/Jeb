# encoding=utf-8
import os
import re
import platform
import xml.etree.ElementTree as et

STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"


def loadStringsSuitable():
    stringsList = []
    stringsFiles = os.listdir(STRINGSDIR)
    while stringsFiles:
        stringFile = STRINGSDIR + stringsFiles.pop()
        print stringFile
        stringsList += extractSuitableStringFromFile(stringFile)
    return stringsList


def extractSuitableStringFromFile(stringFile):
    stringsList = []
    with open(stringFile) as strings:
        content = strings.read()
    content = re.sub(u'[\x00-\x08\x0b-\x0c\x0e-\x1f]+', u"", content)
    try:
        root = et.fromstring(content)
        print len(root)
        for i in range(0, len(root)):
            if root[i].text:
                stringsList.append(root[i].text.encode("utf-8"))
        return stringsList    
    except et.ParseError:
        return []


def main():
    stringList = loadStringsSuitable()
    print len(stringList)
    while stringList:
        print stringList.pop()


if __name__ == '__main__':
    main()
