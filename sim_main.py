#coding=utf-8

from ucode_sim import UCODESim


if __name__ == "__main__":
    
    sim = UCODESim(256)

    sim.reset()

    while(1):
        sim.cycle()
