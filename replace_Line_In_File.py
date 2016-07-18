#usage:
    # python replace_A_Line_In_File.py    file_Name   old_text_starts_with    new_text
        #you should not put spaces in a single argument
    # python replace_A_Line_In_File.py    old_text_starts_with    new_text
        #you should not put spaces in a single argument
        #you should change lines in statement: if len(sys.argv) == 3:
    # python replace_A_Line_In_File.py
        #you should change lines in statement: if len(sys.argv) == 1:

#result of : python replace_A_Line_In_File.py file.txt XX YYY
    # file.txt -content before:
        #XX
        #XXaa
        #XXXAAA
        #XXXvbds
        #X
        #YYYY
        #XXXX
    # file.txt -after script
        #YYY
        #YYY
        #YYY
        #YYY
        #X
        #YYYY
        #YYY



import fileinput
import sys

# a function that replaces a line that starts with : old_text_starts_with with a line : new_text, and takes file_Name as argument
def Replace_Line_In_File (file_Name):
    count = 0
    for line in fileinput.input(file_Name, inplace=true):
        if line.strip().startswith(old_text_starts_with):
            print new_text
            count+=1
        else:
            line = line.rstrip('\n')
            print line
    print ("in file: \"" + file_Name + "\" changed that many: " + str(count))

#if you give no parameter, this will execute
if len(sys.argv) == 1:
    old_text_starts_with='XX'
    new_text='YYY'
    for v in ["CV_INT","CV_REAL", "S_INT", "S_INT_G", "S_REAL"]:
        Replace_Line_In_File("tb/TB_MATRIX_MUL_IP_CORE_"+v+".vhd")



#if you give two parameters loop here will be used
if len(sys.argv) == 3:
    old_text_starts_with=sys.argv[1]
    new_text=sys.argv[2]
    for v in ["CV_INT","CV_REAL", "S_INT", "S_INT_G", "S_REAL"]:
        Replace_Line_In_File("tb/TB_MATRIX_MUL_IP_CORE_"+v+".vhd")


#if you give four parameters, first will be name of the file
if len(sys.argv) == 4:
    old_text_starts_with=sys.argv[2]
    new_text=sys.argv[3]
    Replace_Line_In_File(sys.argv[1])

#example of for loops:

    # for v in range(4):
        # Replace_Line_In_File("router/router_V"+`v`+".tcl")

    # for v in ["arbiter", "fifo", "lbdr", "xbar"]:
        # Replace_Line_In_File("units/"+v+".tcl")
