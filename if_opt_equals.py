from common import *


def if_opt_eqs(opt, reg_list):
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
            init_nd(reg_list, nt)
            ori_obj.ori(nt, ns, imm16, reg_list)
            nt = rmv(bin(int(nt))).zfill(5)
            ns = rmv(bin(int(ns))).zfill(5)
            print("#32'b" + op + "_" + ns + "_" + nt + "_" + '_'.join(ext[i:i + 4] for i in range(0, len(ext), 4)))
            print(reg_list)
            print("--------------------------")
    except Exception as e:
        print(e)
        print('---???---')
