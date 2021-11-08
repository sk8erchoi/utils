import os
import argparse
import chk_manuscript

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="filename", type=str)
parser.add_argument("-r", "--rulefile", nargs='+', 
                    default=['ko_spelling_rules.json', 'ko_spacing_rules.json', 'foreign_sound_rules.json'])
args = parser.parse_args()

chk_manuscript.main(args.filename, args.rulefile)