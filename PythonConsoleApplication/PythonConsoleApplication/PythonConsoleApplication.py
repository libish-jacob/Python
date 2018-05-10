#!/usr/bin/python
def Main():
        print("Hello world");
        numberOfLines = int(input("Please enter the number of lines to read:"));
        file = open("C:\\Users\\jajac\\Desktop\\py\\Q.txt");
        lines = file.readlines();
        for x in lines:
            if numberOfLines != 0:
                print(x);
                print("\r");
                numberOfLines-= 1;
            else:    
                break;
            

        file.close();
        
if __name__ == "__man__":
    Main();
elif __name__ == "__main__":
    Main();
else:
    print("No way to go ahead.");    