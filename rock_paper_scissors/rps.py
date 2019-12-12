#!/usr/bin/python

import sys

# r, p, s

# rr, rp, rs
# pr, pp, ps
# sr, sp, ss

# rrr, rrp, rrs
# rpr, rpp, rps
# rsr, rsp, rss
# prr, prp, prs
# ppr, ppp, pps
# psr, psp, pss
# srr, srp, srs
# spr, spp, sps
# ssr, ssp, sss


def rock_paper_scissors(n):
    output = [[0 for i in range(n)] for i in range(3**n)]
    return output



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(0))