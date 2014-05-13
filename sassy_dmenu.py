#!/usr/bin/env python3
import random
import alex_sasses, brendan_sasses

sasses = alex_sasses.sasses
sasses.extend(brendan_sasses.sasses)

sass = random.sample(sasses, 1)[0]
print(sass)
