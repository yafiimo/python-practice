# must use 'w' as 2nd argument to write to a file, and file_name as first argument
with open('text_files/write_file.txt', 'w') as write_file:
    text1 = 'Hello, I am writing my first line to a file using Python!'
    print('Writing first line to file...')
    write_file.write(text1)

# if you want to ammend a file, you must use the 'a' argument
with open('text_files/write_file.txt', 'a') as write_file:
    text2 = '\nWriting a second line into the text file.'
    print('Adding a second line to file...')
    write_file.write(text2)

quotes = [
    '\nI\'m so mean I make medicine sick'
    '\nThe best preparation for tomorrow is doing your best today'
    '\nI am always doing that which I cannot do, in order that I may learn how to do it'
]

# writing lines into a text file from list separated lines
with open('text_files/write_file.txt', 'a') as write_file:
    print('Adding quotes to file...')
    write_file.writelines(quotes)
