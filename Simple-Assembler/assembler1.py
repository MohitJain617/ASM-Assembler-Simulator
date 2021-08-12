global instructionDictA
instructionDictA = {'add': '00000', 'sub': '00001', 'mul': '00110', 'xor': '01010', 'or': '01011', 'and':'01100'}

global instructionDictD
instructionDictD = {'ld': '00100', 'st':'00101'}
                        
global regDict
regDict = {'R0':'000', 'R1': '001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}

global var 
var = dict()




# takes in s(string) and size(int) returns binary string of size size
def toBinary(s,size):
    ans = ""
    if(s.isnumeric()):
        s = int(s) 
    else:
        return "Invalid syntax"
    while(s > 0):
        if(s % 2 == 0):
            ans = "0" + ans;
        else:
            ans = "1" + ans;
        s = s//2

    if(len(ans)==size):
        return ans;
    elif(len(ans) < size):
        while(len(ans) != size):
            ans = "0" + ans
        return ans
    else:
        ans = ans[len(ans) - size:]
        return ans
    



def typeAInstruction(x):
    '''Takes in input for type A instruction, tests if it is valid 
    and returns the corresponding binary code for the instruction
    Requires: string input
    Functions used:
        1. isValidTypeA: checks if string is a valid expression 
        of type A
        2. isValidImm: checks if immediate is a valid immediate
        3. isValidReg: checks if register is valid.
    '''
    x = x.split()
    if(isValidTypeA(x)):
        binary = ''
        
        #accounting for the op-code
        if(x[0] in instructionDictA.keys()): binary+=instructionDictA(x[0]);

        if(isValidReg(x[1]) and isValidReg(x[2]) and isValidReg(x[3])):
            binary+= regDict(x[1]) + regDict(x[2]) + regDict(x[3])

        if(len(binary) == 16): return binary
        else: raise SyntaxError("Typos in instruction or register name")


        
        
    else: raise SyntaxError("General Syntax Error")



def isValidType(operationArr):
    '''takes in array argument and determines if it is a valid type A 
    syntax'''

    if(len(operationArr) != 4): return False
    if(operationArr[0] not in instructionDictA): return False
    for i in range(1, 4):
        if(!isValidReg(operationArr[1])): return False
    return True


def isValidReg(reg):
    '''except flag'''
    regDictA = {'R0':'000', 'R1': '001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110'}
    return (reg in regDictA.keys())



#is valid variable instruction, returns boolean if the instructions is a valid var function 
def validVarInstruction(ins):
    ins = ins.split()
    if(len(ins) != 2) return false
    if(ins[0] != 'var') return false 
    if(ins[1] in regDict.keys()) return false
    if(ins[1] in instructionDictA.keys()) return false 
    ''' add more dict check here once they are declared above '''
    #check if it is alphanum or has underscores:
    for ch in ins[1]:
        if(ch.isalnum() or (ch == '_')) continue
        else return false
    global var
    ''' add mechanism to give value to var as well (depending on program size) '''
    var[ins[1]] = 1
    return true

def isValidVar(ins):
    global var
    return (ins in var.keys())

def isValidTypeD(ins):
    #takes in string and finds out if type matches or no
    x = ins.split()
    if len(x) != 3:
        return False
    return (ins[0] in instructionDictD.keys())

def typeDInstruction(ins):
    '''assumes ins is of type D, 
    Takes in string argument and returns its corresponding binary string
    returns error if the registers or memory address are invalid

    types of error:
    use of undefined variable address 
    misuse of labels as variables
    Illegal use of flag register '''
    ins = ins.split()
    binary = instructionDictD[ins[0]]
    if (ins[1] == "FLAG"):
        #error invalid register
        return "Illegal use of flag register"
    elif(isValidReg(ins[1]) == False):
        return "Typo in register name"
    else:
        binary = binary + regDict[ins[1]]
    
    if(ins[2] in label.keys()):
        return "Misuse of labels as variables"
    elif(isValidVar(ins[2]) == False):
        return "Use of undefined Variable address"
    else:
        binary = binary + var[ins[2]]

    return binary





def typeFInstruction(ins, numberHalts = True):
    '''Takes in string argument and returns its corresponding binary.
    Optional: can also raise an error depending on the boolean value numberHalts
    
    Operands:
        1. String ins for the instruction
        2. boolean numberHalts which checks if the number of halts are not >1, default value is true'''
    if(not numberHalts):
        raise SyntaxError("hlt not being used as the last instruction.")
    if(ins.strip() == 'hlt'):
        return "10011"+11*'0'