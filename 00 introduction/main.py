#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

regex = r'1995年6月1日|1995/6/1|1995\-6\-1|1995\-06\-01|1995\-06'
s = '•”xxx出生于1995年6月1日” • ”xxx出生于1995/6/1” • ”xxx出生于1995-6-1” • ”xxx出生于1995-06-01” • ”xxx出生于1995-06”'
print(re.findall(regex, s))
