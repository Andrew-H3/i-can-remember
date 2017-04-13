#!/usr/bin/env python3.5
# ^ This line is neccesary on linux. Tested with Ubuntu 16.04 LTS with python verion: 3.5.2-2ubuntu0~16.04.1u
#You can remove if not needed

def main():
    print('Hello, would you like to input, append or recieve info?')
    i = input('i or a or r\n')
    if i == 'i':
        write()

    elif i == 'r':
        recieve()
        
    elif i == 'a':
        append()

    else:
        print('**Invailid choice**')
        main()

def write():
    text = input('Please input the text: \n-')
    inputText = open('input-text', 'w')
    inputText.write(text)
    inputText.close()
    print('Success')

def append():
    text = input('Please input the text: \n-')
    inputText = open('input-text', 'a')
    inputText.write('\n' + text)
    inputText.close()
    print('Success')

def recieve():
    text = open('input-text', 'r')
    rd = text.read()
    text.close()
    print(rd)


main()
