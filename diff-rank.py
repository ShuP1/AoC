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
leaderboard = requests.get(url, cookies=dict(session=session)).json()['members']

def rank_by_day(get_score, top, fmt):
    for day in range(1, 25+1):
        scores = []
        for id, member in leaderboard.items():
            stars = member.get('completion_day_level', {}).get(str(day), {})
            score = get_score(stars)
            if score is not None:
                scores.append((member.get('name') or id, score))

        if scores:
            print('Day', day, ':')
            print('\n'.join(map(lambda t: '{0} ({1})'.format(t[0], fmt(t[1]) if fmt else t[1]), sorted(scores, key=lambda t: t[1])[:top])))
            print()

def rank_all_days(get_score, acc, top, fmt):
    scores = []
    max_days = 0
    for id, member in leaderboard.items():
        m_scores = list(filter(lambda v: v, map(get_score, member.get('completion_day_level', {}).values())))
        if len(m_scores) < max_days: continue
        if len(m_scores) > max_days:
            scores = []
            max_days = len(m_scores)

        scores.append((member.get('name') or id, acc(m_scores)))

    print('For all', max_days, 'days:')
    print('\n'.join(map(lambda t: '{0} ({1})'.format(t[0], fmt(t[1]) if fmt else t[1]), sorted(scores, key=lambda t: t[1])[:top])))

def star2delay(stars): 
    if '1' in stars and '2' in stars:
        return stars['2']['get_star_ts'] - stars['1']['get_star_ts']
def pretty_delay(seconds):
    return timedelta(seconds=seconds)

print('Rank by delay between first and second stars')
rank_by_day(star2delay, 3, pretty_delay)

rank_all_days(star2delay, sum, 5, pretty_delay)