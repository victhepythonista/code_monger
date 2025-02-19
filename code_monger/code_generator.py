# product id manage here 




import uuid,os
from string import ascii_uppercase, digits , printable , punctuation , whitespace ,ascii_lowercase
from random import choice 
from io import StringIO
import datetime as dt


def generate_code( length = 10 ,  numbers = True , letters = False , punctuation_chars = False , capitalize =False , random_case = False):
    '''
    Make a code as per the specifications and return it
    '''
    bool_parameters_chosen =  numbers , letters , punctuation ,capitalize ,random_case
    contents = ""
    if numbers:
        contents += digits
    if letters:
        contents += ascii_lowercase
    if punctuation_chars:
        contents += punctuation  
    if capitalize:
        contents = contents.upper()
    elif random_case:
        contents += ascii_uppercase # lowecase is already added 

    cache = ""
    if contents == "":
        contents = ascii_uppercase + ascii_lowercase + digits + punctuation
    while True:
        for i in range(0, length):
            cache += choice(contents)
        return cache



class CodeGenerator:
    def __init__(self , storage_file):
        self.storage_file = storage_file
        self.CheckStorage()

    def  NewCode(self, key_string ,length = 10 ,  numbers = True , letters = False , punctuation_chars = False , capitalize =False , random_case = False ) -> str:
        '''
        Generate a new code , store it in a file and return the code
        '''
        self.CheckStorage()
        data_file = self.storage_file
        with open(data_file, "r") as f :
            lines = f.readlines()
        lines = [s.strip() for s in lines]
        contents = digits + ascii_uppercase
        while True:
            cache = generate_code( length = length , numbers = numbers , letters = letters , punctuation_chars =punctuation , capitalize = capitalize)
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
        self.CheckStorage()
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

    def ClearCodes(self ,delete = False ):
        ''' 
        This methods removes all the codes from the storage file . 
        set delete to True to delete the file 
        '''
        if delete:
            # delete the storage file
            try:
                os.remove(self.storage_file)
            except Exception as e:
                print("Could not delete {} because of {}".format(self.storage_file ,e))
                raise
            return
        # overwrite the data in the storagefile
        with open(self.storage_file , "w") as f:
            f.write("")

    def CheckStorage(self):
        '''
        Ensure that the storage file is present , if not, attempt to create it

        '''
        storage_file = self.storage_file
        if not os.path.isfile(storage_file):
            print("Storage file {} is non-existent , attempting to create ".format(storage_file), end = "")
            try:
                missing_folder , missing_file  = os.path.split(storage_file)
                if missing_folder:
                    if not os.path.isdir(missing_folder):
                        os.makedirs(missing_folder)
                with open( storage_file , "w") as f:
                    f.write("")
                print("DONE")
            except Exception as e:
                print("ERROR")
                print("Error creating the storage file because of {}  Error".format(e))
                raise


if __name__ == '__main__':
    print(NewSerialNo(10))