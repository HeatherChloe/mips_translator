from inspect import trace

from common import *
list_to_beq_jump = []
j_list = []

result_str = ""


def result_mine(pc, opt, bytecode_rst):
    global result_str
    opt = list(opt.values())[0]
    result_str += str(pc) + " " + str(opt) + '\n'
    result_str += bytecode_rst
    result_str += '\n\n'


def if_opt_eqs_func(opt, reg_list, mem_list, opt_list_with_line_num):
    try:
        pc = opt_list_with_line_num.index(opt) * 4
        action = list(opt.values())[0][0]
        elses = list(opt.values())[0][0:]
        if action == 'ori':
            ori_obj = HandlerI()
            ori_result = ori_obj.ori(elses, reg_list)
            result_mine(pc, opt, ori_result)

        if action == 'addiu':
            addiu_obj = HandlerI()
            addiu_result = addiu_obj.addiu(elses, reg_list)
            result_mine(pc, opt, addiu_result)

        if action == 'sw':
            sw_obj = HandlerI()
            sw_result = sw_obj.sw(elses, reg_list, mem_list)
            result_mine(pc, opt, sw_result)

        if action == 'lw':
            lw_obj = HandlerI()
            lw_result = lw_obj.lw(elses, reg_list, mem_list)
            result_mine(pc, opt, lw_result)

        if action == 'add':
            add_obj = HandlerR()
            add_result = add_obj.add(elses, reg_list)
            result_mine(pc, opt, add_result)

        if action == 'subu':
            subu_obj = HandlerR()
            subu_result = subu_obj.subu(elses, reg_list)
            result_mine(pc, opt, subu_result)

        if action == 'sub':
            sub_obj = HandlerR()
            sub_result = sub_obj.sub(elses, reg_list)
            result_mine(pc, opt, sub_result)

        if action == 'slt':
            slt_obj = HandlerR()
            slt_result = slt_obj.slt(elses, reg_list)
            result_mine(pc, opt, slt_result)

        if action == 'sltu':
            slt_obj = HandlerR()
            sltu_result = slt_obj.sltu(elses, reg_list)
            result_mine(pc, opt, sltu_result)

        if action == 'beq':
            op = '000100'
            beq_obj = HandlerI()
            ns = beq_obj.get_ns(elses)
            nt = beq_obj.get_nt(elses)
            rs = int(reg_list[int(ns)])
            rt = int(reg_list[int(nt)])
            nt = rmv(bin(int(nt))).zfill(5)
            ns = rmv(bin(int(ns))).zfill(5)

            if rt == rs:
                mark = elses[-1]
                if isinstance(mark, str):
                    imm16 = '0000_0000_0000_0001'
                    beq_result = ("#32'b" + op + "_" + ns + "_" + nt + "_" + imm16)
                    result_mine(pc, opt, beq_result)
                    for each in opt_list_with_line_num:
                        opt_ = list(each.values())
                        if opt_[0][0].startswith(mark):
                            key_tmp = list(each.keys())
                            val_tmp = opt_[0]
                            lst_tmp = [val_tmp[0].split(':')[-1]] + val_tmp[1:]
                            opt_list_with_line_num[opt_list_with_line_num.index(each)] = \
                                {key_tmp[0]: lst_tmp}
                            list_to_beq_jump.append(opt_list_with_line_num
                                                    [opt_list_with_line_num.index({key_tmp[0]: lst_tmp}):])
                            for x in list_to_beq_jump[0][::-1]:
                                location_beq = opt_list_with_line_num.index(opt)
                                opt_list_with_line_num.insert(location_beq + len(list_to_beq_jump), x)
                elif isinstance(mark, int):
                    pass

        if action == 'srl':
            srl_obj = HandlerR()
            srl_result = srl_obj.srl(elses, reg_list)
            result_mine(pc, opt, srl_result)

        if action == 'sll':
            sll_obj = HandlerR()
            sll_result = sll_obj.sll(elses, reg_list)
            result_mine(pc, opt, sll_result)

        if action == 'sra':
            sra_obj = HandlerR()
            sra_result = sra_obj.sra(elses, reg_list)
            result_mine(pc, opt, sra_result)

        if action == 'j':
            op = '000010'
            target = int(elses[1])
            tar_pri = rmv(str(target))
            j_result = ('#32b' + op + '_' + '_'.join(tar_pri[i:i + 4] for i in range(0, len(tar_pri), 4)))
            result_mine(pc, opt, j_result)
            if target > 0:
                j_list = opt_list_with_line_num[int(target)//4 - 1:opt_list_with_line_num.index(opt)]
            else:
                j_list = opt_list_with_line_num[0:opt_list_with_line_num.index(opt)]
            opt_list_with_line_num += j_list

    except Exception as e:
        print(e)
        print(trace())
        print('---opt eqls err---')

