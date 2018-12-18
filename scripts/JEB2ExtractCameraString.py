# encoding=utf-8

import os
import platform
import shutil
from com.pnfsoftware.jeb.client.api import IScript
from com.pnfsoftware.jeb.core import Artifact
from com.pnfsoftware.jeb.core.input import FileInput
from com.pnfsoftware.jeb.core.output.text import ITextDocument
from java.io import File


APKDIR = "D:/DetectApksSecond/" if platform.system(
) != 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/apks/"
STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) != 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"
APKLOADEDDIR = "D:/DetectApksSecondLoaded/"

WINDOWSIZE = 2


class JEB2ExtractCameraString(IScript):

    def run(self, ctx):
        engineContext = ctx.getEnginesContext()
        if not engineContext:
            print "engine is not initialized"
            return
        projects = engineContext.getProjects()
        if not projects:
            print "there is no opened project"
            return
        project = projects[0]
        print "start to load apkfile....."
        apkFiles = os.listdir(APKDIR)
        apkFileDealList = []
        while apkFiles:
            for i in range(0, WINDOWSIZE):
                if apkFiles:
                    apkFileDealList.append(apkFiles.pop())
            while apkFileDealList:
                apkName = apkFileDealList.pop()
                artifact = self.loadArtifacts(APKDIR + apkName)
                liveArtifact = project.processArtifact(artifact)
                print "now in artiface: " + artifact.getName()
                self.extractStringsXmlFromArtifact(liveArtifact)
                self.destroyUnitsOnlyRemainApkName(project, liveArtifact)
                self.moveFile(APKDIR+apkName, APKLOADEDDIR+apkName)
        # for apkFile in apkFiles:
        #     # print apkFile
        #     artifact = self.loadArtifacts(APKDIR + apkFile)
        #     liveArtifact = project.processArtifact(artifact)
        #     self.extractStringsXmlFromArtifact(liveArtifact)
        #     self.destroyUnitsOnlyRemainApkName(project, liveArtifact)


#   将apk转为artifact文件

    def loadArtifacts(self, artifactFilePath):
        artifactFile = File(artifactFilePath)
        return Artifact(artifactFile.getName(), FileInput(artifactFile))


#   将artifact中Resources下的strings.xml录入到文件中

    def extractStringsXmlFromArtifact(self, liveArtifact):
        stringFilePath = STRINGSDIR + liveArtifact.getArtifact().getName() + ".txt"
        print stringFilePath
        units = liveArtifact.getUnits()
        if not units:
            print "artifact loaded fail"
            return
        unit = units[0]
        unitChildren = unit.getChildren()
        if not unitChildren:
            print "artifact explain unit fail"
            return
        for unit_child in unitChildren:
            if unit_child.getName() == "Resources":
                for resource_child in unit_child.getChildren():
                    if resource_child.getName() == "values":
                        for value_child in resource_child.getChildren():
                            if value_child.getName() == "strings.xml":
                                doc = self.getTextDocument(value_child)
                                text = self.formatTextDocument(doc)
                                with open(stringFilePath, 'w') as stringFile:
                                    stringFile.write(text.encode("utf-8"))
                                return

    def getTextDocument(self, srcUnit):
        formatter = srcUnit.getFormatter()
        if formatter and formatter.getDocumentPresentations():
            doc = formatter.getDocumentPresentations()[0].getDocument()
            if isinstance(doc, ITextDocument):
                return doc
        return None

    def formatTextDocument(self, doc):
        s = ''
        # retrieve the entire document -it's a source file,
        # no need to buffer individual parts. 10 MLoC is enough
        alldoc = doc.getDocumentPart(0, 10000000)
        for line in alldoc.getLines():
            s += line.getText().toString() + '\n'
        return s

#   删除载入的artifact下的所有unit，只保留artifact的名字也就是apk名
    def destroyUnitsOnlyRemainApkName(self, project, liveArtifact):
        units = liveArtifact.getUnits()
        for unit in units:
            project.destroyUnit(unit)

#   将已经载入过的apkfile 移动到另外的文件夹中
    def moveFile(self, nowPos, targetPos):
        shutil.move(nowPos, targetPos)
