#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 文件 文档注释，
 doc comments,
"""

assert 'comment' == 'comment' # comment,
# raise Exception
"""
 multiline comments,
 raise Exception
"""

class C:
    """ 类 文档注释 doc comments, class C """
    def __init__(self, name):
        """
        方法 文档注释 doc __init__ self
        下面也是原原本本的，
        :param name: 名字
        :return: nothing
        """
        pass

assert (len(__doc__)) == 26
assert (len(C.__doc__)) == 30
assert (len(C.__init__.__doc__)) == 111
