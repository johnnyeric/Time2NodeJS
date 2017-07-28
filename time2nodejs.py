import sys
import os
from io import StringIO
import contextlib
import subprocess


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf


if __name__ == "__main__":
    st = get_stdin()
    # print(st)
    with stdoutIO() as s:
        try:
            tmpfold = os.environ["TMPDIR"]
            tmpfile = "%s/%s" % (tmpfold, "script.js")
            # print(tmpfile)
            f = open(tmpfile, 'w')
            print(st, file=f)
            f.close()
            p1 = subprocess.Popen(["node", tmpfile], stdout=subprocess.PIPE)
            print(p1.stdout.read().decode('utf-8'))
        except BaseException as e:
            print(e)
    print(s.getvalue())

