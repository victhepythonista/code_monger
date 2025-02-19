
import string , unittest

from unittest import TestCase

from code_monger import CodeGenerator , generate_code


class TestCodeGeneration(TestCase):
	def test_SimpleCodeGeneration(self):
		'''
		check if a code is generated or not 
		'''
		code = generate_code(  )
		self.assertTrue(type(code) == str and len(code) > 0 )


	def test_CustomCodeGeneration(self):
		'''
		Checking if different parameters during custom code generation are considered 
		'''
		# code length
		none_special_chartachters = string.ascii_uppercase + string.ascii_lowercase + string.digits
		code = generate_code(length = 20  )
		self.assertTrue(len(code) == 20 )
		# check letter casing
		code  = generate_code(capitalize = True , numbers = False , letters = True )
		self.assertTrue(code.isupper())
		code  = generate_code(capitalize = False ,letters = True , numbers = False)
		self.assertTrue(code.islower())
		# check numbers only
		code = generate_code(numbers = True , letters = False)
		self.assertTrue(code.isnumeric())
		# check code generation with  special charachters 
		code = generate_code(punctuation_chars = True  , letters = False , numbers = False)
		self.assertTrue(all(  [  (char not in none_special_chartachters) for char in code   ] ))


	def test_CodeClearance(self):
		test_file = "codes_test_file.txt"
		cg = CodeGenerator(test_file)

class TestCodeGenerator(TestCase):

	def test_NewCode(self):
		'''
		Testing the CodeGenerator class functionality 

		'''
		test_file = "./test_data/codes.txt"
		test_key_string = "myemail@gmail.com"
		cg = CodeGenerator(test_file)
		code = cg.NewCode(test_key_string  , length = 13)
		self.assertTrue(len(code) == 13)
		file_data = ''
		with open (test_file , "r") as f:
			file_data = f.read()
		self.assertTrue(code in file_data)
		validation_result = cg.ValidateCode(code , test_key_string)
		self.assertTrue(validation_result == True)
		with open (test_file , "r") as f:
			file_data = f.read()
		# chec if the code was deleted after validation
		self.assertTrue(code not in file_data)


if __name__ == '__main__':
	unittest.main()