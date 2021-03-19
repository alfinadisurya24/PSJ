import sys
script  =  sys.argv[0]
def print_usage():
    sys.exit(f'Usage: python {script} pattern')
def main(argv):
    if len(argv) < 1 :
        print_usage()
    pattern = argv[0]
    lines = sys.stdin
    if len(argv) > 1:
        lines = open(argv[1])
    for line in lines:
        if pattern in line:
            print(line.strip())

if __name__ == '__main__':
    main(sys.argv[1:])
