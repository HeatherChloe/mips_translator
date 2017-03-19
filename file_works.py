import os
import shutil


def file_to_edit_ver(src_name):
    try:
        print("############File To Edit Ver############")
        print("#               LOADING                #")

        file_in_path = os.path.abspath(src_name)

        path = os.path.dirname(src_name)
        no_name = path + '\\edited_version'
        # no_name += tmp_folder

        if os.path.exists(no_name) is False:
            os.mkdir(os.path.join(path, no_name))

        new_path = path + '\\edited_version'
        shutil.copy(file_in_path, new_path)
        file_tmp = (new_path + '\\' + os.path.basename(src_name) + '.tmp')

        if os.path.exists(file_tmp) is True:
            os.remove(file_tmp)

        fore_name = new_path + '\\' + os.path.basename(src_name)
        now_name = file_tmp
        os.rename(fore_name, now_name)
        print(file_tmp)
    except Exception:
        print("############Exception############")
        print(Exception)
        print("############Exception############")
    print("############File To Edit Ver############")
if __name__ == "__main__":
    file_to_edit_ver('E:\workSpace\mips_translator\\05136064.txt')