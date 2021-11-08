from cotmm_resources import *


def cotmm_help():
    print_message = [
        "Welcome to cotmm, a cli probe for AWS to give you information about your resources",
        "usage: cotm [resources]",
        "supported resources include:",
    ]
    print_message.extend(
        [
            " " + r + " (by " + resource_meta[r]["identifier"] + ")"
            for r in resource_meta
        ]
    )

    print("\n".join(print_message))
    exit()


def cotmm_output(type, output):
    output = ["cotmm", cotmm_output_types[type], output]
    print(": ".join(output))


cotmm_output_types = {
    "o": " output",
    "e": "  error",
    "h": "   help",
    "c": "aws-cli"}
