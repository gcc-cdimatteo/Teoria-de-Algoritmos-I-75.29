import random, utils

def write_file(path):
    file = open(path, "w+")
    for i in range(utils.HKEY_TEST_POINT_QUANTITY):
        file.write(f"{random.randint(utils.HKEY_TEST_BEG_RANGE, utils.HKEY_TEST_END_RANGE)} {random.randint(utils.HKEY_TEST_BEG_RANGE, utils.HKEY_TEST_END_RANGE)}")
        if i != utils.HKEY_TEST_POINT_QUANTITY-1: file.write("\n")

    file.close()

a_file = write_file(utils.HKEY_FILE_PATH_A)
b_file = write_file(utils.HKEY_FILE_PATH_B)
