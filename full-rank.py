#!/usr/bin/env python3

import requests
import sys
import os
from datetime import date, timedelta
from collections import defaultdict

START_YEAR = 2015
END_YEAR = date.today().year

usage = "Usage: SESSION=? $0 team | $0 team session_id"
assert len(sys.argv) + (1 if 'SESSION' in os.environ else 0) == 3, usage

team = sys.argv[1]
session = sys.argv[2] if len(sys.argv) == 3 else os.environ.get('SESSION')

leaderboard = defaultdict(dict)
for year in range(START_YEAR, END_YEAR+1):
    url = 'https://adventofcode.com/{0}/leaderboard/private/view/{1}.json'.format(year, team)
    board = requests.get(url, cookies=dict(session=session)).json()['members']
    for id, member in board.items():
        who = leaderboard[member.get('name') or id]
        for d, stars in member.get('completion_day_level', {}).items():
            for s in range(1, 3):
                if str(s) in stars:
                    who[(year, int(d), s)] = stars[str(s)]['get_star_ts']

stars = sorted([(who, len(s)) for who, s, in leaderboard.items()], key=lambda v: v[1], reverse=True)
print('\n'.join([who + ': ' + str(s) for who, s in stars[:10]]))
