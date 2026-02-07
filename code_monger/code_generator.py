# product id manage here 




import uuid,os
from string import ascii_uppercase, digits , printable , punctuation , whitespace ,ascii_lowercase
from random import choice 
from io import StringIO
import datetime as dt


valid_casing_values = ['all' , "upper" ,'lower']
UNWANTED_CHARACHTERS = '''"','''
def generate_code( length = 10 ,  numbers = False , letters = False , punctuation_chars = False , casing = "all"):
    '''Makes a code following the parameters provided

    Parameters
    ----------
    length:int
        length of the code to be generated
    numbers:bool
        set to [True] to Include integers during code generation
    letters:bool
        set to [True] to Include english alphabet letters
    punctuation_chars:bool
        set to [True] to include punctuation characters  
    casing:str
        Choice of casing for the code generated , it can only be one of these :
            > 'lower' - Lowercase only
            > 'upper' - Uppercase only
            > 'all'   - Mix uppercase and lowercase
        If an invalid value is provided, the value is reset to 'all'

    Returns
    -------
    str
        the generated code is returned as a string object

    '''

    contents = ""
    casing = casing.strip().lower()
    if not casing in valid_casing_values:
        casing = "all"
    if numbers:
        contents += digits
    if letters:
        if casing == "all":
            contents += ascii_uppercase + ascii_lowercase
        elif casing == "upper":
            contents += ascii_uppercase
        elif casing == "lower":
            contents += ascii_lowercase
    if punctuation_chars:
        contents += punctuation  
    cache = ""
    if contents == "":
        contents = ascii_uppercase + digits  
    contents = "".join([ char for char in contents if not char in UNWANTED_CHARACHTERS])
    while True:
        for i in range(0, length):
            cache += choice(contents)
        return cache



