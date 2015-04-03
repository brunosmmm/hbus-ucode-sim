#coding=utf-8

from ucode_defs import *


class UCODEArithFunc:
    
    function = None
    opcode = 0

    def __init__(self,opcode,function):
        self.function = function
        self.opcode = opcode

    def calculate(self,**kwargs):
        return self.function(**kwargs)

UCODE_ARITHMETIC_FUNCTIONS = {FUNC_ADD : UCODEArithFunc(FUNC_ADD, lambda x, y: x+y),
                              FUNC_SUB : UCODEArithFunc(FUNC_SUB, lambda x, y: x-y),
                              FUNC_AND : UCODEArithFunc(FUNC_AND, lambda x, y: x&y),
                              FUNC_OR  : UCODEArithFunc(FUNC_OR, lambda x, y: x|y),
                              FUNC_XOR : UCODEArithFunc(FUNC_XOR, lambda x, y: x^y),
                              FUNC_NOT : UCODEArithFunc(FUNC_NOT, lambda x: ~x),
                              FUNC_MUL : UCODEArithFunc(FUNC_MUL, lambda x, y: x*y),
                              FUNC_SLT : UCODEArithFunc(FUNC_SLT, lambda x, y: x<y),
                              FUNC_DIV : UCODEArithFunc(FUNC_DIV, lambda x, y: [x/y, x%y]),
                              FUNC_ADDI: UCODEArithFunc(FUNC_ADDI, lambda x, y: x+y),
                              FUNC_SUBI: UCODEArithFunc(FUNC_SUBI, lambda x, y: x-y),
                              FUNC_ANDI: UCODEArithFunc(FUNC_ANDI, lambda x, y: x&y),
                              FUNC_ORI : UCODEArithFunc(FUNC_ORI, lambda x, y: x|y),
                              FUNC_XORI: UCODEArithFunc(FUNC_XORI, lambda x, y: x^y)
                              }

UCODE_SHIFT_FUNCTIONS = {FUNC_SHR : UCODEArithFunc(FUNC_SHR, lambda x, y: x>>y),
                         FUNC_SHL : UCODEArithFunc(FUNC_SHL, lambda x, y: x<<y),
                         FUNC_ROR : UCODEArithFunc(FUNC_ROR, lambda x, y: x<<(8-y) | x>>y),
                         FUNC_ROL : UCODEArithFunc(FUNC_ROL, lambda x, y: x>>(8-y) | x<<y)
                         }


class UCODEInstruction:
    """Instruction descriptor class"""
    
    opcode = None
    reg_a = 0
    reg_b = 0
    shamt = 0
    addr = 0
    func = 0

class UCODERegBank:
    
    registers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def __init__(self):
        pass

    def write_reg(self,reg_num,reg_val):
        
        if reg_num > 15 or reg_num < 0:
            raise IOError("Invalid register number")
        
        if reg_num == 0:
            return #prevents writing into register #0

        self.registers[reg_num] = reg_val

    def read_reg(self,reg_num):
        
        if reg_num > 15 or reg_num < 0:
            raise IOError("Invalid register number")
            
        return self.registers[reg_num]

    def clear_regs(self):
        
        for i in range(0,len(self.registers)):
            self.registers[i] = 0
            
