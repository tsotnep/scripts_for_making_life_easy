FileName=file.txt

#print the content of file and save it in a variable $a
    a=$(cat $FileName )

#save it into a file.
    #all capital : "${a^^}"`
    #all lowercase : "${a,,}"`
    echo "${a,,}" > converted_$FileName

#in case you want to use that in shell, then use that commands by yourself.
    #export b=`echo "${a,,}"`

#then open ATOM editor
	# ctrl + F
	# search for underscore _
	# alt + enter
	# select all characters next to underscore
	# ctrl + k + u
