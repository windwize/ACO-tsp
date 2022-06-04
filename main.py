
import argparse
from ACO import ACO

from utils import random_init,calculate_distance,load_example

def default_argument_parser():
    parser = argparse.ArgumentParser(description="Ant Colony Algorithm")
    parser.add_argument("--test",nargs="?")
    parser.add_argument('--ant', default=72,type=int)
    parser.add_argument('--points', default=20,type=int)
    parser.add_argument('--generation', default=100,type=int)
    parser.add_argument('--alpha', default=4.0,type=float)
    parser.add_argument('--beta', default=5.0,type=float)
    parser.add_argument('--rho', default=0.1,type=float)
    parser.add_argument('--q', default=100,type=float)
    parser.add_argument('--strategy', default=2,type=int)
    parser.add_argument('--min_x', default=0,type=int) 
    parser.add_argument('--max_x', default=50,type=int) 
    parser.add_argument('--min_y', default=0,type=int) 
    parser.add_argument('--max_y', default=100,type=int)
    return parser

def main():
    args = default_argument_parser().parse_args()

    if args.test!=None:
        points,distance = load_example(args.test)
    else:
        points = random_init(args.points,args.min_x,args.max_x,args.min_y,args.max_y)
        distance = calculate_distance(points)
    aco = ACO(
        ant_count=args.ant,
        generations=args.generation,
        alpha=args.alpha,
        beta=args.beta,
        rho=args.rho,
        q=args.q,
        strategy=args.strategy,
        points=points,
        distance=distance,
    )
    aco.run()

if __name__ == '__main__':
    main()