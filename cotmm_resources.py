import re

resource_meta = {
    "ec2": {
        "identifier": "instance-id", 
        "regex_str": r"""i-0[^\W_]{16}"""
        },
    "eni": {
        "identifier": "interface-id", 
        "regex_str": r"""eni-0[^\W_]{16}"""
        },
}

for resource in resource_meta:
    resource_meta[resource]["regex_pat"] = re.compile(
        resource_meta[resource]["regex_str"]
    )


def getrtype(resource_identifier):
    # do some regex matching of the resource specifier
    for resource_type, resource in resource_meta.items():
        if resource["regex_pat"].match(resource_identifier):
            return resource_type


def getrinfo(resource_type, identifier):
    print("getting info for the " + resource_type + " with id " + identifier)
