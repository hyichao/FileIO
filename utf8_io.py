#!/usr/bin/env python
'''
Read UTF8 encoded file
File List or Charset
Personal used for daily Deep Learning
Yichao Huang
2017.11
'''

import os

def read_charset(filename):
    ''' read file return a dict of char and number mapping '''
    with open(filename,'r') as infile:
        content = infile.read().decode('utf8')
        if content[-1] is '\n':
            content = content[:-1]
        content = sorted(content)
        charset = {}
        for idx, ele in enumerate(content):
            charset[ele] = idx
        print str(len(charset))+' classes without end-line symbol'
        print content[0], charset[content[0]]
        print content[-1], charset[content[-1]]
        return charset

def read_lines(filename):
    ''' read file return lines '''
    with open(filename,'r') as infile:
        lines = infile.readlines()
        lines = [line.decode('utf8') for line in lines]
        return lines

def read_sublines(filename):
    ''' read file return lines which split by \t '''
    lines = read_lines(filename)
    group_num = len(lines[0].split('\t'))
    group_lines = []
    for idx in xrange(group_num):
        sublines = []
        group_lines.append(sublines)
    # split by \t
    for line in lines:
        words = line.strip('\n').split('\t')
        for idx in xrange(group_num):
            group_lines[idx].append(words[idx])
    # print out
    print 'line number: '+str(len(group_lines))
    print 'seperate into '+str(group_num)
    for idx in xrange(group_num):
        print 'subline number: '+str(len(group_lines[idx]))
        print group_lines[idx]
        print len(group_lines[idx][0])
        print group_lines[idx][0].encode('utf8')

    return group_lines

def write_lines(filename, lines):
    ''' write lines into file '''
    with open(filename,'w') as outfile:
        for line in lines:
            outfile.write(line) 

def write_dict(filename, dicts):
    ''' write sorted dict '''
    outlines = []
    for key, value in sorted(dicts.iteritems(), key=lambda (k,v): (v,k)):
        outline = key.encode('utf8')+' : '+str(value)+'\n'
        outlines.append(outline)
    write_lines(filename, outlines)

def split_to_files(filename, folder, subnum):
    '''Read multiple lines and split to sub files'''
    print 'split to the following files: '
    partfiles = []
    for partid in xrange(subnum):
        partpath = os.path.join(folder, 'part_{}.txt'.format(partid))
        partfile = open(partpath,'w')
        partfiles.append(partfile)
        print partpath

    lines = read_lines(filename)
    for index, line in enumerate(lines):
        partid = index % subnum
        partfiles[partid].write(line)
    print 'split done.'

def merge_from_files(folder, filename, subnum):
    '''Read all sub files and merge into one'''
    outlines = []
    for partid in xrange(subnum):
        partpath = os.path.join(folder, 'part_{}.txt'.format(partid))
        partlines = read_lines(partpath)
        outlines += partlines
    write_lines(filename, outlines)

def filter_by_keys(fromfile, rmfile, tofile):
    ''' as name tells '''
    fromlines = read_lines(fromfile)
    rmlines = read_lines(rmfile)
    rmdict = {}
    for line in rmlines:
        rmdict[line] = True
    remain = []
    for line in fromlines:
        words = line.split('\t')
        path = words[0]
        if path in rmdict:
            continue
        remain.append(line)
    write_lines(tofile, remain)

def main():
    ''' test reading file with main '''
    # lines = read_lines('test-utf8.txt')
    sublines = read_sublines('test/test-utf8.txt')
    paths, labels = sublines

if __name__ == '__main__':
    main()