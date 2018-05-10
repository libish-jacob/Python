#!/usr/bin/python

from Helper.FileHelper import FileHelper

def Main():
        print("Hello world");
        numberOfLines = int(input("Please enter the number of lines to read:"));
        fileHelper = FileHelper("Input.txt");
        lines = fileHelper.ReadFile();

        for x in lines:
            if numberOfLines != 0:
                print(x);
                print("\r");
                numberOfLines-= 1;
            else:    
                break;
        
if __name__ == "__man__":
    Main();
elif __name__ == "__main__":
    Main();
else:
    print("No way to go ahead.");    