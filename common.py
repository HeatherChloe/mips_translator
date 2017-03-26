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

