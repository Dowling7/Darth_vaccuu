#!/usr/bin/env python3

import sys
import re
if len(sys.argv) < 2:
    print("USAGE: ./fix_links.py file_to_fix")
    sys.exit(1)

file_to_fix = sys.argv[1]
data = None
with open(file_to_fix, "r") as myfile:
    data= myfile.readlines()

if data is None:
    sys.exit(2)

for l in data:
    print(re.sub(r"\[([^\]]*)\]\(([^\)]*)\)", r'<a-no-proxy href="\2">\1</a-no-proxy>', l))