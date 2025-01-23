'''
Send a response based on user input

'''
from time import sleep

while(1):
    sleep(1)
    print(f'`')
    inp = input()
    if(inp == "F"):
        print(inp)
        break
    else:
        print(f'`')
