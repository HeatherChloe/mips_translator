# -*- coding: utf-8 -*-
# may rewrite with C
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QRegExp

import cons

result_mem = ""
result_reg = ""


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
                result_str = result_str.split('\n')[0]
        if '#' in result_str:
            result = ''.join(result_str.split('#')[0])
        else:
            result = result_str
        # if '\n' in result:
    except Exception as e:
        print("########genlines Exception############")
        print(e)
        print("########genlines Exception############")
    return result


# def init_nd(reg, num):
#     try:
#         num = int(num)
#         if num < len(reg):
#             return
#         for i in range(0, num):
#             reg.append('null')
#     except Exception as e:
#         print(e)
#     return reg
def myBin(stri):
    count = 0
    rst = 0
    for each in stri[::-1]:
        rst += int(each) * 2**count
        count += 1
    return rst

def unsigned(num):
    unsigned_num = num & 0xffffffff
    return unsigned_num


def rmv(num):
    num = num.replace("0b", "")
    return num


def add_to_reg(nt, rt, reg):
    reg[int(nt)] = rt
    return reg


def reg_show(nt, reg, debug_flag=None):
    str_reg = ""
    count = 0
    for each in reg:
        str_reg += str(count) + ': ' + str(each)
        str_reg += '\n'
        count += 1
    global result_reg
    result_reg = str_reg
    if debug_flag:
        pass


