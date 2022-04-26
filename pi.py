import argparse

def getArgs():
    parser = argparse.ArgumentParser(description='Iterates over a range of numbers, checking to see if and where each one occurs in the number pi.')
    parser.add_argument('--start', type=int, nargs=1, default=0,
                       help='Start searching for numbers in pi beginning at this number. (default=0)')
    parser.add_argument('--stop', type=int, nargs=1, default=500000,
                       help='Stop searching for numbers in pi at this number. (default=500000)')
    parser.add_argument('--path', type=str, nargs=1, default='pi-10000.txt',
                       help='The path to the file containing the number pi. (default="pi.txt")')
    parser.add_argument('--output', type=str, nargs=1, default='positions.txt',
                       help='The path to the file that the position that each number that was found will be output to. (default="positions.txt")')
    args = parser.parse_args()

    return parser, args

def load(filename):
    with open(filename, 'r') as f:
        return f.read()

def save(filename, data):
    print "Saving %s..." % filename,
    with open(filename, 'w') as f:
        f.write(str(data))
    print "saved"

def hello(parser, args):
    print "Running %s" % argparse._sys.argv[0]
    print parser.description
    print "\nProcessing numbers:"

def checkPi(pi, start, stop, output):
    positions = []

    for n in range(start, stop):
        pos = pi.find(str(n))
        positions.append((n, pos))

        if n % 1000 == 0:
            print "%d\t" % n,
    print

    save(output, positions)
    save("sorted.txt", sorted(positions, key=lambda x:x[1]))
    return positions, start, stop

def goodbye(positions, start, stop):
    notFound = [t[0] for t in positions if t[1] == -1]

    numSearched = stop - start
    numFound = numSearched - len(notFound)
    print '\n%d/%d = %%%d found' % (numFound*1.0, numSearched, (numFound/numSearched)*100)
    print 'Goodbye!'

def main():
    parser, args = getArgs()
    hello(parser, args)
    print args.path
    pi = load(args.path[0])
    positions, start, stop = checkPi(pi, args.start, args.stop, args.output)
    goodbye(positions, start, stop)

if __name__ == "__main__":
    main()
