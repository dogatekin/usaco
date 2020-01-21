import sys

problem = sys.argv[1]

print(f'''"""
ID: dotekin1
LANG: PYTHON3
TASK: {problem}
"""
with open("{problem}.in") as fin:
    lines = fin.read().splitlines()
    
    
    
with open("{problem}.out", "w") as fout:
    fout.write(f"{{out}}\\n")''')
