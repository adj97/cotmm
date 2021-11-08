import sys
from cotmm_cli import *
from cotmm_resources import *

if __name__ == "__main__":

    # empty args
    if len(sys.argv) == 1:
        # help
        cotmm_help()

    # resource declaration
    identifiers = sys.argv[1:]

    for identifier in identifiers:
        resource_type = getrtype(identifier)
        getrinfo(resource_type, identifier)
