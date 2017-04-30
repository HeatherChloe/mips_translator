# -*- coding: utf-8 -*-
import os
import shutil

import sys

from common import gen_lines


def file_to_edit_ver(file_name):
    try:

        print("############File To Edit Ver############")
        print("#               LOADING                #")

        result = []
        fp = open(file_name, encoding='utf-8')
        line_count = 0
        for line in fp:
            where_main_line = 0
            line_count += 1
            if not line.startswith('main'):
                where_main_line += 1
            elif line.startswith(('main')):
                rst = {str(line_count): gen_lines(line.split(':')[-1]).replace(' ', ',').split(',')}
                result.append(rst)
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
