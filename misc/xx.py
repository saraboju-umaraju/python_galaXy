#!/usr/bin/python3
import sys
import re
NONWORD_RE = re.compile('\W+')
idx = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for n, line in enumerate(fp, 1):
        for word in NONWORD_RE.split(line):
            if word.strip():
                idx.setdefault(word, []).append(n)
print(idx)
#for word in sorted(idx, key=str.upper):
 #   print (word, idx[word])
