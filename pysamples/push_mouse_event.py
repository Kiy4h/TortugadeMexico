#Copyright (c) 2009-10, Walter Bender, Tony Forster

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#
# This procedure is invoked when the user-definable block on the "extras"
# palette is selected.

def myblock(lc, x):

    ###########################################################################
    #
    # Push mouse event to stack
    #
    ###########################################################################

    if lc.tw.mouse_flag == 1:
        # push y first so x will be popped first
        lc.heap.append((lc.tw.canvas.height / 2) - lc.tw.mouse_y)
        lc.heap.append(lc.tw.mouse_x - (lc.tw.canvas.width / 2))
        lc.heap.append(1) # mouse event
        lc.tw.mouse_flag = 0
    else:
        lc.heap.append(0) # no mouse event