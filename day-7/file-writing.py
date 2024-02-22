
text_to_write = 'OOOOOOO\nthis is some text\ni like some stuff\n'

with open('file-writing.txt', 'w') as file:
    file.write(text_to_write)

text_to_append = '++++++ 11111 ++++++'

with open('file-writing.txt', 'a') as file:
    file.write(text_to_append)