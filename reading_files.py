#-----------------------------------
#FP2-L01 Reading_files.py
#Zach Ignacio
#A simple .txt file with some information
#A python program that opens, reads, and interacts with information from that file, then closes
#------------------------------------


#------Functions-------
def read_all():
    #import a file to read
    file = open('rainbow.txt', 'r')
    all_lines = file.read()
    
    #print the variable (whole document)
    print(all_lines)
    
    #close the file
    file.close()
    
def list_file():
    file = open('rainbow.txt', 'r')
    #saves file to list
    color_list = file.readlines()
    print(color_list)
    
    rainbow = (color_list[4])
    print("The fifth color of the rainbow is", rainbow)
    
    #close the file
    file.close()
    
def read_all_lines():
    file = open('rainbow.txt', 'r')
    line = file.readline()
    print(line)
    
    line2 = file.readline()
    print(line2)
    
    file.close()
    
def main():      # main function code
    read_all()
    list_file()
    read_all_lines()

#-------Main Code-------

main()
    
    
    
    