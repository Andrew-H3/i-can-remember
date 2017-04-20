#!/usr/bin/env python3.5
# ^ This line is only needed if you wish to run the script from the linux terminal.

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
