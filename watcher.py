#!/usr/bin/env python3

import os
import sys
from datetime import date
from time import sleep
import requests
import re
import subprocess, platform

OVERRIDE = False

usage = "Usage: SESSION=? $0 (year day) | $0 (year day) session_id"

assert len(sys.argv) + (1 if 'SESSION' in os.environ else 0) in [2, 4], usage

answer_re = re.compile(r'<p>Your puzzle answer was <code>([\w,]+)</code>.</p>')

session = sys.argv[2] if len(sys.argv) in [2, 4] else os.environ.get('SESSION')
today = date.today() # assume timezone >= UTC-5
if len(sys.argv) > 1:
    year, day = sys.argv[1:3]
elif today.month == 12:
    year = str(today.year)
    day = str(today.day)
else:
    print('No in december', usage)

def get_input():
    url = 'https://adventofcode.com/'+ year + '/day/' + day + '/input'
    return requests.get(url, cookies=dict(session=session))

def get_text():
    url = 'https://adventofcode.com/'+ year + '/day/' + day
    return requests.get(url, cookies=dict(session=session))

def post_answer(part, ans):
    url = 'https://adventofcode.com/' + year + '/day/' + day + '/answer'
    return requests.post(url, data={u'level': str(part), u'answer': ans}, cookies=dict(session=session))

print('AoC', year, day)

input_file = 'data/' + year + '/' + day + '.input'
inp = get_input()
input_text = inp.text
if inp.ok:
    print('input: ', input_text.split('\n', 3)[:-1])
else:
    print(inp.reason, input_text)
    exit(1)

if OVERRIDE or not os.path.isfile(input_file):
    with open(input_file, 'w') as f:
        f.write(input_text)

answers = []
txt = get_text()
if txt.ok:
    answers = answer_re.findall(txt.text)
else:
    print(txt.reason, txt.text)
    exit(1)

code_path = 'src/' + year + '/' + day + '.py'
if not os.path.isfile(code_path):
    with open('src/template.py') as tpl:
        with open(code_path, 'w') as f:
            f.write(tpl.read())

def open_editor(path):
    if platform.system() == 'Darwin':
        subprocess.call(('open', path))
    elif platform.system() == 'Windows':
        os.startfile(path)
    else:
        subprocess.call(('xdg-open', path))

open_editor(code_path)
stamp = os.stat(code_path).st_mtime
while len(answers) < 2:
    sleep(.5)
    if stamp != os.stat(code_path).st_mtime:
        stamp = os.stat(code_path).st_mtime

        result = subprocess.run(sys.executable + ' ' + code_path, shell=True, stdout=subprocess.PIPE, input=input_text, text=True)
        if result.returncode > 0:
            continue

        ans = result.stdout.strip().split('\n')
        print(ans)
        if input('Submit [y] ? ') != 'y':
            continue

        part = len(answers) + 1
        ans = ans[part - 1]
        res = post_answer(part, ans)
        start = res.text.index('<article><p>')
        end = res.text.index('</p></article>', start)
        out = res.text[start + 12 :end]
        if not out.startswith("That's the right answer!"):
            print(out)
            continue

        print('Correct')
        answers.append(ans)

answer_file = 'data/' + year + '/' + day + '.answers'
if OVERRIDE or not os.path.isfile(answer_file):
    with open(answer_file, 'w') as f:
        f.write(''.join(ans + '\n' for ans in answers))

print('Done')