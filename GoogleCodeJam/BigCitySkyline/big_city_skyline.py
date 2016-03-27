#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to solve the Google Code Jam "Big City Skyline" puzzle:
    http://static.googleusercontent.com/media/services.google.com/en//blog_resources/Google_CodeJam_Practice.pdf

Usage: big_city_skyline <input_file>
"""

import copy



#  class for an active block
class Block(object):
    def __init__(self, start, width, height):
        """Start a new block.

        start   is the start coordinate of this block
        height  is the height of the block
        """

        self.start = start              # left-most column of block
        self.height = height            # height of block
        self.area = None                # used only when block is closed

    def __str__(self):
        return 's=%d, h=%d, a=%s' % (self.start, self.height, str(self.area))


def build_city(width_height):
    """Solve the Big City Skyline problem.

    width_height  a list of (width, height) tuples

    Return the area of the largest block.
    """

#    print('build_city: width_height=%s' % str(width_height))

    # a list holding all open blocks
    open_blocks = []

    # a reference to the single closed block
    closed_block = None

    #height of last buiding added
    last_height = None

    # current column number
    current_column = None

    for (w, h) in width_height:
#        print('Adding block: width=%d, height=%d' % (w, h))
        if last_height is None:
#            print('First block')
            # first building, initialize
            new_block = Block(0, w, h)
            open_blocks.append(new_block)
            last_height = h
            current_column = w
        else:
            if h > last_height:
#                print('Bigger height block')
                # start a new open block
                new_block = Block(current_column, w, h)
                open_blocks.append(new_block)
                # extend all open blocks (nothing to do)
                # update state
                last_height = h
                current_column += w
            elif h == last_height:
#                print('Same height block')
                # extend all open blocks (nothing to do)
                # update state
                current_column += w
            else:       # h < last_height
#                print('Smaller height block')
                # put copy of open blocks > h into a closed list
                closed = []     # list of blocks that will be closed
                for b in open_blocks:
#                    print('looking at b: %s, h=%s' % (str(b), h))
                    if b.height > h:
#                        print('1. closing block %s' % str(b))
                        new_closed = copy.deepcopy(b)
                        new_closed.area = (current_column - b.start) * b.height
                        closed.append(new_closed)
#                        print('1. closed=%s' % str([str(x) for x in closed]))

                # ensure largest closed is referred to by 'closed_block'
                for b in closed:
                    if closed_block is None:
                        closed_block = b
                    elif b.area > closed_block.area:
                        closed_block = b
                closed = []             # flush the refs in 'closed'

                # modify open blocks to new lower height, keep only largest
                delete = []
                largest = None
                for b in open_blocks:
#                    print('looking at b: %s, h=%s' % (str(b), h))
                    if b.height > h:
#                        print('2. lowering block %s' % str(b))
                        b.height = h
                        area = (current_column - b.start) * b.height
                        if largest is None:
                            largest = b
                        else:
                            if area > (current_column - largest.start) * largest.height:
                                delete.append(largest)
                                largest = b
                            else:
                                delete.append(b)

                # now delete all in 'delete' from open_blocks
                for b in delete:
                    open_blocks.remove(b)

                # update state
                last_height = h
                current_column += w

#        print('After:\n\tcurrent_column=%d\n\topen_blocks=%s\n\tclosed_block=%s'
#              % (current_column, str([str(x) for x in open_blocks]), str(closed_block)))

    # return area of largest block
    result = 0
    for b in open_blocks:
        b_area = (current_column - b.start) * b.height
#        print('3. looking at open_blocks b: %s, area=%d' % (str(b), b_area))
        if b_area > result:
#            print('3. new largest area=%d' % b_area)
            result = b_area
    if closed_block and closed_block.area > result:
#        print('3. closed_block is greater, area=%d' % closed_block.area)
        result = closed_block.area

    return result


def main(input_file):
    """Solve the Big City Skyline problem.

    input_file  the input data file

    The solution is written to standard output:
        y
    where y is the area of the largest possible block.

    Note that the problem statement specifies that the number of buildings N
    is on the first line and the N width/height pairs occupy the second line.
    Because python makes this easy, we allow newlines anywhere in the input
    except within a number.
    """
    
    # read file into memory, removing trailing '\n'
    with open(input_file, 'rb') as handle:
        l = handle.readlines()
    lines = [ll.strip() for ll in l]

    # split data on space, convert to ints
    numbers = []
    for l in lines:
        l = l.strip()
        n = l.split()
        numbers.extend(n)

    numbers = [int(x) for x in numbers]

    # gather into final form: N and [(W1,H1),...,(Wn,Hn)]
    N = int(numbers[0])
    numbers = numbers[1:]
    if len(numbers) != 2*N:
        print('ERROR: width+height numbers list is wrong length')
        sys.exit(10)
    width_height = zip(numbers[0::2], numbers[1::2])

    result = build_city(width_height)

    print('%d' % result)

    return 0

##############################################################################

if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    # to help the befuddled user
    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print(__doc__)

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)
        sys.exit(1)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'h', ['help'])
    except getopt.error:
        usage()
        sys.exit(1)

    for (opt, param) in opts:
        if opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    # check for the input file
    if len(args) != 1:
        usage()
        sys.exit(1)
    input_file = args[0]

    # run the program code
    result = main(input_file)
    sys.exit(result)

