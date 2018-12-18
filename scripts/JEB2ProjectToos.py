# encoding=utf-8

import os
import platform
import shutil
from com.pnfsoftware.jeb.client.api import IScript
from com.pnfsoftware.jeb.core import Artifact
from com.pnfsoftware.jeb.core.input import FileInput
from com.pnfsoftware.jeb.core.output.text import ITextDocument
from java.io import File


FirstProject = "C:\Users\dreamcxy\Desktop\Security\SilentCamera\codes\Jeb\apks\1_com.ss.android.ugc.boom 3.1.0 3102 .apk"
SecondProject = "C:\Users\dreamcxy\Desktop\Security\SilentCamera\codes\Jeb\apks\ a201706021616.vpn.turbovpn 1.2.3 16 .apk"

APKDIR = "D:/DetectApksSecond/" if platform.system(
) != 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/apks/"
STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) != 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"
APKLOADEDDIR = "D:/DetectApksSecondLoaded/"

WINDOWSIZE = 3



class JEB2ProjectToos(IScript):

    def run(self, ctx):
        engineContext = ctx.getEnginesContext()
        print engineContext
        # if not engineContext:
        #     print "engine not init"
        #     return
        # artifact_count_in_firstProject = 0
        # artifact_count_in_secondProject = 0 

        
        
        



        # second_project = self.load_project(SecondProject, engineContext)
        # artifact_first = self.loadArtifacts("D:/DetectApksSecond/a201706011153.xsky.txvpn 1.2.1 16 .apk")
        # artifact_second = self.loadArtifacts("D:/DetectApksSecond/admobileapps.multiapps38 1.0 10 .apk")

        # first_project.processArtifact(artifact_first)
        # second_project.processArtifact(artifact_second)
        project = engineContext.getProjects()[0]
        print project.getKey()
        engineContext.unloadProject(project.getKey())
        
        
        # first_project = self.load_project(FirstProject, engineContext)

        
       
        
    def loadArtifacts(self, artifactFilePath):
        artifactFile = File(artifactFilePath)
        return Artifact(artifactFile.getName(), FileInput(artifactFile))


    def load_project(self, project_key, engineContext):
        return engineContext.loadProject(project_key)