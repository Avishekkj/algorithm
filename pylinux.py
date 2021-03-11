import os
import  subprocess

out = subprocess.Popen(['wc', '-l', 'rename.py'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)


stdout,stderr = out.communicate()

result = os.system("df -h")

