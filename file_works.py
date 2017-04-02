# -*- coding: utf-8 -*-
import os
import shutil

import sys

from common import gen_lines


def file_to_edit_ver(file_name):
    try:

        print("############File To Edit Ver############")
        print("#               LOADING                #")
        # file_in_path = os.path.abspath(src_name)
        #
        # path = os.path.dirname(src_name)
        # new_path = path + '\\edited_version'
        #
        # if os.path.exists(new_path) is False:
        #     os.mkdir(os.path.join(path, new_path))
        #
        # shutil.copy(file_in_path, new_path)
        # fore_name = new_path + '\\' + os.path.basename(src_name)
        # file_tmp = (fore_name + '.tmp')
        #
        # if os.path.exists(file_tmp) is True:
        #     os.remove(file_tmp)
        #
        # now_name = file_tmp
        # os.rename(fore_name, now_name)
        # print(file_tmp)
        result = []
        fp = open(file_name, encoding='utf-8')
        # fp_new = open(now_name, 'w+', encoding='utf-8')
        line_count = 0
        for line in fp:
            where_main_line = 0
            line_count += 1
            if not line.startswith('main'):
                where_main_line += 1
            elif line.startswith(('main')):
                rst = {str(line_count): gen_lines(line.split(':')[-1]).replace(' ', ',').split(',')}
                result.append(rst)
                # fp_new.write(gen_lines(line.split(':')[-1]) + '\n')
                for line in fp.readlines()[where_main_line:]:
                    line_count += 1
                    line = line.lstrip()
                    if line.startswith('#') or line.startswith('\t') or line == '':
                        continue
                    else:
                        line_num = line_count
                        line_ = gen_lines(line)
                        line_ = line_.replace(' ', ',').split(',')
                        rst = {str(line_num): line_}
                        result.append(rst)
        print(result)
        return result
    except Exception:
        print("############Exception file_works############")
        print(Exception)
        print("############Exception file_works############")
    print("############File To Edit Ver############")
