#!/usr/bin/env python3
import random
import alex_sasses, brendan_sasses

sasses = set(alex_sasses.sasses)
sasses = sasses | set(brendan_sasses.sasses)

sass = random.sample(sasses, 1)[0]
print(sass)
