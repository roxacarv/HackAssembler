SYMBOL_TABLE = {
    'SP': '0',
    'LCL': '1',
    'ARG': '2',
    'THIS': '3',
    'THAT': '4',
    'R0': '0',
    'R1': '1',
    'R2': '2',
    'R3': '3',
    'R4': '4',
    'R5': '5',
    'R6': '6',
    'R7': '7',
    'R8': '8',
    'R9': '9',
    'R10': '10',
    'R11': '11',
    'R12': '12',
    'R13': '13',
    'R14': '14',
    'R15': '15',
    'SCREEN': '16384',
    'KBD': '24576'
}

ADDRESSES = {}

def HasSymbol(symbol):
    return (symbol[1:] in SYMBOL_TABLE.keys())

def VarAlloc(var):
    n = 16
    if not var[1:-1] in ADDRESSES.keys():
        lastAddress = GetFreeAddress()
        if lastAddress == None:
            ADDRESSES[var[1:]] = 16
        else:
            ADDRESSES[var[1:]] = lastAddress + 1
        SYMBOL_TABLE[var[1:]] = str(ADDRESSES[var[1:]])

def GetFreeAddress():
    lastAddress = None
    for i in ADDRESSES.values():
        lastAddress = i
    return lastAddress