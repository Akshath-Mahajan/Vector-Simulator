# Vector-Simulator

This is a functional simulator for the presented vector ISA following the prescribed specifications. The machine is reminiscent of VMIPS but we will not consider off-chip data movement for simplicity.

The simulator is implemented in Python 3, without using any external libraries. To limit engineering effort, we are directly processing assembly instructions, and hence there is no need to consider actual instruction encodings and machine code.

## Input

The simulator takes the following files as inputs:
- `Code.asm`: The file contains the assembly code for the test function.
- `SDMEM.txt`: The file contains the initial state of the SDMEM containing the data required for the
test function in integer format. Each line in this file represents one word (32 bit) of data in the SDMEM.
- `VDMEM.txt`: The file contains the initial state of the VDMEM containing the data required for the
test function in integer format. Each line in this file represents one word (32 bit) of data in the VDMEM.

## Output
The simulator outputs these files:
- `VRF.txt`: The file shows the final state of the Vector Register File after the execution of all the
instructions in the input `Code.asm` file. Each line contains a comma separated list of integer values showing all the elements of a vector register.
- `SRF.txt`: The file shows the final state of the Scalar Register File after the execution of all the instructions in the input `Code.asm` file. Each line contains an integer value showing a scalar register data.
- `SDMEMOP.txt`: The file contains the final state of the SDMEM after the execution of the `Code.asm` file.
- `VDMEMOP.txt`: The file contains the final state of the VDMEM after the execution of the `Code.asm` file.

## ISA Specification

Vector length of 64, 32b integer elements.

The architectural state of the vector processor has the following components: 
- VDMEM: Vector Data Memory with a capacity of 512 KB, word addressable. 
- SDMEM: Scalar Data Memory with a capacity of 32 KB, word addressable. 

Register Files:

- Scalar Register File: 8 Scalar Registers of 32 bits each.
- Vector Register File: 8 Vector Registers each with a maximum capacity of 2048 bits or 256 bytes or 64
32-bit elements. Maximum Vector Length is set to 64.
- Vector Mask Register: 1 Vector Mask Register also known as the Flag Register. Contains 64 1 bit values.
The vector operations are valid only for the elements with corresponding flag register value set. Clear this
register if all the elements are valid.
- Vector Length Register: 1 Vector Length Register of size 32 bits to contain the number of vector element
operations. Set this to MVL if all the elements of the vector register inputs are to be evaluated.