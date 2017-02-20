#!/usr/bin/env python
# encoding: UTF-8

import re
import sys


def create_letter_pool(source):
    pool = dict()
    for x in source:
        if x in pool:
            pool[x] += 1
        else:
            pool[x] = 1
    return pool


def loose_match(word, length, regex):
    if len(word) != length:
        return False
    matches = re.finditer(regex, word)
    for matchNum, match in enumerate(matches):
        return True
    return False


def strict_match(word, letter_pool):
    _letter_pool = create_letter_pool(word)
    # print "word", word
    # print "_letter_pool", _letter_pool
    for x in _letter_pool:
        if x not in letter_pool:
            return False
        if letter_pool[x] < _letter_pool[x]:
            return False
    return True


def find_word(dictionary, pattern, rest_contains):
    # capture = "[" + ("".join(rest_contains)) + "]"

    letter_source = rest_contains
    for x in list(pattern):
        if x != ".":
            letter_source += str(x)

    letter_pool = create_letter_pool(letter_source)
    length = len(pattern)
    capture = "[" + rest_contains + "]"
    regex_pattern = str(pattern).replace(".", capture)
    regex = r"(" + regex_pattern + ")"
    # print "letter_source", letter_source
    # print "letter_pool", letter_pool

    print ("Dot-letter pattern given: \n\t%s" % pattern)
    print("Letters in pool: ")
    i = 0
    for x in letter_source:
        print "\t", x,
        i += 1
        if i > 3:
            print ''
            i = 0
    if i != 0:
        print ''

    print("Performing loose match ... ")
    result = list()
    it = 0
    with open(dictionary, "r") as f:
        for line in f:
            it += 1
            word = str(line).replace("\n", "")
            if loose_match(word, length, regex):
                result.append(word)
            print "\tProgress: %d, %s                  \r" % (it, word),
    print ''

    print("Result: %d/%d" % (len(result), it))
    i = 0
    for x in result:
        print "\t", x,
        i += 1
        if i > 3:
            print ''
            i = 0
    if i != 0:
        print ''

    print("Performing strict match ...")

    refined_result = list()
    for x in result:
        if strict_match(x, letter_pool):
            refined_result.append(x)

    print("Refined result: %d/%d" % (len(refined_result), len(result)))
    i = 0
    for x in refined_result:
        print "\t", x,
        i += 1
        if i > 3:
            print ''
            i = 0
    if i != 0:
        print ''


def print_help_and_exit():
    print u'''\
Hi there, I am a general and naïve solver for word guessing games.
Written by Makito Sumi, 2017

Usage: %s <dictionary> <dot-letter pattern> <letters in pool>\
''' % sys.argv[0]
    exit(0)


if len(sys.argv) == 4:
    find_word(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print_help_and_exit()
