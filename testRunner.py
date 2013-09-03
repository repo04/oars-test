#!/usr/bin/env python
import sys, argparse
#from selenium import webdriver
sys.path.insert(0, './src/')
from fillData import Filler

parser = argparse.ArgumentParser()

#command line arguments
#input order does not matter
parser.add_argument("--test", "-T",    action="store", type=str, required=True)
parser.add_argument("--driver", "-D",     action="store", type=str, required=True)
#parser.add_argument("--program", "-P", action="store", type=str, required=True) #unnecessary as of now
parser.add_argument("--url", "-U",     action="store", type=str, required=True)
parser.add_argument("--os", "-OS",     action="store", type=str, required=True)

args = parser.parse_args()

arg_map = {}
arg_map['test'] = args.test #name of the python module containing the test you would like to run
#arg_map['program'] = args.program 
arg_map['url'] = args.url #the url for the program
arg_map['driver'] = args.driver	#store webdriver name
arg_map['data'] = Filler(args.url) #instantiate and store Filler; used for inputting data on forms
arg_map['os'] = args.os # the OS on which the program will run

sys.path.insert(0, './src/tests/')
t = __import__(arg_map['test']) #used to load test using command line argument

#refer to userNames.py to configure username/password
test = t.test(arg_map)	#start setup/test