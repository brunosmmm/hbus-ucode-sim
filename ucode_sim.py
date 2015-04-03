#coding=utf-8

from ucode_basic import UCODERegBank, UCODEInstructionOpcode

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

    #status
    status = UCODESimStatus.init

def __init__(self):
    self.reg_bank = UCODERegBank()

def cycle(self):
    """A single cycle"""
    
    #if paused, nothing to do
    if self.status = UCODESimStatus.paused:
        return

    #fetch stage
    #self.next_instr =
    
    #decode
    if self.next_instr.opcode == UCODEInstructionOpcode.OPCODE_R:
        #arithmetic operations

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

    #set PC to 0
    self.pc = 0

    #set next instruction to first instruction


    #set running
    self.status = UCODESimStatus.running
    
