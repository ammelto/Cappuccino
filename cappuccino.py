import sys
import subprocess

arg = sys.argv
if len(arg) != 3:
    sys.exit('Usage: cappuccino <input> <output>')

inf = open(arg[1], 'r')
tempOut = "Espresso" + arg[1]
outf = open(tempOut, 'w')

i = 0
o = 0
ilb = []
ob = []
sop = []
dontCare = []
deSop = []
deDontCare = []

for l in inf:
    line = l.partition(' ')
    if line[0] == '.i':
        i = int(line[2])
        outf.write(l)
    elif line[0] == '.o':
        o = int(line[2])
        outf.write(l)
    elif line[0] == '.ilb':
        ilb = line
        outf.write(l)
    elif line[0] == '.ob':
        ob = line
        outf.write(l)
    elif line[0].__contains__('.e'):
        break
    elif l.__contains__('sum'):
        temp = l.split("+")
        sop.append(temp[0])
        if len(temp) > 1:
            dontCare.append(temp[1])
        else:
            dontCare.append('NULL')
    else:
        outf.write(l)

if len(sop) > o:
    sys.exit('Too many SOP equations listed and too few outputs')

for count in range(0, o):
    deSop.append([])
    deDontCare.append([])

for idx, x in enumerate(sop):
    temp = str(x).replace(',', ' ')
    temp = temp.replace('(', ' ')
    temp = temp.replace(')', ' ')
    temp = [int(s) for s in temp.split() if s.isdigit()]
    deSop[idx].extend(temp)

for idx, x in enumerate(dontCare):
    temp = str(x).replace(',', ' ')
    temp = temp.replace('(', ' ')
    temp = temp.replace(')', ' ')
    temp = [int(s) for s in temp.split() if s.isdigit()]
    deDontCare[idx].extend(temp)

print(sop)
print(dontCare)
print(deSop)
print(deDontCare)

binI = pow(2, i)
binO = pow(2, o)

for count in range(0, int(binI)):
    s = str(bin(count))[2:]
    if len(s) < i:
        for x in range(0, i - len(s)):
            s = '0' + s

    outf.write(s)
    outf.write(' ')
    for x in range(0, o):
        if count in deSop[x]:
            outf.write('1')
        elif count in deDontCare[x]:
            outf.write('-')
        else:
            outf.write('0')

    outf.write('\n')
outf.write('\n')
outf.write('.e')
outf.close()

program_name = "espresso"
arguments = ["-Dexact", "-o", "eqntott", tempOut]

command = [program_name]
command.extend(arguments)

f = open(arg[2], 'w')
subprocess.Popen(command, stdout=f).communicate()[0]
print(subprocess.Popen(command).communicate()[0])





