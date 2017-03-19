# may rewrite with C


def gen_lines(line):
    line = line.lstrip()
    # result = ''.join(result_list)
    count_space = 0
    result_str = ""
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
    print(result)
    return result


if __name__ == '__main__':
    line = " ori  $1,  $0,      0x0005               #32'b001101_00000_00001_0000_0000_0000_0101"
    gen_lines(line)