def mem_show(mem, debug_flag):
    try:
        str_mem = ""
        if mem:
            for k, v in mem.items():
                str_mem += str(k) + ': ' + str(v)
                str_mem += '\n'
        global result_mem
        result_mem = str_mem
        if debug_flag is True:
            pass
    except Exception as e:
        print(e)


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
            try:
                imm16 = int(imm16, 16)
                imm16 = bin(imm16).replace('b', '')
            except Exception as e:
                print("ext err %s" % e)
            return imm16

        def ext_16_str(self, stri):
            ext_16 = stri.zfill(16)
            return ext_16

        def ori(self, elses, reg):
            try:
                op = '001101'
                nt = self.get_nt(elses)
                ns = self.get_ns(elses)
                imm16 = self.getimm(elses)
                imm16_n = self.ext(imm16)
                a = rmv(imm16_n)
                rs = reg[int(ns)]
                rd = "%05d" % (int(rs) | int(a))
                add_to_reg(nt, rd, reg)
                ext = self.ext_16_str(self.ext(imm16))
                nt = rmv(bin(int(nt))).zfill(5)
                ns = rmv(bin(int(ns))).zfill(5)
                reg_show(nt, reg, debug_flag=False)
                cons.changed_reg = myBin(nt)

            except Exception as e:
                print(e)
            return str("#32'b" + op + "_" + ns + "_" + nt + "_" + '_'.join(ext[i:i + 4] for i in range(0, len(ext), 4)))

        def addiu(self, elses, reg):
            op = '001001'
            ns = self.get_ns(elses)
            nt = self.get_nt(elses)
            imm16 = self.getimm(elses)
            imm16_n = rmv(self.ext(imm16))
            rd = int(reg[int(ns)]) + int(imm16_n)
            add_to_reg(nt, rd, reg)
            ext = self.ext_16_str(self.ext(imm16))
            nt = rmv(bin(int(nt)))
            ns = rmv(bin(int(ns)))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(
                ext[i:i + 4] for i in range(0, len(ext), 4)))

        def sw(self, elses, reg, mem):
            try:
                op = '101011'
                ns = self.get_ns(elses)
                nt = self.get_nt(elses)
                imm16 = self.getimm(elses)
                nt = int(nt)
                ns = int(ns)
                imm16_n = int(rmv(self.ext(imm16)), 2)
                try:
                    reg[ns] = int(str(reg[ns]), 2)
                except Exception:
                    reg[ns] = int(str(reg[ns]))
                mem_key = int(int(reg[ns]) + imm16_n)
                mem_val = int(reg[nt])
                mem[mem_key] = mem_val

                ext = self.ext_16_str(self.ext(imm16))
                nt = rmv(bin(int(nt)))
                ns = rmv(bin(int(ns)))
                mem_show(mem, debug_flag=False)
                cons.changed_mem = mem_key
            except Exception as e:
                print("sw debug")
                print(e)
            return str("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(
                ext[i:i + 4] for i in range(0, len(ext), 4)))

        def lw(self, elses, reg, mem):
            try:
                op = '100011'
                ns = self.get_ns(elses)
                nt = self.get_nt(elses)
                imm16 = self.getimm(elses)
                nt = int(nt)
                ns = int(ns)
                imm16_n = int(rmv(self.ext(imm16)), 2)

                rt = mem[int(reg[ns]) + imm16_n]
                add_to_reg(nt, rt, reg)
                ext = self.ext_16_str(self.ext(imm16))
                nt = rmv(bin(int(nt)))
                ns = rmv(bin(int(ns)))
                # mem_show(mem, debug_flag=False)
                reg_show(nt, reg)
                cons.changed_reg = myBin(nt)
            except Exception as e:
                print('lw')
                print(e)
            return str("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(
                ext[i:i + 4] for i in range(0, len(ext), 4)))

        def beq(self, idx, elses):
            try:
                op = '000100'
                ns = self.get_ns(elses)
                nt = self.get_nt(elses)
                nt = rmv(bin(int(nt))).zfill(5)
                ns = rmv(bin(int(ns))).zfill(5)
                imm16 = int(rmv(self.ext(str(idx))), 2)
                ext = self.ext_16_str(str(self.ext(str(imm16))))
            except Exception as e:
                print(e)
                print("beq error")
            return str("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(
                ext[i:i + 4] for i in range(0, len(ext), 4)))
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

        def add(self, elses, reg):
            op = '000000'
            func = '100000'
            shamt = '00000'
            ns = self.get_ns(elses)
            nt = self.get_nt(elses)
            nd = self.get_nd(elses)
            rd = int(reg[ns]) + int(reg[nt])
            add_to_reg(nd, rd, reg)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)

        def sub(self, elses, reg):
            op = '000000'
            shamt = '00000'
            func = '100010'
            ns = self.get_ns(elses)
            nt = self.get_nt(elses)
            nd = self.get_nd(elses)
            rd = int(reg[ns]) - int(reg[nt])
            add_to_reg(nd, rd, reg)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)

        def subu(self, elses, reg):
            op = '000000'
            shamt = '00000'
            func = '100011'
            ns = self.get_ns(elses)
            nt = self.get_nt(elses)
            nd = self.get_nd(elses)
            rd = unsigned(int(reg[ns])) - unsigned(int(reg[nt]))
            add_to_reg(nd, rd, reg)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)

        def slt(self, elses, reg):
            op = '000000'
            shamt = '00000'
            func = '101010'
            ns = self.get_ns(elses)
            nt = self.get_nt(elses)
            nd = self.get_nd(elses)
            tmp = int(reg[ns]) - int(reg[nt])
            rd = 1 if tmp < 0 else 0
            add_to_reg(nd, rd, reg)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)

        def sltu(self, elses, reg):
            op = '000000'
            shamt = '00000'
            func = "101011"
            ns = self.get_ns(elses)
            nt = self.get_nt(elses)
            nd = self.get_nd(elses)
            tmp = unsigned(int(reg[ns])) - unsigned(int(reg[nt]))
            rd = 1 if tmp < 0 else 0
            add_to_reg(nd, rd, reg)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)

        def srl(self, elses, reg):
            op = '000000'
            rs = '00111'
            func = '100001'
            nd = self.get_nd(elses)
            nt = self.get_ns(elses)
            shamt = self.get_shamt(elses)
            shamt = int(shamt)
            reg[nt] = int(reg[nt])
            rd = rmv(bin(reg[nt] >> shamt)).zfill(32)
            add_to_reg(nd, rd, reg)
            nd = rmv(bin(int(nd)))
            nt = rmv(bin(int(nt)))
            shamt = rmv(bin(shamt).zfill(5))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + rs + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5) + '_' + str(
                shamt).zfill(5) + '_' + func)

        def sll(self,elses, reg):
            op = '000000'
            rs = '00111'
            func = '110000'
            nd = self.get_nd(elses)
            nt = self.get_ns(elses)
            shamt = self.get_shamt(elses)
            shamt = int(shamt)
            reg[nt] = int(reg[nt])
            rd = rmv(bin(reg[nt] << shamt)).zfill(32)
            if len(rd) != 32:
                rd = rd[:32].zfill(32)
            add_to_reg(nd, rd, reg)
            nd = rmv(bin(int(nd)))
            nt = rmv(bin(int(nt)))
            shamt = rmv(bin(shamt).zfill(5))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + rs + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5) + '_' + str(
                shamt).zfill(5) + '_' + func)

        def sra(self, elses, reg):
            op = '000000'
            rs = '00111'
            func = '101100'
            nd = self.get_nd(elses)
            nt = self.get_ns(elses)
            shamt = self.get_shamt(elses)
            shamt = int(shamt)
            nt = int(nt)
            if len(reg[nt]) == 32:
                rd = reg[nt][:-shamt].zfill(32)
            else:
                reg[nt] = int(rmv(reg[nt]))
                rd = bin(reg[nt] >> shamt)
                rd = rmv(rd).rjust(32, [1]) if bin(reg[nt])[0] == 1 else rmv(rd.zfill(32))
            add_to_reg(nd, rd, reg)
            nd = rmv(bin(int(nd)))
            nt = rmv(bin(int(nt)))
            shamt = rmv(bin(shamt).zfill(5))
            reg_show(nt, reg, debug_flag=False)
            cons.changed_reg = myBin(nt)
            return str("#32'b" + op + '_' + rs + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5) + '_' + str(
                shamt).zfill(5) + '_' + func)
    except Exception as e:
        print(e)
        print("***???***")


class HandlerJ:
    try:
        def getimm(self, imm16):
            imm16 = imm16.replace("0x", "")
            return imm16

        def ext(self, imm16):
            imm16 = int(imm16, 16)
            imm16 = bin(imm16).replace('b', '')
            return imm16

        def ext_16_str(self, stri):
            ext_16 = stri.zfill(16)
            return ext_16

        def j(self, elses):
            pass
    except Exception as e:
        print(e)
        print("***???***")