#coding=utf-8

from ucode_basic import UCODEInstruction

class UCODEInstrMem:
    
    memory = [] #array of instructions

    def __init__(self,size):
        #initialize memory with instructions that are NOPs
        for i in range(0,size):
            self.memory.append(UCODEInstruction())

        self.size = size

    def load_from_file(self,filename):
        pass

    def fetch_instruction(self,index):

        if index < self.size and index > 0:
            return self.memory[index]
        else:
            raise ValueError("Invalid PC")
    
