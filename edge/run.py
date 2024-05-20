import sys
import subprocess as sp

import conf

procs = []
for bind in conf.BINDS:
    proc = sp.Popen([sys.executable, 'server.py', bind])
    procs.append(proc)

for proc in procs:
    proc.wait()
