import unittest
import glob
import sys

from chk_manuscript import *

import yaml


class TestsContainer(unittest.TestCase):
    longMessage = True

def make_test_function(name, line):
    def test(self):
        if re.match(r'\w+_TC\d', name):
            corrections = check(rules, line)
            #print(corrections)
            self.assertGreater(len(corrections), 0, name)
        elif re.match(r'\w+_FC\d', name):
            self.assertEqual(len(check(rules, line)), 0, name)
        else:
            sys.exit("Something's wrong with test cases!")
    return test


if __name__ == '__main__':
    rules = loadrules(glob.glob('*.json'))
    for filename in glob.glob('test/*.yaml'):
        with open(filename, 'r') as stream:
            try:
                parsed_yaml = yaml.safe_load(stream)
                caseid = re.search(r'test/(\w+).yaml', filename)[1]
                true_cases = parsed_yaml['true cases']
                if true_cases:
                    for i, case in enumerate(true_cases):
                        name = caseid +'_TC' + str(i)
                        test_func = make_test_function(name, case)
                        setattr(TestsContainer, f'test_{name}', test_func)
   
                false_cases = parsed_yaml['false cases']
                if false_cases:
                    for i, case in enumerate(false_cases):
                        name = caseid +'_FC' + str(i)
                        test_func = make_test_function(name, case)
                        setattr(TestsContainer, f'test_{name}', test_func)

            except yaml.YAMLError as e:
                print(e)
        
    unittest.main()
