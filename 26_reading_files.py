lorem_file = open('text_files/lorem_ipsum.txt')

# to read the file by looping through the lines
print('\nLooping method:\n')
for line in lorem_file:
    print(line.rstrip())                 # use rstrip to remove the extra line between each printed line, returns each line as a string

# to read the file again from the beginning, you must return to the
# beginning of the file
lorem_file.seek(0)

# to read each line in a file and store them in a list:
print('\nUsing readlines() method:\n')
lines = lorem_file.readlines()
print(lines)

# reading a specific number of characters from a particular point in the text
lorem_file.seek(202)
print('\nUsing read(n) method from character 202 to read 50 characters:\n')
print(lorem_file.read(50))
# if not argument is passed to read(), it will read to the end

lorem_file.close()

# using 'with open()' to eliminate the need to close the file
print('\nUsing "with open()" and readlines():\n')
with open('text_files/lorem_ipsum.txt') as lorem_file:
    lines = lorem_file.readlines()
    print(lines)
