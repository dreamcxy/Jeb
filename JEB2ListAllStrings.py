# coding=utf-8
from com.pnfsoftware.jeb.client.api import IScript

class JEB2ListAllStrings(IScript):
    def run(self, ctf):
        print ctf.getArguments()