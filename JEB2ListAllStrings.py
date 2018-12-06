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
                                # print t_child.getInput()      "com.pnfsoftware.jeb.core.input.BytesInput@63c342da"
                                # print t_child.getInput().getCurrentSize()
                                doc = self.getTextDocument(t_child)
                                text = self.formatTextDocument(doc)
                                f = open(
                                    "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/test.txt", "w")
                                f.write(text.encode("utf-8"))
                                f.close()

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
