
import string , unittest

from unittest import TestCase

from code_generator import CodeGenerator , generate_code


class TestCodeGeneration(TestCase):
	def test_SimpleCodeGeneration(self):
		code = generate_code( length = 5 , capitalize = True   )

		self.assertTrue(code.isupper())



class TestCodeGenerator(TestCase):

	def test_NewCode(self):
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