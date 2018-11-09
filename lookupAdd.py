import subprocess

with open('address.txt') as i, open('lookup.txt', 'w') as o:
   for line in i:
     if line.strip(): # skips empty lines
        proc = subprocess.Popen(["host", line.strip()],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        o.write('{}\n'.format(proc.communicate()[0]))

print('Done')


COMMAND = "awk '/has address/{print}' lookup.txt > awkedLookup.txt"

subprocess.call(COMMAND, shell=True)
