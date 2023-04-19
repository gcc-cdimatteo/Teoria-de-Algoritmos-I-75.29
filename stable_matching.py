import sys, conj, utils

def match(A, B):
    matches = conj.matches()

    A.sort()
    B.sort()

    while not A.empty():
        a = A.pop()
        b = B.y_closest(a)
        if not b: continue
        matches.match(a, b)
    
    return matches

def main():
    args = sys.argv[1:]

    A = conj.conj()
    B = conj.conj()

    if len(args) == 0:
        A_path = utils.HKEY_FILE_PATH_A
        B_path = utils.HKEY_FILE_PATH_B
    else:
        A_path = args[utils.HKEY_FILE_PATH_A_POS]
        B_path = args[utils.HKEY_FILE_PATH_B_POS]

    conj.import_coords(A_path, A)
    conj.import_coords(B_path, B)

    matches = match(A, B)

    matches.print()

    matches.print_file()

main()