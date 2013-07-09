#!/usr/bin/env python
import sys
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

sys.path.insert(0, './src/test/')
t = __import__(arg_map['test'])

test = t.test(arg_map)