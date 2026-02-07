

import string , unittest , os

from unittest import TestCase

from code_monger import CodeGenerator , generate_code


test_file = 'test_data/test_fetching_and_deletion.txt'
test_key_string = "testkeystring"


if os.path.isfile(test_file):
	with open(test_file ,"w") as f:
		f.write('')

class Test_Code(TestCase):
	def test_get_code(self):
		cg = CodeGenerator(test_file)
		cg.ClearCodes()
		cg.NewCode(test_key_string)
		code = cg.GetCode(test_key_string)
		lines_read = []
		with open(test_file , "r") as f:
			lines_read = f.readlines()
		self.assertTrue(len(lines_read) == 1)
		self.assertTrue(lines_read[0].split(",")[1].replace("\n",'') == code)

	def test_CodeClearance(self):
		'''Test if code clearance works '''
		test_file = "test_data/codes_test_file.txt"
		cg = CodeGenerator(test_file)
		cg.NewCode("test_key_string")
		cg.ClearCodes()
		with open(test_file , "r") as f:
			self.assertTrue(f.read() == '')


	def test_delete_code(self):
		cg = CodeGenerator(test_file)
		code = cg.NewCode(test_key_string)
		cg.DeleteCode(code)
		self.assertFalse(cg.ValidateCode(code , test_key_string , delete_if_valid=False))
		self.assertTrue(cg.GetCode(test_key_string) == '')
		self.assertTrue(cg.GetKey(code) == '')

 


class Test_Key(TestCase):
	''' key related tests
	'''

	def test_delete_key(self):
		cg = CodeGenerator(test_file)
		cg.ClearCodes()
		code = cg.NewCode(test_key_string)
		cg.DeleteKey(test_key_string)
		self.assertTrue(cg.GetKey(code) == '')
		self.assertFalse(cg.ValidateCode(code , test_key_string , delete_if_valid=False))
		self.assertTrue(cg.GetCode(test_key_string) == '')


	def test_get_key_string(self):

		cg = CodeGenerator(test_file)
		cg.ClearCodes()
		code = cg.NewCode(test_key_string)
		key_string = cg.GetKey(code)
		self.assertTrue(key_string == test_key_string)

	def test_Replace_key_string(self):
		'''
		test to see if key replacement  works'''

		cg = CodeGenerator(test_file)
		cg.ClearCodes()
		code = cg.NewCode(test_key_string)
		new_key_string = "replacement"
		cg.ReplaceKey(test_key_string , new_key_string)
		# check if the new key has been written
		self.assertTrue(cg.GetCode(new_key_string) == code)
		with open(cg.storage_file , "r") as f:
			self.assertTrue(new_key_string in f.read() )


	 