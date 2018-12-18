# coding=utf-8
import os
import re
import platform
import xml.etree.ElementTree as et
from Camera import Camera_CN, Camera_EN


STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"

def load_strings_suitable():
    strings_list = []
    strings_files = os.listdir(STRINGSDIR)
    while strings_files:
        strings_file = STRINGSDIR + strings_files.pop()
        print strings_file
        strings_list += extract_suitable_string_from_file(strings_file)
    return strings_list


def extract_suitable_string_from_file(string_file):
    strings_list = []
    with open(string_file) as strings:
        content = strings.read()
    content = re.sub(u'[\x00-\x08\x0b-\x0c\x0e-\x1f]+', u"", content)
    try:
        root = et.fromstring(content, parser=None)
        print len(root)
        for i in range(0, len(root)):
            if root[i].text:
                # strings_list.append(root[i].text)
                root_text = root[i].text
                if distinguish_cn(root_text) and if_related_camera_cn(root_text.encode("utf-8")):
                    extract_to_file(root_text, "strings_cn.txt")
                elif if_related_camera_en(root_text):
                    extract_to_file(root_text, "strings_en.txt")
                strings_list.append(root_text)
        return strings_list
    except et.ParseError:
        return []

def if_related_camera_cn(text):
    for cn in Camera_CN:
        if cn.value in text:
            return True
    return False

def if_related_camera_en(text):
    for en in Camera_EN:
        if en.value in text:
            return True
    return False


def extract_to_file(text, output_filename):
    with open(output_filename, "a") as output_file:
        # output_file.write(strings)
        output_file.write(text.encode("utf-8"))


def distinguish_cn(string_text):
    cn_pattern = re.compile(u'[\u4e00-\u9fa5]')
    match = cn_pattern.search(string_text)
    return match


def main():
    stringList = load_strings_suitable()
    print "length: " + str(len(stringList))
    # while stringList:
    #     try:
    #         print stringList.pop()
    #     except IOError:
    #         continue


if __name__ == '__main__':
    main()
