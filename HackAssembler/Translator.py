import Parser
import re
import Instructions

class Translator(object):

    def __init__(self):
        self.parser = Parser.Parser()
        self.output = None

    def GetOutput(self):
        return self.output

    def WriteToSource(self):
        source = ""
        for i in self.output:
            temp = source
            source = temp + i + '\n'
        sourceFile = open('output.hack', 'w')
        sourceFile.write(source)
        sourceFile.close()

    def Translate(self, code):
        binCode = []
        for _ in code:
            result = ""
            if re.search('=|;', _) != None:
                result = "111"
                if re.search("=", _) and re.search(";", _):
                    step = _.split("=")
                    step = list(step[0]) + step[1].split(';')
                    temp = result
                    tableCode = Instructions.COMP_TABLE[step[1]][1] + Instructions.COMP_TABLE[step[1]][0] + Instructions.DEST_TABLE[step[0]]
                    result = temp + tableCode + Instructions.JUMP_TABLE[step[2]]
                if re.search("=", _):
                    step = _.split("=")
                    temp = result
                    tableCode = Instructions.COMP_TABLE[step[1]][1] + Instructions.COMP_TABLE[step[1]][0] + Instructions.DEST_TABLE[step[0]]
                    result = temp + tableCode + '000'
                if re.search(";", _):
                    step = _.split(";")
                    temp = result
                    tableCode = Instructions.COMP_TABLE[step[0]][1] + Instructions.COMP_TABLE[step[0]][0] + '000' + Instructions.JUMP_TABLE[step[1]]
                    result = temp + tableCode
                binCode.append(result)
            if self.parser.IsAInstruction(_):
                result = "0"
                temp = result
                number = int(_[1:])
                binary = bin(number).replace('0b', '')
                result = temp + binary.zfill(15)
                binCode.append(result)
        self.output = binCode
        return binCode