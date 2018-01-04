#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Manipulating Files by shutil and multiprocessing
Like copying files to another folder or so on.
Personal used for daily Deep Learning
Yichao Huang
2018.1
'''

import os
import shutil
from multiprocessing import Pool

import utf8_io

def copy_file(paths):
    assert len(paths)==2
    from_path = paths[0]
    to_path = paths[1]
    #print gotopath
    shutil.copy(from_path, to_path)
    return to_path

def copy_files_multi(from_path_list, to_path_list):
    '''
    from_path_list: a list of from paths
    to_path_list: a list of to paths
    two list should have the same length
    '''
    assert len(from_path_list)==len(to_path_list)
    length = len(from_path_list)
    print '[file_io]', 'copying '+str(length)+' files to target places.'
    paths_list = []
    for idx in xrange(length):
        paths_tup = (from_path_list[idx], to_path_list[idx])
        paths_list.append(paths_tup)

    pool = Pool()
    pool.map(copy_file, paths_list)
    pool.close()
    pool.join()

def main():
    paths, labels = utf8_io.read_sublines('test/test-utf8.txt')
    if not os.path.exists('test/copy-data'):
        os.makedirs('test/copy-data')
    cppaths = [pth.replace('synthetic-data','copy-data') for pth in paths]
    copy_files_multi(paths, cppaths)

if __name__ == '__main__':
    main()