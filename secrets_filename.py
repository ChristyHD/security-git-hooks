#!/usr/bin/env python3

import argparse
import sys
import re

IGNORE_KEYWORD = "leak-detection-ignore"

for regex in _FILE_CONTENT_REGEXES:
    try:
        re.compile(_FILE_CONTENT_REGEXES[regex])
    except:
        raise


def detect_secret_in_line(line_to_check):
    """compiles regex and checks against line."""
    for rule, regex in _FILE_CONTENT_REGEXES.items():
        if re.search(re.compile(regex), line_to_check):
            return rule


def main(argv=None):
    print("UPDATED")

    return 1


if __name__ == "__main__":
    sys.exit(main())
