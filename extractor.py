#!/usr/bin/env python3

import os
import sys
import requests
import re

# Extract previous inputs and answers
assert len(sys.argv) == 2 if 'SESSION' in os.environ else 3, "Usage: SESSION=??? $0 year || $0 year session_id"
year = sys.argv[1]
session = sys.argv[2] if len(sys.argv) == 3 else os.environ.get('SESSION')
answer_re = re.compile(r'<p>Your puzzle answer was <code>([\w,]+)</code>.</p>')

def get(path):
    url = 'https://adventofcode.com/'+year+'/'+path
    return requests.get(url, cookies=dict(session=session))

for i in range(0, 25):
    day = str(i+1)
    inp = get('day/' + day + '/input')
    if inp.status_code == 200:
        with open(day + '.input', 'w') as f:
            f.write(inp.text)
        ans = get('day/' + day)
        assert ans.status_code == 200
        answers = answer_re.findall(ans.text)
        if len(answers) != 2:
            print(day + ': ' + str(len(answers)) + ' answer(s)')
        if len(answers) > 0:
            with open(day + '.answers', 'w') as f:
                f.write('\n'.join(answers))
    else:
        print(day + ': no input')