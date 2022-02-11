import sys
import getopt

sys.path.insert(0,"..")
import circle

def main(argv):
    """Main function for circle code to process the file arguments """

    radius = None
    try:
        opts, _args = getopt.getopt(argv, "r:", ["radius="])
    except getopt.GetoptError:
        print('circle.py -r <radius>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('circle.py -r <radius>')
            sys.exit()
        elif opt in ("-r", "--radius"):
            radius = arg

    if radius is None:
       print('circle.py -r <radius>')
    else:
        myC = circle.Circle(float(radius))
        print(myC.summary())


if __name__ == "__main__":
    main(sys.argv[1:])
