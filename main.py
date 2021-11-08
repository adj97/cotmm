import sys
from cotmm_cli import *

if __name__ == "__main__":

    # empty args
    if len(sys.argv)==1:
        # help
        cotmm_help()

    # resource declaration
    resources = sys.argv[1:]

    cotmm_output("h", ', '.join(resources))