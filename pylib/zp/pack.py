import struct

def p32(data,fmt="<I"):
    return struct.pack(fmt,data)

def u32(data,fmt="<I"):
    return struct.unpack(fmt,data)[0]

def p64(data,fmt="<Q"):
    if type(data) == str:
        return data
    return struct.pack(fmt,data)

def u64(data,fmt="<Q"):
    if type(data) == str:
        return data
    return struct.unpack(fmt,data)[0]


def _flat(args):
    out = []
    for arg in args:
        if type(arg) == list:
            for i in range(len(arg)):
                out.append(arg[i])
        else :
            out.append(arg)
    return out

def flat32(*args, **kwarg):
    return ''.join(map(p32,_flat(args)))

def flat64(*args, **kwarg):
    return ''.join(map(p64,_flat(args)))
