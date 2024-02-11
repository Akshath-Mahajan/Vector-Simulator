import os
import argparse

class IMEM(object):
    def __init__(self, iodir):
        self.size = pow(2, 16) # Can hold a maximum of 2^16 instructions.
        self.filepath = os.path.abspath(os.path.join(iodir, "Code.asm"))
        self.instructions = []

        try:
            with open(self.filepath, 'r') as insf:
                self.instructions = [ins.strip() for ins in insf.readlines()]
            print("IMEM - Instructions loaded from file:", self.filepath)
            # print("IMEM - Instructions:", self.instructions)
        except:
            print("IMEM - ERROR: Couldn't open file in path:", self.filepath)

    def Read(self, idx): # Use this to read from IMEM.
        if idx < self.size:
            return self.instructions[idx]
        else:
            print("IMEM - ERROR: Invalid memory access at index: ", idx, " with memory size: ", self.size)

class DMEM(object):
    # Word addressible - each address contains 32 bits.
    def __init__(self, name, iodir, addressLen):
        self.name = name
        self.size = pow(2, addressLen)
        self.min_value  = -pow(2, 31)
        self.max_value  = pow(2, 31) - 1
        self.ipfilepath = os.path.abspath(os.path.join(iodir, name + ".txt"))
        self.opfilepath = os.path.abspath(os.path.join(iodir, name + "OP.txt"))
        self.data = []

        try:
            with open(self.ipfilepath, 'r') as ipf:
                self.data = [int(line.strip()) for line in ipf.readlines()]
            print(self.name, "- Data loaded from file:", self.ipfilepath)
            # print(self.name, "- Data:", self.data)
            self.data.extend([0x0 for i in range(self.size - len(self.data))])
        except:
            print(self.name, "- ERROR: Couldn't open input file in path:", self.ipfilepath)

    def Read(self, idx): # Use this to read from DMEM.
        if idx < self.size:
            return self.data[idx]
        return False    # In case we need to check "Read" results

    def Write(self, idx, val): # Use this to write into DMEM.
        if idx < self.size:
            self.data[idx] = val
            return True
        return False

    def dump(self):
        try:
            with open(self.opfilepath, 'w') as opf:
                lines = [str(data) + '\n' for data in self.data]
                opf.writelines(lines)
            print(self.name, "- Dumped data into output file in path:", self.opfilepath)
        except:
            print(self.name, "- ERROR: Couldn't open output file in path:", self.opfilepath)

class RegisterFile(object):
    def __init__(self, name, count, length = 1, size = 32):
        self.name       = name
        self.reg_count  = count
        self.vec_length = length # Number of 32 bit words in a register.
        self.reg_bits   = size
        self.min_value  = -pow(2, self.reg_bits-1)
        self.max_value  = pow(2, self.reg_bits-1) - 1
        self.registers  = [[0x0 for e in range(self.vec_length)] for r in range(self.reg_count)] # list of lists of integers

    def Read(self, idx):
        if idx < self.reg_count:
            return self.registers[idx]
        return False
    # Read returns entire register
    # Write takes  entire register
    def Write(self, idx, val):
        if idx < self.reg_count:
            self.registers[idx] = val
            return True
        return False

    def dump(self, iodir):
        opfilepath = os.path.abspath(os.path.join(iodir, self.name + ".txt"))
        try:
            with open(opfilepath, 'w') as opf:
                row_format = "{:<13}"*self.vec_length
                lines = [row_format.format(*[str(i) for i in range(self.vec_length)]) + "\n", '-'*(self.vec_length*13) + "\n"]
                lines += [row_format.format(*[str(val) for val in data]) + "\n" for data in self.registers]
                opf.writelines(lines)
            print(self.name, "- Dumped data into output file in path:", opfilepath)
        except:
            print(self.name, "- ERROR: Couldn't open output file in path:", opfilepath)

