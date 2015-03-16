#!/usr/bin/env python

#tested on python2.7
# https://2013.picoctf.com bitwise
#encryption array
#user_arr.append( ( ( (thing << 5) | (thing >> 3) ) ^ 111) & 255 )

verify_arr = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
user_arr = []
done_arr = []


for thing in verify_arr:
  axor = (thing ^ 111)
  aor = (axor >> 5) | (axor << 3)
  user_arr.append(aor & 255)


print user_arr

for bla in user_arr:
  done_arr.append(chr(bla))

print done_arr


