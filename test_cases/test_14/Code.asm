CVM
MFCL SR1
LS SR2 SR0 0
LS SR3 SR0 1
LV VR1 SR0
LV VR2 SR1
MULVV VR3 VR1 VR2
PACKLO VR4 VR3 VR0
PACKHI VR5 VR3 VR0
ADDVV VR3 VR4 VR5
SRA SR1 SR1 SR2
MTCL SR1
BNE SR1 SR2 -5
CVM
SV VR3 SR3
HALT