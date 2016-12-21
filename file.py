
textToWrite = 'line_one'

File = open( 'text', 'w')
File.write(textToWrite)
File.close()


textToAppend = '\nline_appended'

File = open( 'text', 'a')
File.write(textToAppend)
File.close()

readFile = open( 'text', 'r').read()
print( readFile)


readLines = open( 'text', 'r').readlines()
print('\n\n' + str(readLines))
