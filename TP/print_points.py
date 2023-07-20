from matplotlib import pyplot as plt
import conj, utils

def draw_points(path, colour):
    for point in open(path, 'r'):
        (x, y) = point.rstrip().replace(',', '.').split(' ')
        (x, y) = (float(x), float(y))
        plt.scatter(x, y, c=colour)
        plt.text(x, y, f"({x},{y})")

def draw_matches():
    matches = conj.matches()

    for match in open(utils.HKEY_FILE_PATH_MATCHES, 'r'):
        if not "->" in match or "A -> B" in match: continue
        matches.import_match(match)
    
    for match in matches.as_list():
        plt.plot(match[0], match[1], c='red')

def main():
    draw_points(utils.HKEY_FILE_PATH_A, 'green')
    draw_points(utils.HKEY_FILE_PATH_B, 'blue')
    draw_matches()

    plt.grid(which='major', axis='both', linestyle='-')

    plt.xlim(utils.HKEY_TEST_BEG_RANGE, utils.HKEY_TEST_END_RANGE)
    plt.ylim(utils.HKEY_TEST_BEG_RANGE, utils.HKEY_TEST_END_RANGE)

    plt.show()

main()