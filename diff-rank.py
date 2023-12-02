#!/usr/bin/env python3

import requests
import sys
import os
from datetime import date, timedelta

usage = "Usage: SESSION=? $0 team (year) | $0 team year session_id"
assert len(sys.argv) + (1 if 'SESSION' in os.environ else 0) in [3, 4], usage

session = sys.argv[3] if len(sys.argv) == 4 else os.environ.get('SESSION')
team = sys.argv[1]
year = sys.argv[2] if len(sys.argv) > 2 else date.today().year

url = 'https://adventofcode.com/{0}/leaderboard/private/view/{1}.json'.format(year, team)
members = requests.get(url, cookies=dict(session=session)).json()['members']
N = max(len(members) * 2, 100)
members = [(data.get('name') or id, data.get('completion_day_level', {}))
    for id, data in members.items()]

last_day = max(int(day) for _,days in members for day in days)
star2delays = [(name, [
    stars['2']['get_star_ts'] - stars['1']['get_star_ts']
    if '1' in stars and '2' in stars else None
    for stars in (days.get(str(i+1), {}) for i in range(last_day))
]) for name, days in members if days]

print('Rank by delay between first and second stars')
per_day = 3
for i in range(last_day):
    scores = sorted((days[i], name) for name, days in star2delays if days[i])[:per_day]
    if scores:
        print(f'Day {i+1}:')
        print('\n'.join(f'{name:20}\t{timedelta(seconds=time)}' for time, name in scores))
        print()

print('For all', last_day, 'days:')
points = [0]*len(star2delays)
for i in range(last_day):
    order = sorted((days[i], idx) for idx, (_, days) in enumerate(star2delays) if days[i])
    for j, (_, idx) in enumerate(order):
        points[idx] += N-j
for pts, (name, days) in sorted(zip(points, star2delays), reverse=True)[:10]:
    print(f'{name:20}\t{pts}\t{timedelta(seconds=sum(day for day in days if day))}')
print()

print('Total stars:', sum(len(day) for _,data in members for day in data.values()))
