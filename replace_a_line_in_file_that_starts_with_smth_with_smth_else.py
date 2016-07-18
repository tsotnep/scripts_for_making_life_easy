#usage:
    # python replace_a_line_in_file_that_starts_with_smth.py FILENAME OLD_LINE_THAT_STARTS_WITH_STRING_WRITTEN_HERE NEW_LINE_TEXT
        #you should not put spaces in a single argument
    # python replace_a_line_in_file_that_starts_with_smth.py OLD_LINE_THAT_STARTS_WITH_STRING_WRITTEN_HERE NEW_LINE_TEXT
        #you should not put spaces in a single argument
    # python replace_a_line_in_file_that_starts_with_smth.py
        #you have to change the script, and modify the arguments manually, lines 24-29



import fileinput
import sys

# a function that replaces a line that starts with : CHANGE_LINE_STARTING_WITH with a line : WITH_THIS_NEW_COMMAND, and takes FILENAME as argument
def REPLACE_WITH_NEW_COMMAND (filename):
    for line in fileinput.input(filename, inplace=True):
        if line.strip().startswith(CHANGE_LINE_STARTING_WITH):
            print WITH_THIS_NEW_COMMAND
        else:
            line = line.rstrip('\n')
            print line

#if you give no parameter, this will execute
if len(sys.argv) == 1:
    CHANGE_LINE_STARTING_WITH='asd'
    WITH_THIS_NEW_COMMAND='HEY'
    for v in ["CV_INT","CV_REAL", "S_INT", "S_INT_G", "S_REAL"]:
        REPLACE_WITH_NEW_COMMAND("tb/TB_MATRIX_MUL_IP_CORE_"+v+".vhd")



#if you give two parameters loop here will be used
if len(sys.argv) == 3:
    CHANGE_LINE_STARTING_WITH=sys.argv[1]
    WITH_THIS_NEW_COMMAND=sys.argv[2]
    for v in ["CV_INT","CV_REAL", "S_INT", "S_INT_G", "S_REAL"]:
        REPLACE_WITH_NEW_COMMAND("tb/TB_MATRIX_MUL_IP_CORE_"+v+".vhd")


#if you give four parameters, first will be name of the file
if len(sys.argv) == 4:
    REPLACE_WITH_NEW_COMMAND(sys.argv[1])
    CHANGE_LINE_STARTING_WITH=sys.argv[2]
    WITH_THIS_NEW_COMMAND=sys.argv[3]

#example of for loops:

    # for v in range(4):
        # REPLACE_WITH_NEW_COMMAND("router/Router_v"+`v`+".tcl")

    # for v in ["ARBITER", "FIFO", "LBDR", "XBAR"]:
        # REPLACE_WITH_NEW_COMMAND("units/"+v+".tcl")
