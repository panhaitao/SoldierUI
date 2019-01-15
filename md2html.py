#!/usr/bin/env python3

import sys
import markdown


md = sys.stdin.read()
exts = ['markdown.extensions.extra','markdown.extensions.tables']

ret=markdown.markdown(md,extensions=exts)

sys.stdout.write( "%s" % ret)

