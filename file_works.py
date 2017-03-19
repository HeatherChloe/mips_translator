import os
import shutil


def file_to_edit_ver(src_name):
    try:
        print("############File To Edit Ver############")
        print("#               LOADING                #")

        file_in_path = os.path.abspath(src_name)

        path = os.path.dirname(src_name)
        new_path = path + '\\edited_version'

        if os.path.exists(new_path) is False:
            os.mkdir(os.path.join(path, new_path))

        shutil.copy(file_in_path, new_path)
        fore_name = new_path + '\\' + os.path.basename(src_name)
        file_tmp = (fore_name + '.tmp')

        if os.path.exists(file_tmp) is True:
            os.remove(file_tmp)

        now_name = file_tmp
        os.rename(fore_name, now_name)
        print(file_tmp)
        return now_name
    except Exception:
        print("############Exception############")
        print(Exception)
        print("############Exception############")
    print("############File To Edit Ver############")
