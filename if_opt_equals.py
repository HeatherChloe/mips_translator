from inspect import trace

from common import *
line_jump = 0


def if_opt_eqs(opt, reg_list, mem_list, opt_list_with_line_num):
    try:
        action = list(opt.values())[0][0]
        elses = list(opt.values())[0][0:]
        if action == 'ori':
            ori_obj = HandlerI()
            op = '001101'
            ns = ori_obj.get_ns(elses)
            imm16 = ori_obj.getimm(elses)
            nt = ori_obj.get_nt(elses)
            ext = ori_obj.ext_16_str(ori_obj.ext(imm16))
            ori_obj.ori(nt, ns, imm16, reg_list)
            nt = rmv(bin(int(nt))).zfill(5)
            ns = rmv(bin(int(ns))).zfill(5)
            print("#32'b" + op + "_" + ns + "_" + nt + "_" + '_'.join(ext[i:i + 4] for i in range(0, len(ext), 4)))
            print("--------------------------")
        if action == 'addiu':
            addiu_obj = HandlerI()
            op = '000000'
            ns = addiu_obj.get_ns(elses)
            nt = addiu_obj.get_nt(elses)
            imm16 = addiu_obj.getimm(elses)
            addiu_obj.addiu(nt, ns, imm16, reg_list)
            ext = addiu_obj.ext_16_str(addiu_obj.ext(imm16))
            nt = rmv(bin(int(nt)))
            ns = rmv(bin(int(ns)))
            print("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(
                ext[i:i + 4] for i in range(0, len(ext), 4)))
            print("--------------------------")
        if action == 'sw':
            op = '101011'
            sw_obj = HandlerI()
            ns = sw_obj.get_ns(elses)
            nt = sw_obj.get_nt(elses)
            imm16 = sw_obj.getimm(elses)
            sw_obj.sw(nt, ns, imm16, reg_list, mem_list)
            ext = sw_obj.ext_16_str(sw_obj.ext(imm16))
            nt = rmv(bin(int(nt)))
            ns = rmv(bin(int(ns)))
            print("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(
                ext[i:i + 4] for i in range(0, len(ext), 4)))
            print("--------------------------")

        if action == 'add':
            op = '00000'
            func = '100000'
            shamt = '00000'
            add_obj = HandlerR()
            ns = add_obj.get_ns(elses)
            nt = add_obj.get_nt(elses)
            nd = add_obj.get_nd(elses)
            add_obj.add(nd, ns, nt, reg_list)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            print("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)
            print(reg_list)
            print("--------------------------")

        if action == 'subu':
            op = '000000'
            shamt = '00000'
            func = '100010'
            subu_obj = HandlerR()
            ns = subu_obj.get_ns(elses)
            nt = subu_obj.get_nt(elses)
            nd = subu_obj.get_nd(elses)
            subu_obj.subu(nd, ns, nt, reg_list)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            print("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)
            print(reg_list)
            print("--------------------------")

        if action == 'sub':
            op = '00000'
            shamt = '00000'
            func = '100010'
            sub_obj = HandlerR()
            ns = sub_obj.get_ns(elses)
            nt = sub_obj.get_nt(elses)
            nd = sub_obj.get_nd(elses)
            sub_obj.sub(nd, ns, nt, reg_list)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            print("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)
            print(reg_list)
            print("--------------------------")
        if action == 'slt':
            op = '000000'
            shamt = '00000'
            func = '101010'
            slt_obj = HandlerR()
            ns = slt_obj.get_ns(elses)
            nt = slt_obj.get_nt(elses)
            nd = slt_obj.get_nd(elses)
            slt_obj.slt(nd, ns, nt, reg_list)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            print("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)
            print("--------------------------")
        if action == 'sltu':
            op = '000000'
            shamt = '00000'
            func = "101011"
            slt_obj = HandlerR()
            ns = slt_obj.get_ns(elses)
            nt = slt_obj.get_nt(elses)
            nd = slt_obj.get_nd(elses)
            slt_obj.sltu(nd, ns, nt, reg_list)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            print("#32'b" + op + '_' + str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(
                5) + '_' + shamt + '_' + func)
            print("--------------------------")
        if action == 'beq':
            op = '000100'
            beq_obj = HandlerI()
            ns = beq_obj.get_ns(elses)
            nt = beq_obj.get_nt(elses)
            rs = int(reg_list[int(ns)])
            rt = int(reg_list[int(nt)])
            nt = rmv(bin(int(nt))).zfill(5)
            ns = rmv(bin(int(ns))).zfill(5)
            imm16 = '0000_0000_0000_0001'
            print("#32'b" + op + "_" + ns + "_" + nt + "_" + imm16)
            if rt == rs:
                mark = elses[-1]
                if isinstance(mark, str):
                    for each in opt_list_with_line_num:
                        print(each)
                        opt = list(each.values())
                        if opt[0][0].startswith(mark):
                            key_tmp = list(each.keys())
                            val_tmp = opt[0]
                            lst_tmp = [val_tmp[0].split(':')[-1]] + val_tmp[1:]
                            opt_list_with_line_num[opt_list_with_line_num.index(each)] = \
                                {key_tmp[0]: lst_tmp}
                            line_jump = int(key_tmp[0])
                            print('hello world')
                            print(line_jump)
                            print(opt_list_with_line_num)
                elif isinstance(mark, int):
                    pass
    except Exception as e:
        print(e)
        print(trace())
        print('---???---')