class CodeGenerator:
    def __init__(self , storage_file):
        self.storage_file = storage_file
        self.CheckStorage()


    def  NewCode(self, key_string ,length = 10 ,  numbers = True , letters = False , punctuation_chars = False , casing = "all" ) -> str:
        '''
        Generate a new code , store it in a file and return the code

         Parameters
        ----------
        key_string:str
            A string that will act as an identifier of the code ownership during validation
            An example is an email_address, or a username 
        length:int
            length of the code to be generated
        numbers:bool
            set to [True] to Include integers during code generation
        letters:bool
            set to [True] to Include english alphabet letters
        punctuation_chars:bool
            set to [True] to include punctuation characters  
        casing:str
            Choice of casing for the code generated , it can only be one of these :
                > 'lower' - Lowercase only
                > 'upper' - Uppercase only
                > 'all'   - Mix uppercase and lowercase
            If an invalid value is provided, the value is reset to 'all'

        Returns
        -------
        str
            the generated code is returned as a string object

        '''
        self.CheckStorage()
        data_file = self.storage_file
        with open(data_file, "r") as f :
            lines = f.readlines()
        lines = [s.strip() for s in lines]
        contents = digits + ascii_uppercase
        while True:
            cache = generate_code( length = length , numbers = numbers , letters = letters , punctuation_chars =punctuation , casing = casing)
            if not cache  in lines:
                lines.append(key_string +","+ cache)
                with open(data_file, 'w') as f:
                    for char in lines:
                        f.write(char + "\n")
                return cache

    def GetKey(
        self, 
        code
        ):
        ''' Fetches the key string that matches the  code provided

        Paramaters
        ----------
        self
        code:str
            The code to match

        Returns
        -------
        key_string:the key attached to the code , '' if none
        '''
        key_string = ''
        file = self.storage_file
        self.CheckStorage()
        if not os.path.isfile(file):
            return key_string
        with open(file, "r") as f:
            data = f.readlines()
        info = []
        lines = [s.strip() for s in data]
        for l in lines:
            vals = l.split(',')
            if not len(vals)>1:
                continue
            ks = vals[0] # fetch the key tring in the line
            value = vals[1].replace("\n",'')
            if value == code  :
                key_string = ks 
                break
        return key_string

    def ReplaceKey(
        self,
        old_key:str,
        new_key:str)->bool:
        """Replace the code associated with the old_key with new_key.


        Parameters
        ----------
        old_key:str
            The existing key 
        new_key:str
            The new replacement key 
            

        Returns
        -------
        outcome:bool
            Whether or not the key has been successfully replaced 

        """
        file = self.storage_file
        self.CheckStorage()
        if not os.path.isfile(file):
            return False
        with open(file, "r") as f:
            lines = [s.strip() for s in f.readlines()]

        new_lines = []
        for line in lines:
            vals = line.split(',')
            if vals[0] == old_key:  # Replace old_key with new_key
                new_lines.append(f"{new_key},{vals[1]}")
            else:
                new_lines.append(line)
        with open(file, "w") as f:
            f.writelines(f"{line}\n" for line in new_lines)
        return True

    def GetCode(
        self, 
        key_string:str
        )->str:
        ''' Fetches the value assigned to the key string in self.storage_file

        Parameters
        ----------
        self
        key_string:str
            The value used to store a code
        
        Returns
        --------
        value:str
            The value assigned to key_string , '' if none was found
        '''
        value = ''
        file = self.storage_file
        self.CheckStorage()
        if not os.path.isfile(file):
            return value
        with open(file, "r") as f:
            data = f.readlines()
        info = []
        lines = [s.strip() for s in data]
        for l in lines:
            vals = l.split(',')
            if not len(vals)>1:
                continue
            ks = vals[0] # fetch the key tring in the line
            value = vals[1].replace("\n",'').strip()
            if key_string == ks  :
                return value 
        return value


    def DeleteKey(
        self,
        key_string:str
        )->None:
        """ Delete the line with the specific key in self.storage_file 

        Parameters
        ----------
        key_string:str
            The key string to remove
        Returns
        -------
        None

        """
        file = self.storage_file
        self.CheckStorage()
        if not os.path.isfile(file):
            return value
        with open(file, "r") as f:
            data = f.readlines()
        info = []
        lines = [s.strip() for s in data]
        for l in lines:
            vals = l.split(',')
            if not len(vals)>1:
                continue
            ks = vals[0]
            value = vals[1].replace("\n",'')
            if ks == key_string:
                lines.remove(l) # remove the line
                continue
        # write the new lines 
        with open(file, "w") as f:
            for l in lines:
                f.write(l )


    def DeleteCode(
            self ,
            code)->None:
        ''' Delete the line with the code in self.storage_file

        Paramaters
        ----------
        code:str
            The code to delete from the file

        Returns
        --------
        None

        ''' 
        file = self.storage_file
        self.CheckStorage()
        if not os.path.isfile(file):
            return value
        with open(file, "r") as f:
            data = f.readlines()
        info = []
        lines = [s.strip() for s in data]
        for l in lines:
            vals = l.split(',')
            if not len(vals)>1:
                continue
            value = vals[1].replace('\n','')
            if code == value:
                lines.remove(l) # remove the line
                continue
        # write the new lines 
        with open(file, "w") as f:
            for l in lines:
                f.write(l )


    def ValidateCode(
            self,
            code:str ,
            key_string:str ,
            delete_if_valid:bool =  True
              )-> bool:
        """
        Check if a code exists in the storage file . 
        if delete_if_valid is True , the code is deleted from the file .

        Parameters
        ----------
        code:str
            The code that is to be vlaidated
        key_string:str
            The value used to store a code
            A string that will act as an identifier of the code ownership during validation
            An example is an email_address, or a username 
        delete_if_valid:bool
            set to [True] to delete the code after positive validation , 
            setting to [False] will leave the code in the file .   

        Returns
        -------
        validation_check:bool
            If the code matches the key string 
        """

        self.CheckStorage()
        value = self.GetCode( key_string)

        validation_check = value == code
        if validation_check and delete_if_valid:
            self.DeleteCode(code)
        return validation_check


       

    def ClearCodes(
            self,
            delete_file = False
             ):
        ''' 
        This methods removes all the codes from the storage file . 
        set delete to True to delete the file 

        Parameters
        ----------
        delete_file:bool
            Set to [True] to delete the storage file , [False] will just clear the file contents

        Returns
        -------
        None
        '''

        if delete_file:
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

        Returns
        -------
        None

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