#coding=utf-8

#OPCODES
OPCODE_R = 0x0
OPCODE_S = 0x1
OPCODE_J = 0xF
OPCODE_JAL = 0xD
OPCODE_BZ_X = 0x8
OPCODE_BZ_T = 0x9
OPCODE_BZ_N = 0xA
OPCODE_JR = 0xC
OPCODE_SW = 0x2
OPCODE_LW = 0x3
OPCODE_LIU = 0x4
OPCODE_LIL = 0x5
OPCODE_M1 = 0xE
OPCODE_BHLEQ = 0x6
#INT still doesnt conform with the instruction set but we must support it here
OPCODE_INT = 0xB

#ARITHMETIC FUNCTIONS
FUNC_AND = 0x0
FUNC_ADD = 0x2
FUNC_SUB = 0x6
FUNC_AND = 0x2
FUNC_OR  = 0x1
FUNC_XOR = 0xF
FUNC_NOR = 0xC
FUNC_MUL = 0x3
FUNC_SLT = 0x7
FUNC_SGT = 0x8
#DIV doesnt conform with the instruction set either
FUNC_DIV = 0xA

#immediates dont make too much sense when the space is rather limited i.e. 4 bits -> signed yields -2 to 1
#FUNC_ADDI = 0x9
#FUNC_SUBI = 0xA
#FUNC_ANDI = 0xB
#FUNC_ORI  = 0xC
#FUNC_XORI = 0xD

#SHIFT FUNCTIONS: room for much more
FUNC_SHR = 0x1
FUNC_SHL = 0x2
FUNC_ROR = 0x4
FUNC_ROL = 0x8
FUNC_SAR = 0x0 #these arent so used

#M1 INSTRUCTION FUNCTIONS
FUNC_LHL = 0x0
FUNC_LHH = 0x1
FUNC_LLL = 0x2
FUNC_LLH = 0x3
FUNC_AIS = 0x4
FUNC_AIH = 0x5
FUNC_AIL = 0x6
FUNC_MFHI = 0x7
FUNC_MFLO = 0x8
FUNC_MTHI = 0x9
FUNC_MTLO = 0xA
