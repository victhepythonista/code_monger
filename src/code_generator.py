# product id manage here 




import uuid,os
from string import ascii_uppercase, digits , printable
from random import choice 
from io import StringIO
import datetime as dt


def generate_code( length = 10 ,  numbers = True , letters = True , special_charachters = False , capitalize =False):
    '''
    Make a code as per the specifications and return it
    '''
    contents = ""
    if numbers:
        contents += digits
    if letters:
        contents += ascii_uppercase
    if special_charachters:
        contents = printable
    if capitalize:
        contents = contents.upper()
    cache = ""
    while True:
        for i in range(0, length):
            cache += choice(contents)
        return cache



class CodeGenerator:
    def __init__(self , storage_file):
        if not os.path.isfile(storage_file):
            try:
                missing_folder , missing_file  = os.path.split(storage_file)
                if not os.path.isdir(missing_folder):
                    os.makedirs(missing_folder)
                with open( storage_file , "w") as f:
                    f.write("")
                    print("File  created sucessfully")
            except Exception as e:
                print("Error creating the storage file because of {}   ".format(e))
                raise
        self.storage_file = os.path.abspath(storage_file)
 
        
    def  NewCode(self, key_string ,length = 10 ,  numbers = True , letters = True , special_charachters = False , capitalize =False  ):
        '''
        Generate a new code , store it in a file and return the code
        '''
        data_file = self.storage_file
        with open(data_file, "r") as f :
            lines = f.readlines()
        lines = [s.strip() for s in lines]
        contents = digits + ascii_uppercase
        while True:
            cache = generate_code( length = length , numbers = numbers , letters = letters , special_charachters = special_charachters , capitalize = capitalize)
            if not cache  in lines:
                lines.append(key_string +","+ cache)
                with open(data_file, 'w') as f:
                    for char in lines:
                        f.write(char + "\n")
                return cache

     
     
    def ValidateCode(self, code , key_string , delete_if_valid =  True  )-> None:
        """
        Check if a code exists in the storage file . 
        if delete_if_valid is True , the code is deleted from the file
        """
        file = self.storage_file
        if not os.path.isfile(file):
            with open(file, "w") as f:
                f.write("")
        with open(file, "r") as f:
            data = f.readlines()
        info = []
        lines = [s.strip() for s in data]
        for l in lines:
            vals = l.split(',')
            ks = vals[0]
            cd = vals[1]
            if key_string == ks and code == cd :
                if delete_if_valid:
                    lines.pop(lines.index(l))
                with open(file, "w") as f:
                    for l in lines:
                        f.write(l+"\n")
                return True
        return False

     
 
 

if __name__ == '__main__':
    print(NewSerialNo(10))