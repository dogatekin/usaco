"""
ID: dotekin1
LANG: PYTHON3
TASK: ride
"""
with open('ride.in') as fin:
    comet, group = fin.read().splitlines()
    
delta = ord('A') - 1

comet_code = 1
for code in map(lambda c: ord(c) - delta, comet):
    comet_code *= code
    
group_code = 1
for code in map(lambda c: ord(c) - delta, group):
    group_code *= code
    
if comet_code % 47 == group_code % 47:
    out = 'GO'
else:
    out = 'STAY'
    
with open('ride.out', 'w') as fout:
    fout.write(out + '\n')