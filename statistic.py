#!/usr/bin/env python
'''
Read Image by OpenCV
Personal used for daily Deep Learning
Yichao Huang
2017.11
'''

import utf8_io

def do_statistic(lines, charset):
    ''' do statistic on multiple lines '''
    stat_dict = {}
    for char in charset:
        stat_dict[char] = 0
    
    for line in lines:           
        for symbol in line:
            if symbol not in stat_dict:
                print 'Not included character: '+symbol
                print 'Origin: '+line
                continue 
            stat_dict[symbol]+=1
    print stat_dict
    return stat_dict

def main():
    charset = utf8_io.read_charset('test/charset-utf8.txt')
    sublines = utf8_io.read_sublines('test/test-utf8.txt')
    paths, labels = sublines
    stat_dict = do_statistic(labels, charset)
    utf8_io.write_dict('test/statistic.txt', stat_dict)

if __name__ == '__main__':
    main()