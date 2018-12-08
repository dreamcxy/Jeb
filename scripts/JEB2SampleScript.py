#coding=utf-8
from com.pnfsoftware.jeb.client.api import IScript




class JEB2SampleScript(IScript):
    def run(self, ctx):
        print "hello world"
        print ctx.getSoftwareVersion()

