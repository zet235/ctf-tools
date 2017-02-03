import struct

def p32(data,fmt="<I"):
    return struct.pack(fmt,data)

def u32(data,fmt="<I"):
    return struct.unpack(fmt,data)[0]

def p64(data,fmt="<Q"):
    return struct.pack(fmt,data)

def u64(data,fmt="<Q"):
    return struct.unpack(fmt,data)[0]

def flat32(*args, **kwarg):
    out = []
    for arg in args:
        if type(arg) == list:
            for i in range(len(arg)):
                out.append(arg[i])
        else :
            out.append(arg)
    return ''.join(map(p32,out))

def flat64(*args, **kwarg):
    out = []
    for arg in args:
        if type(arg) == list:
            for i in range(len(arg)):
                out.append(arg[i])
        else :
            out.append(arg)
    return ''.join(map(p64,out))
