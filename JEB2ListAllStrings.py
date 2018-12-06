# coding=utf-8
from com.pnfsoftware.jeb.client.api import IScript
from com.pnfsoftware.jeb.core.output.text import ITextDocument

class JEB2ListAllStrings(IScript):
    def run(self, ctx):
        enginesContext = ctx.getEnginesContext()
        project = enginesContext.getProject(0)
        # print project.getName()           得到当前打开的apk的名字
        artifact = project.getLiveArtifact(0)
        unit = artifact.getUnits()[0]
        for child in unit.getChildren():
            if child.getName() == "Resources":
                for s_child in child.getChildren():
                    if s_child.getName() == "values":
                        for t_child in s_child.getChildren():
                            if t_child.getName() == "strings.xml":
                                print "extract string.xml"
                                print t_child.getDescription()

    def getTextDocument(self, srcUnit):
        formatter = srcUnit.getFormatter()
        if formatter and formatter.getDocumentPresentations():
            doc = formatter.getDocumentPresentations()[0].getDocument()
            if isinstance(doc, ITextDocument):
                return doc
        return None