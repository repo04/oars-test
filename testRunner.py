#!/usr/bin/env python

import sys
sys.path.insert(0, './src/test/')
import testLogin
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", "-T",    action="store", type=str, required=True)
parser.add_argument("--program", "-P", action="store", type=str, required=True)
parser.add_argument("--url", "-U",     action="store", type=str, required=True)
args = parser.parse_args()

test    = args.test
program = args.program
url     = args.url

test = testLogin.testLogin()

def __init__(self, test, program, url):
  self.test    = test
  self.program = program
  self.url     = url

