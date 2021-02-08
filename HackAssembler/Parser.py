import re
import Instructions
import SymbolTable
import Translator

class Parser(object):
    A_INSTRUCTION = '^@\d+|//$'
    SYMBOLIC_DATA = '^@[a-zA-Z._\$\d]+|//$'
    COMMENT_LINE = '^//'
    INNER_COMMENT = '//'
    LABEL_SYMBOL = '^\((.*?)\)'

    def __init__(self, asmFile=None):
        if asmFile != None:
            self.rawAsm = asmFile.readlines()
            self.filteredAsm = self.RemoveCommentsWhiteSpaces(self.rawAsm)
            self.BuildSymbolTable(self.filteredAsm)

    def RemoveCommentsWhiteSpaces(self, asmFile):
        code = []
        for _ in asmFile:
            line = _.replace(" ", "").replace("\n", "")
            if self.IsAInstruction(line):
                code.append(self.IsAInstruction(line).group(0))
            elif self.IsSymbol(line):
                code.append(self.IsSymbol(line).group(0))
            elif not self.IsComment(line):
                if self.HasComment(line):
                    code.append(line[:self.HasComment(line).span()[0]])
                elif line:
                    code.append(line)
        return code

    def BuildSymbolTable(self, code):
        elements = []
        #first pass: search for label symbols
        j = 0
        for i in range(len(code)):
            if self.IsLabel(code[i]):
                elements.append(code[i])
                SymbolTable.SYMBOL_TABLE[self.IsLabel(code[i]).group(1)] = i - j
                j += 1
        for i in elements:
            code.remove(i)        
        #second pass: search for variables
        for i in code:
            if i[0] == "@" and not self.IsAInstruction(i):
                if not SymbolTable.HasSymbol(i):
                    SymbolTable.VarAlloc(i)
        for i in code:
            if i[0] == "@":
                if SymbolTable.HasSymbol(i):
                    code[code.index(i)] = "@" + str(SymbolTable.SYMBOL_TABLE[i[1:]])

    def IsAInstruction(self, line):
        return re.search(Parser.A_INSTRUCTION, line)

    def IsSymbol(self, line):
        return re.search(Parser.SYMBOLIC_DATA, line)

    def IsComment(self, line):
        return re.search(Parser.COMMENT_LINE, line)
    
    def HasComment(self, line):
        return re.search(Parser.INNER_COMMENT, line)

    def IsLabel(self, line):
        return re.search(Parser.LABEL_SYMBOL, line)

