import sys
import file_works
from common import gen_lines

order_list = []
# like this order_list[{0:{"order":[ori $1,$0,0x0005]}}]
reg_list = []
# like this [{1:0x0001}, {2:1}]
mem_list = []
# like this [{1:0x0001}, {2:1}]

def ready_to_run(now_name):
    try:
        print("###########Prepare To Run###########")
        fp = open(now_name, 'r+')
        if fp is None:
            sys.exit(0)

        for line in fp:
            count = 0
            if not line.startswith("main"):
                count += 1
            elif line.startswith("main"):
                stri = line.split(':')[-1]
                print(gen_lines(stri))
    except Exception:
        print("############Exception############")
        print(Exception)
        print("############Exception############")
if __name__ == '__main__':
    now_name = file_works.file_to_edit_ver('E:\workSpace\mips_translator\\test_for_main_space.txt')
    ready_to_run(now_name)
    print("############Ready To Run############")
