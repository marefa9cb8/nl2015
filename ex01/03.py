# -*- coding: utf-8 -*-
import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tmp = re.sub('[.,]',"",str)
words = tmp.split()
result = []
for word in words:
  result.append(len(word))
print result
