import webbrowser
import argparse
from units import urls
from includes import file
from includes import scan
from units import banner
from units import chknet

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="Enter url")
parser.add_argument("-i","--input",help="Enter input file name")
parser.add_argument("-o","--output",help="Enter the output file name")
parser.add_argument("-b","--blog",action='store_true',help="Reports")
args = parser.parse_args()

def main():
    if args.url:
        banner.banner()
        scan.cvescan(args.url,args.output)

    if args.input:
        banner.banner()
        file.reader(args.input,args.output)
    
    if args.blog:
        banner.banner()
        webbrowser.open(urls.data.blog)

if __name__ == "__main__":
    if chknet.net():
        main()
    else:
        print("\ncheck internet")