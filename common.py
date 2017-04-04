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
    try:
        num = int(num)
        if num < len(reg):
            return
        for i in range(0, num):
            reg.append('null')
    except Exception as e:
        print(e)
    return reg


def unsigned(num):
    unsigned_num = num & 0xffffffff
    return unsigned_num


def rmv(num):
    num = num.replace("0b", "")
    return num


def add_to_reg(nt, rt, reg):
    reg[int(nt)] = rt
    return reg


class HandlerI:
    try:
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

        def addiu(self, nt, ns, imm16, reg):
            imm16_n = rmv(self.ext(imm16))
            rd = int(reg[int(ns)]) + int(imm16_n)
            add_to_reg(nt, rd, reg)

        def sw(self, nt, ns, imm16, reg, mem):
            nt = int(nt)
            ns = int(ns)
            imm16_n = int(rmv(self.ext(imm16)), 2)
            reg[ns] = int(str(reg[ns]), 2)
            mem_key = int(int(reg[ns]) + imm16_n)
            mem_val = int(reg[nt])
            mem[mem_key] = mem_val
            return mem_val
    except Exception as e:
        print(e)
        print("***???***")


class HandlerR:
    try:
        def get_nd(self, opt):
            nd = int(opt[1].replace("$", "").zfill(5))
            return nd

        def get_ns(self, opt):
            ns = int(opt[2].replace("$", "").zfill(5))
            return ns

        def get_nt(self, opt):
            nt = int(opt[3].replace("$", "").zfill(5))
            return nt

        def get_shamt(self, opt):
            shamt = int(opt[3].zfill(5))
            return shamt

        def add(self, nd, ns, nt, reg):
            rd = int(reg[ns]) + int(reg[nt])
            add_to_reg(nd, rd, reg)
            # return rd

        def sub(self, nd, ns, nt, reg):
            rd = int(reg[ns]) - int(reg[nt])
            add_to_reg(nd, rd, reg)

        # return rd

        def subu(self, nd, ns, nt, reg):
            rd = unsigned(int(reg[ns])) - unsigned(int(reg[nt]))
            add_to_reg(nd, rd, reg)
            # return rd

        def slt(self, nd, ns, nt, reg):
            tmp = int(reg[ns]) - int(reg[nt])
            if tmp < 0:
                rd = 1
            else:
                rd = 0
            add_to_reg(nd, rd, reg)
            return rd

        def sltu(self, nd, ns, nt, reg):
            tmp = unsigned(int(reg[ns])) - unsigned(int(reg[nt]))
            if tmp < 0:
                rd = 1
            else:
                rd = 0
            add_to_reg(nd, rd, reg)
            return rd

    except Exception as e:
        print(e)
        print("***???***")
