def main():
    print('Hello, would you like to input, append or recieve info?')
    i = input('i or a or r\n')
    if i == 'i':
        write()

    elif i == 'r':
        print('Sorry, the programmer dosen\'t know how to do that yet. :)')
        
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
    inputText.close
    print('Success')

def recieve():
    pass

main()
