def fix_data(src):
    old = open(src)
    csv = ""
    for line in old.readlines():
        row = line.split(',')
        if row[0][-1].isdigit():
            row[0] = row[0][:-1]
        if row[1][-1].isdigit():
            row[1] = row[1][:-1]
        if row[2] == '': #aggregate empty violent crime value
            row[2] = sum([int(x) if x != '' else 0 for x in row[3:8]])
        for x in row[:-1]:
            csv += str(x)+','
        csv += '\n'
    old.close()
    new = open(src,'w')
    for line in csv:
        new.write(line)
    new.close()
        
src = input("src: ")
while src != '':
    src = src.replace('\"','')
    fix_data(src)
    src = input("src: ")
