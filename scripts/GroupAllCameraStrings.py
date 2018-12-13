# coding=utf-8
import os
import re
import platform
import xml.etree.ElementTree as et
import Camera


STRINGSDIR = "C:/Users/dreamcxy/Desktop/Security/SilentCamera/codes/Jeb/strings/" if platform.system(
) == 'Windows' else "/Users/chenxiaoyu/Desktop/Project/Jeb/strings/"


def load_strings_suitable():
    strings_list = []
    strings_files = os.listdir(STRINGSDIR)
    while strings_files:
        strings_file = STRINGSDIR + strings_files.pop()
        print strings_file
        strings_list += extractSuitableStringFromFile(strings_file)
    return strings_list

def extractSuitableStringFromFile(string_file):
    strings_list = []
    with open(string_file) as strings:
        content = strings.read()
    content = re.sub(u'[\x00-\x08\x0b-\x0c\x0e-\x1f]+', u"", content)
    try:
        root = et.fromstring(content, parser=None)
        print len(root)
        for i in range(0, len(root)):
            if root[i].text:
                if distinguish_cn(root[i].text):
                    strings_list.append(root[i].text)
                # stringList.append(root[i].text.encoding("utf-8"))
        return strings_list
    except et.ParseError:
        return []


def extract_to_file(strings, output_filename):
    with open(output_filename, "w") as output_file:
        output_file.write(strings)
    


def distinguish_cn(string_text):
    cn_pattern = re.compile(u'[\u4e00-\u9fa5]')
    match = cn_pattern.search(string_text)
    return match


def dealStrings(args):
    pass


def classifyStrings(args):
    pass


def main():
    stringList = load_strings_suitable()
    print "length: " + str(len(stringList))
    while stringList:
        try:
            print stringList.pop()
        except IOError:
            continue
    


if __name__ == '__main__':
    main()
