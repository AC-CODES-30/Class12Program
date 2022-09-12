#Program 6
'''Write a menu-driven program to read the file names from ‘...\fileNames.txt’
and print the number of lines and words in each file. Output should look like:
<File name>
_____ lines in the file
______ words in the file
'''
def print_filename():
    myfile=open("prgm6.txt",'r')
    for line in myfile:
        line=line.rstrip('\n')
        print('File name:',line)
    myfile.close()

def print_file_lines():
    myfile1=open('prgm6.txt','r+')
    for l1 in myfile1:
        l1=l1.rstrip('\n')
        print('File name:',l1)
        mf1=open(l1,'r')
        lines=mf1.readlines()
        len_lines=len(lines)
        print('No. of lines in the file:',len_lines)
    mf1.close()
    myfile1.close()

def print_file_words():
    myfile2=open('prgm6.txt','r+')
    for l2 in myfile2:
        l2=l2.rstrip('\n')
        print('File name:',l2)
        mf2=open(l2,'r')
        count=0
        lines=mf2.readlines()
        #print(lines)
        for l2 in lines:
            words=l2.split()
            #print(words)
            count+=len(words)
        print('No. of words in the file:',count)

print('1. To print the file name')
print('2. To print the number of lines in the file')
print('3. To print the number of words in the file')

while True:
    ch=int(input('Enter your choice:'))
    if ch==1:
        print_filename()
    elif ch==2:
        print_file_lines()
    elif ch==3:
        print_file_words()
    else:
        print('Wrong choice')
        break
