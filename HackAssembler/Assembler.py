from Parser import Parser
from Translator import Translator

import sys

with open(sys.argv[2], 'r') as asmFile:
    parser = Parser(asmFile)
    translator = Translator()
    translator.Translate(parser.filteredAsm)
    translator.WriteToSource()