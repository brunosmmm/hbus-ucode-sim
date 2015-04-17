#coding=utf-8

from ucode_basic import UCODERegBank, UCODE_ARITHMETIC_FUNCTIONS, UCODE_SHIFT_FUNCTIONS
from ucode_defs import *
from ucode_mem import UCODEInstrMem

class UCODESimStatus:
    init = 0
    running = 1
    paused = 2


class UCODESim:
    """Main simulator class"""

    pc = 0
    next_instr = None

    #special registers
    reg_hi = 0
    reg_lo = 0
    reg_ret = 0

    #status
    status = UCODESimStatus.init

    def __init__(self, imem_size):
        self.reg_bank = UCODERegBank()
        self.imem = UCODEInstrMem(imem_size)

    def cycle(self):
        """A single cycle"""
    
        #if paused, nothing to do
        if self.status == UCODESimStatus.paused:
            return

        #fetch stage
        self.next_instr = self.imem.fetch_instruction(self.pc)
    
        #decode & execute
        jump = False

        if self.next_instr.opcode == OPCODE_R:
            #arithmetic operations - results goes directly into reg_a except for mul
            reg_a_val = self.reg_bank.read_reg(self.next_instr.reg_a)
            reg_b_val = self.reg_bank.read_reg(self.next_instr.reg_b)

            result = UCODE_ARITHMETIC_FUNCTIONS[self.next_instr.func].calculate(reg_a_val,reg_b_val)

            #write
            if self.next_instr.func == FUNC_MUL:
                self.reg_hi = result >> 8
                self.reg_lo = result & 0xFF
            elif self.next_instr.func == FUNC_DIV:
                self.reg_hi = result[0]
                self.reg_lo = result[1]
            else:
                self.reg_bank.write_reg(self.next_instr.reg_a, result)

        elif self.next_instr.opcode == OPCODE_S:
            #shift operations
            reg_a_val = self.reg_bank.read_reg(self.next_instr.reg_a)
            shamt_val = self.next_instr.shamt

            result = UCODE_SHIFT_FUNCTIONS[self.next_instr.func].calculate(reg_a_val, shamt_val)

            #write
            self.reg_bank.write_reg(self.next_instr.reg_a, result)
        
        elif self.next_instr.opcode in (OPCODE_JAL, OPCODE_J):
            jump = True

            if self.next_instr.opcode == OPCODE_JAL:
                #save current PC

                #old ucode:
                #self.reg_bank.write_reg(14,(self.pc & 0xFF00)>>8)
                #self.reg_bank.write_reg(15,self.pc & 0xFF)
            
                #new ucode:
                self.reg_ret = self.pc

            #jump to destination addr
            self.pc = self.next_instr.addr
        
        elif self.next_instr.opcode == OPCODE_JR:
            jump = True
            
            #potentially problematic - C implementation: registers are 8 bits wide so can only jump
            #to instruction in range 0 - 255
            #new ucode: this is relative to current pc
            reg_a_val = self.reg_bank.read_reg(self.next_instr.reg_a)
    
            self.pc = self.pc + reg_a_val + self.next_instr.offset

        elif self.next_instr.opcode == OPCODE_BEQ:
            reg_a_val = self.reg_bank.read_reg(self.next_instr.reg_a)
            reg_b_val = self.reg_bank.read_reg(self.next_instr.reg_b)

            if reg_a_val == reg_b_val:
                jump = True
                self.pc = self.pc + self.next_instr.offset

        elif self.next_instr.opcode == OPCODE_MFHI:
            self.reg_bank.write_reg(self.next_instr.reg_a, self.reg_hi)
        
        elif self.next_instr.opcode == OPCODE_MFLO:
            self.reg_bank.write_reg(self.next_instr.reg_a, self.reg_lo)

        #extension - copy from return val reg. hardwired to reg 14&15
        elif self.next_instr.opcode == OPCODE_MFRET:
            self.reg_bank.write_reg(14, (self.reg_ret & 0xFF00)>>8)
            self.reg_bank.write_reg(15, self.reg_ret & 0xFF)

        elif self.next_instr.opcode == OPCODE_M1:
            
            if self.next_instr.func == FUNC_LHL:
                self.reg_lo = self.reg_bank.read_reg(self.next_instr.reg_a)
                self.reg_hi = self.reg_bank.read_reg(self.next_instr.reg_b)

            elif self.next_instr.func == FUNC_LIH:
                self.reg_hi = self.next_instr.imm

            elif self.next_instr.func == FUNC_LIL:
                self.reg_lo = self.next_instr.imm
            
            elif self.next_instr.func == FUNC_AIS:
                self.reg_hi = self.reg_hi + self.next_instr.imm #IMM AS SIGNED INT!!!

        elif self.next_instr.opcode == OPCODE_INT:
            #emit interrupt (dummy)
            pass

        elif self.next_instr.opcode == OPCODE_RET:
            #load saved address and jump
            jump = True
            self.pc = self.reg_ret

        #increment PC
        if jump == False:
            self.pc = self.pc + 1
         

    def pause(self):
        """Pause execution (simulation)"""
        self.status = UCODESimStatus.paused

    def unpause(self):
        """Resume execution (simulation)"""
        self.status = UCODESimStatus.running


    def reset(self):
        """Reset VM"""
    
        #clear register bank
        self.reg_bank.clear_regs()

        #clear special registers
        self.reg_hi = 0
        self.reg_lo = 0
        self.reg_ret = 0

        #set PC to 0
        self.pc = 0

        #set running
        self.status = UCODESimStatus.running
    

