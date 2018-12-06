# coding=utf-8

from com.pnfsoftware.jeb.client.api import IScript
from com.pnfsoftware.jeb.core import Artifact
from com.pnfsoftware.jeb.core.input import FileInput

from java.io import File


class Artifact(object):
    """docstring for Artifact"""

    def __init__(self, arg):
        super(Artifact, self).__init__()
        self.arg = arg


class JEB2ExtractCameraString(IScript):

    def run(self, ctx):
        engineContext = ctx.getEnginesContext()
        project = engineContext.getProject(0)
        artifact = Artifact("Place", FileInput(
            File("D:\DetectApksSecond\\adult.dating.secret 3.11.45 45 .apk")))
        project.processArtifact(artifact)

    def loadArtifact(self):


def main():
    pass


if __name__ == '__main__':
    main()
