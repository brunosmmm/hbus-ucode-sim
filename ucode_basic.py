#coding=utf-8

class UCODEInstructionOpcode:
    OPCODE_R = 0
    OPCODE_S = 0
    OPCODE_J = 0
    OPCODE_W = 0
    OPCODE_L = 0

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
            
