# -*- coding: utf-8 -*-
# may rewrite with C


def gen_lines(line):
    try:
        line = line.lstrip()
        count_space = 0
        result_str = ""
        line.replace('\t', '')
        for each in line:
            if each == ' ':
                if count_space == 0:
                    result_str += each
                    count_space = 1
            else:
                result_str += each

        for each in result_str:
            if each == '#':
                result = ''.join(result_str.split(each)[0])
    except Exception as e:
        print("########genlines Exception############")
        print(e)
        print("########genlines Exception############")
    return result


def init_nd(reg, num):
    num = int(num)
    if num < len(reg):
        return
    for i in range(0,num):
        reg.append('null')
        return reg


def rmv(num):
    num = num.replace("0b", "")
    return num


def add_to_reg(nt, rt, reg):
    nt = int(nt)
    if nt in range(len(reg)):
        reg[nt] = rt
    elif nt == len(reg):
        reg.append(rt)
    else :
        indx = nt
        indx = int(indx)
        while(reg.index(reg[-1]) != indx):
            reg.append('null')
            indx -= 1
            if reg.index(reg[-1]) == nt - 1:
                break
            reg.append(rt)
    return reg


class HandlerI:
    try:
        # def __init__(self, op, rs, rt, imm16):
        #     self.op = op
        #     self.rs = rs
        #     self.rt = rt
        #     self.imm16 = imm16

        def get_nt(self, opt):
            nt = opt[1].replace("$", "").zfill(5)
            return nt

        def get_ns(self, opt):
            ns = opt[2].replace("$", "").zfill(5)
            return ns

        def getimm(self, opt):
            imm16 = opt[3].replace("0x", "")
            return imm16

        def ext(self, imm16):
            imm16 = int(imm16, 16)
            imm16 = bin(imm16).replace('b', '')
            return imm16

        def ext_16_str(self, stri):
            ext_16 = stri.zfill(16)
            return ext_16

        def ori(self, nt, ns, imm16, reg):
            imm16_n = self.ext(imm16)
            a = rmv(imm16_n)
            rs = reg[int(ns)]
            rd = "%05d" % (int(rs) | int(a))
            add_to_reg(nt, rd, reg)
    except Exception as e:
        print(e)
        print("***???***")