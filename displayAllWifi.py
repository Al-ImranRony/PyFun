# Showing all wifi by python

import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r", "")

lst = results.split("\n")
lst = lst[4:]
SSids = []

x = 0
while x < len(lst):
    if x % 5 == 0:
        SSids.append(lst[x])
    x += 1

print(results)
print(SSids)