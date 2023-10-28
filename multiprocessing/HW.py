import argparse
from multiprocessing import Pool

def f(l:tuple[str,str]):
    if "".join(l[0]) in open(l[1], encoding="UTF-8").read().split(): 
        return True
    else:
        return False

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--str', nargs=1, dest='str', required=True)
    parser.add_argument('-l', '--list', nargs='+', dest='list', required=True)
    args=parser.parse_args()

    with Pool() as p:
        print(p.map(f,[(args.str, item) for item in args.list]))