class Core():
    def __init__(self, imem: IMEM, sdmem: DMEM, vdmem: DMEM):
        self.IMEM = imem
        self.SDMEM = sdmem
        self.VDMEM = vdmem

        self.RFs = {"SRF": RegisterFile("SRF", 8),
                    "VRF": RegisterFile("VRF", 8, 64)}
        
        # Your code here.
        
    def run(self):
        # Initialization
        instr_idx = 0 
        # Execution
        while(True):
            instr_idx += 1
            instr = self.fetch(instr_idx)
            
            instr = self.decode(instr)

            instr = self.execute(instr)

    def fetch(self, idx):
        '''
        Fetch instr at idx
        '''
        return self.IMEM.Read(idx)
    
    def decode(self, instr):
        '''
        Take instr in string format
        Return as: [instr, ...operands]
        '''
        return instr.split(" ")
    
    def execute(self, instr):
        '''
        Take instr in [instr, ...operands] format
        Return ALU Result
        '''
        # Vector Operations
        if instr[0] == "ADDVV":
            pass
        if instr[0] == "ADDVS":
            pass
        if instr[0] == "SUBVV":
            pass
        if instr[0] == "SUBVS":
            pass
        if instr[0] == "MULVV":
            pass
        if instr[0] == "MULVS":
            pass
        if instr[0] == "DIVVV":
            pass
        if instr[0] == "DIVVS":
            pass
        
        # Vector Mask Register Operations
        # Change __ to EQ NE GT LT GE LE
        if instr[0] == "S__VV":
            pass
        if instr[0] == "S__VS":
            pass
        if instr[0] == "CVM":
            pass
        if instr[0] == "POP":
            pass

        # Vector Length Register Operations
        if instr[0] == "MTCL":
            pass
        if instr[0] == "MFCL":
            pass

        # Memory Access Operations
        if instr[0] == "LV":
            pass
        if instr[0] == "SV":
            pass
        if instr[0] == "LVWS":
            pass
        if instr[0] == "SVWS":
            pass
        if instr[0] == "LVI":
            pass
        if instr[0] == "SVI":
            pass
        if instr[0] == "LS":
            pass
        if instr[0] == "SS":
            pass

        # Scalar Operations
        if instr[0] == "ADD":
            pass
        if instr[0] == "SUB":
            pass
        if instr[0] == "AND":
            pass
        if instr[0] == "OR":
            pass
        if instr[0] == "XOR":
            pass
        if instr[0] == "SLL":
            pass
        if instr[0] == "SRL":
            pass
        if instr[0] == "SRA":
            pass

        # Control operations
        if instr[0] == "B__":
            pass

        # Register-Register Shuffle
        if instr[0] == "UNPACKLO":
            pass
        if instr[0] == "UNPACKHI":
            pass
        if instr[0] == "PACKLO":
            pass
        if instr[0] == "PACKHI":
            pass

        # HALT

        

    def dumpregs(self, iodir):
        for rf in self.RFs.values():
            rf.dump(iodir)

def execute(instr):
    if instr[0] == "":
        pass



if __name__ == "__main__":
    #parse arguments for input file location
    parser = argparse.ArgumentParser(description='Vector Core Performance Model')
    parser.add_argument('--iodir', default="", type=str, help='Path to the folder containing the input files - instructions and data.')
    args = parser.parse_args()

    iodir = os.path.abspath(args.iodir)
    print("IO Directory:", iodir)

    # Parse IMEM
    imem = IMEM(iodir)  
    # Parse SMEM
    sdmem = DMEM("SDMEM", iodir, 13) # 32 KB is 2^15 bytes = 2^13 K 32-bit words.
    # Parse VMEM
    vdmem = DMEM("VDMEM", iodir, 17) # 512 KB is 2^19 bytes = 2^17 K 32-bit words. 

    # Create Vector Core
    vcore = Core(imem, sdmem, vdmem)

    # Run Core
    vcore.run()   
    vcore.dumpregs(iodir)

    sdmem.dump()
    vdmem.dump()

    # THE END