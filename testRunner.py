#!/usr/bin/env python

import sys
sys.path.insert(0, './src/test/')
import testLogin
import argparse
from selenium import webdriver

parser = argparse.ArgumentParser()
parser.add_argument("--test", "-T",    action="store", type=str, required=True)
parser.add_argument("--program", "-P", action="store", type=str, required=True)
parser.add_argument("--url", "-U",     action="store", type=str, required=True)
args = parser.parse_args()

arg_map = {}
arg_map['test'] = args.test
arg_map['program'] = args.program
arg_map['url'] = args.url
arg_map['driver'] = webdriver.Firefox()

test = testLogin.test_login(arg_map)

def __init__(self, test, program, url):
  self.test    = test
  self.program = program
  self.url     = url

