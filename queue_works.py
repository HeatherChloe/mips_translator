import if_opt_equals
import main


class debugQueue:
    def __init__(self, reg_list, mem_list, opt_list_with_line_num):
        self.queue = None
        self.reg_list = reg_list
        self.mem_list = mem_list
        self.opt_list_with_line_num = opt_list_with_line_num
        # self.opt = opt

    def push(self):
        self.queue = self.opt_list_with_line_num

    def q_pop(self, count):
        try:
            opt = self.opt_list_with_line_num[count]
            main.if_opt_eqs_func(opt, self.reg_list, self.mem_list, self.opt_list_with_line_num)

        except Exception as e:
            if_opt_equals.result_str += "end of file"
