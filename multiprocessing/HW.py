import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--str', dest='str', required=True)
parser.add_argument('-l', '--list', nargs='+', dest='list', required=True)
args=parser.parse_args()
print(args.str)
print(args.list)