#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Doing Statistic on Text Data
Personal used for daily Deep Learning
Yichao Huang
2017.11
'''

import os
import sys
import cPickle
import jieba

import utf8_io

def is_chinese(label):
    ''' as name telss, acccoding to chinese unicode range '''
    cncount = 0
    encount = 0
    for ele in label:
        if u'\u4e00' <= ele <= u'\u9fff':
            cncount += 1
        else:
            encount += 1
    return cncount >= encount


def count_character_frequency(lines):
    ''' argv[0]: corpus in lines, utf8 encoded '''
    char_freq = {}
    for line in lines:
        for char in line:
            char_freq[char] = char_freq.get(char, 0)+1
    return char_freq

def count_word_frequency(lines):
    ''' argv[0]: corpus in lines, utf8 encoded '''
    words_freq = {}
    for line in lines:
        segs = jieba.cut(line, cut_all=True)
        genline = '\t'.join(segs)
        genwords = genline.split('\t')
        for word in genwords:
            words_freq[word] = words_freq.get(word, 0)+1
    return words_freq

def main():
    ''' call main function '''
    #charset = utf8_io.read_charset('test/charset-utf8.txt')

    sublines = utf8_io.read_sublines('test/test-utf8.txt')
    paths, labels = sublines

    char_freq = count_character_frequency(labels)
    word_freq = count_word_frequency(labels)

    utf8_io.write_dict('output/char_freq.txt', char_freq)
    utf8_io.write_dict('output/word_freq.txt', word_freq)

if __name__ == '__main__':
    main()