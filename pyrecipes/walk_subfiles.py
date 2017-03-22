#!/usr/bin/python
#-*-encoding=utf-8 -*-
"""
返回该路径下的所有文件
argv:
     srcdir 输入文件的路径

return:
    filelist该路径下的所有文件列表
"""
import os
import os.path
def get_subfiles(srcdir = None):
    filelist= []
    def process_dir(arg, dirname, names):
        for name in names:
            name_path = "{}{}{}".format(dirname, os.sep, name)
            if os.path.islink(name_path):
                os.path.walk(name_path, process_dir, arg)
            elif os.path.isfile(name_path):
                filelist.append(os.path.abspath(name_path))
    if srcdir == None:
        return []
    if isinstance(srcdir, str):
        os.path.walk(srcdir, process_dir, "")
        return filelist
    elif isinstance(srcdir, list):
        for sdir in srcdir:
            os.path.walk(sdir, process_dir, "")
        return filelist

def test_get_subfiles():
    srcdir = "testcase"
    filelist = [
    	"./testcase/data.txt",
        "./testcase/1.txt",
        "./testcase/folder/1.txt",
        "./testcase/folder/folder2/1.txt",
        "./testcase/folder2/1.txt"]
    filelist2 = [os.path.abspath(i) for i in filelist]
    srcdir = os.path.abspath(srcdir)
    l = get_subfiles(srcdir)
    assert set(l) == set(filelist2)

if __name__ == '__main__':
    test_get_subfiles()