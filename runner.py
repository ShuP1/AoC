import sys
import os
import subprocess
import time

# Check solutions with extractor.py data
usage = 'Usage: $0 data "python _.py"'

assert len(sys.argv) == 3, usage

qdir = sys.argv[1]
files = os.listdir(qdir)
days = {}
for path in files:
    parts = path.split('.input', 1)
    if len(parts) == 2:
        day = parts[0]
        inp = None
        with open(os.path.join(qdir, path), 'r') as f:
            inp = f.read()
        ans = None
        with open(os.path.join(qdir, day + '.answers'), 'r') as f:
            ans = f.read()
        days[int(day) if day.isdigit() else day] = (inp, ans.strip())

solutions = sys.argv[2].split('_')
assert len(solutions) == 2, usage

ok = 0
total = 0
for i, (inp, ans) in sorted(days.items()):
    day = str(i)
    cmd = solutions[0] + day + solutions[1]
    begin = time.time()
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, input=inp, text=True)
    delay = round((time.time() - begin) * 1000)  # ms

    if result.returncode > 0:
        print(day + ': exit ' + str(result.returncode))
        print(result.stderr)
    res = result.stdout.strip()
    if ans:
        total += 1
        if ans == res:
            print(day + ': ok (' + str(delay) + 'ms)')
            ok += 1
        else:
            print(day + ': expect ' + repr(ans) + ' got ' + repr(res))
    else:
        print(day + ': no answer got ' + repr(res))

print(str(ok) + ' / ' + str(total))
exit(ok != total)