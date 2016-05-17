import struct

def p32(data,fmt="<I"):
    return struct.pack(fmt,data)

def u32(data,fmt="<I"):
    return struct.unpack(fmt,data)[0]

def p64(data,fmt="<Q"):
    return struct.pack(fmt,data)

def u64(data,fmt="<Q"):
    return struct.unpack(fmt,data)[0]
