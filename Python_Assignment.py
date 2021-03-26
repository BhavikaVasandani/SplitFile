# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from faker import Faker

# To create a json file
import json		

# For student id
from random import randint	

fake = Faker()

def input_data(x):

	# dictionary
	student_data ={}
	for i in range(0, x):
		student_data[i]={}
		student_data[i]['id']= randint(1, 100)
		student_data[i]['name']= fake.name()
		student_data[i]['address']= fake.address()
		student_data[i]['latitude']= str(fake.latitude())
		student_data[i]['longitude']= str(fake.longitude())
	print(student_data)

	# dictionary dumped as json in a json file
	with open('students.json', 'w') as fp:
		json.dump(student_data, fp)
	

def main():


	number_of_students = 10000
	input_data(number_of_students)
main()
from faker import Faker

# To create a json file
import json		

# For student id
from random import randint	

fake = Faker()

def input_data(x):

	# dictionary
	student_data ={}
	for i in range(0, x):
		student_data[i]={}
		student_data[i]['id']= randint(1, 100)
		student_data[i]['name']= fake.name()
		student_data[i]['address']= fake.address()
		student_data[i]['latitude']= str(fake.latitude())
		student_data[i]['longitude']= str(fake.longitude())
	print(student_data)

	# dictionary dumped as json in a json file
	with open('students.json', 'w') as fp:
		json.dump(student_data, fp)
	

def main():


	number_of_students = 10000
	input_data(number_of_students)
main()

from faker import Faker

# To create a json file
import json		

# For student id
from random import randint	

fake = Faker()

def input_data(x):

	# dictionary
	student_data ={}
	for i in range(0, x):
		student_data[i]={}
		student_data[i]['id']= randint(1, 100)
		student_data[i]['name']= fake.name()
		student_data[i]['address']= fake.address()
		student_data[i]['latitude']= str(fake.latitude())
		student_data[i]['longitude']= str(fake.longitude())
	print(student_data)

	# dictionary dumped as json in a json file
	with open('students.xml', 'w') as fp:
		json.dump(student_data, fp)
	

def main():


	number_of_students = 10000
	input_data(number_of_students)
main()

from faker import Faker

# To create a json file
import json		

# For student id
from random import randint	

fake = Faker()

def input_data(x):

	# dictionary
	student_data ={}
	for i in range(0, x):
		student_data[i]={}
		student_data[i]['id']= randint(1, 100)
		student_data[i]['name']= fake.name()
		student_data[i]['address']= fake.address()
		student_data[i]['latitude']= str(fake.latitude())
		student_data[i]['longitude']= str(fake.longitude())
	print(student_data)

	# dictionary dumped as json in a json file
	with open('students.csv', 'w') as fp:
		json.dump(student_data, fp)
	

def main():


	number_of_students = 10000
	input_data(number_of_students)
main()

from fsplit.filesplit import Filesplit

fs = Filesplit()
def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))

fs.split(file="students.xml", split_size=2000000, output_dir="Downloads/CSVfile", callback=split_cb)

from fsplit.filesplit import Filesplit

fs = Filesplit()
def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))

fs.split(file="students.json", split_size=2000000, output_dir="Downloads/Jsonfile", callback=split_cb)

from fsplit.filesplit import Filesplit

fs = Filesplit()
def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))

fs.split(file="students.xml", split_size=2000000, output_dir="Downloads/Xmlfile", callback=split_cb)