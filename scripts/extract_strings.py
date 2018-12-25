# coding=utf-8
# 直接调用apktool反编译apk之后 提取strings.xml

import subprocess
import os
import shutil
import platform

APKDIR = "D:/DetectApksSecond/" if platform.system(
) == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/apks/"
# APKDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/apks/"
STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"
APKLOADEDDIR = "D:/DetectApksSecondLoaded/"


def apktool_decompile():
    input_files = os.listdir(APKDIR)

    while input_files:
        apk_file_name = input_files.pop()
        if os.path.splitext(apk_file_name)[-1] == ".apk":
            apk_input_path = APKDIR + apk_file_name
            apk_output_path = APKDIR + \
                os.path.splitext(apk_file_name)[0].rstrip()
            if os.path.isdir(apk_output_path):
                os.makedirs(apk_output_path)
            command = "apktool d \"%s\" -o \"%s\" " % (
                apk_input_path, apk_output_path)
            print command
            subprocess.call(command, shell=True)
            shutil.move(APKDIR+apk_file_name, APKLOADEDDIR+apk_file_name)
            strings_origin_path = apk_output_path+"/res/values/strings.xml"
            strings_target_path = STRINGSDIR + \
                os.path.splitext(apk_file_name)[0].rstrip()+".txt"
            print "move path: " + strings_origin_path + "\n"+ strings_target_path
            if os.path.isfile(strings_origin_path):
                print "move strings file"
                shutil.move(strings_origin_path, strings_target_path)
                print "delete decompile dir"
                try:
                    shutil.rmtree(apk_output_path)
                except BaseException:
                    continue
            else:
                continue




def main():
    apktool_decompile()


if __name__ == '__main__':
    main()
