#encoding=utf-8

import platform



# class JEB2SampleScript(IScript):
#     def run(self, ctx):
#         print "hello world"
#         print ctx.getSoftwareVersion()

APKDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/apks/" if platform.system() == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/apks/"
STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system() == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"

print APKDIR, STRINGSDIR