from com.pnfsoftware.jeb.client.api import IScript
from com.pnfsoftware.jeb.core import Artifact


class JEB2ProjectToos(IScript):

    def run(self, ctx):
        engineContext = ctx.getEnginesContext()
        project = engineContext.getProject(0)
        print "artifact count: " + str(project.getArtifactCount())

        liveActifact = project.getLiveArtifact(1)
        print "artifact name: " + liveActifact.getArtifact().getName()
        units = liveActifact.getUnits()
        for unit in units:
            project.destroyUnit(unit)
