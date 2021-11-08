def cotmm_help():
    print_message = [
        "Welcome to cotmm, a ...",
        "usage: cotm [resources]"
    ]
    print('\n'.join(print_message))
    exit()

def cotmm_output(type, output):
    output = ["cotmm", cotmm_output_types[type], output]
    print(": ".join(output))

cotmm_output_types={
    "o":" output",
    "e":"  error",
    "h":"   help",
    "c":"aws-cli" 
}