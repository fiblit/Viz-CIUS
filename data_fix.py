import os

global states
global extra

def fix_data(src, startSrc = None):
    old = open(src)
    fips = open("./data/FIPS_national.txt")
    start = open(startSrc)
    csv = ""
    i = 0
    lines = old.readlines()
    fipsids= fips.readlines()
    data = start.readlines()
    old.close()
    fips.close()
    start.close()
    flag = len(lines[0]) > 11 and not "Motor" in lines[0][11]
    for row in lines:
        row = row.split(',')
##        if flag:
##            row = restore_data(row,data)
        row = update_row(row,fipsids)
        for x in row:
            csv += str(x)+','
        csv += '\n'
        i += 1
    new = open(src,'w')
    for line in csv:
        new.write(line)
    new.close()

def update_row(row,filedata):
    row = row[:-1]
    #row = remove_nums(row)
    #row = agg_vc(row)
    #row = fix_dash(row)
    #row = add_fips(row,filedata)
    return row

def restore_data(row,source):
    line0 = remove_nums(source[0].split(','));
    if row[1] == "County":
        return row[:11]+["Motor vehicle theft"]+row[11:]
    for line in source:
        line = remove_nums(line.split(','))
        if row[1] == line[1]:
            return row[:11]+[line[10]]+row[11:]
    print (row[:11]+['']+row[11:])
    return row[:11]+['']+row[11:]

def add_fips(row,data):
    fipsid = ''
    state = row[0].split('-')[0].strip()
    for line in data:
        record = line.split(',')
        if record[0].upper() == state.upper(): # add header
            fipsid = record[1]+record[2]
            break
        elif record[0] == states[state]:
            county = ''
            cWords = row[1].split(' ')  #process multi word counties
            for word in cWords:
                if word not in extra:   #remove police department from names
                    county += word+' '
                else:
                    break
            county = county.replace(' ','').upper()
            fipsC = record[3].replace(' ','').upper()
            if county == fipsC[:len(county)]:
                fipsid = record[1]+record[2]
                break
    row[-1] = fipsid
    return row

def fix_dash(row):
    state = row[0].split('-')[0].strip()
    if state.upper() not in states.keys() and len(state.split(' ')) > 1:
        row[0] = ''
        state = state.split(' ')
        state.insert(-2,'-')
        for x in state:
            row[0] += x+' '
    return row
    
def remove_nums(row):
    row[0] = row[0].strip();
    if row[0][-1].isdigit():
        row[0] = row[0][:-1]
    if row[1][-1].isdigit():
        row[1] = row[1][:-1]
    return row

def agg_vc(row):
    if row[2] == '': #aggregate empty violent crime value
        row[2] = sum([int(x) if x != '' else 0 for x in row[3:8]])
    return row

extra = ["County", "Police", "Department"]
states = {"ALABAMA":"AL","ALASKA":"AK","ARIZONA":"AZ","ARKANSAS":"AR","CALIFORNIA":"CA",
                    "COLORADO":"CO","CONNECTICUT":"CT","DELAWARE":"DE","FLORIDA":"FL","GEORGIA":"GA",
                    "HAWAII":"HI","IDAHO":"ID","ILLINOIS":"IL","INDIANA":"IN","IOWA":"IA",
                    "KANSAS":"KS","KENTUCKY":"KY","LOUISIANA":"LA","MAINE":"ME","MARYLAND":"MD",
                    "MASSACHUSETTS":"MA","MICHIGAN":"MI","MINNESOTA":"MN","MISSISSIPPI":"MS","MISSOURI":"MO",
                    "MONTANA":"MT","NEBRASKA":"NE","NEVADA":"NV","NEW HAMPSHIRE":"NH","NEW JERSEY":"NJ",
                    "NEW MEXICO":"NM","NEW YORK":"NY","NORTH CAROLINA":"NC","NORTH DAKOTA":"ND","OHIO":"OH",
                    "OKLAHOMA":"OK","OREGON":"OR","PENNSYLVANIA":"PA","RHODE ISLAND":"RI","SOUTH CAROLINA":"SC",
                    "SOUTH DAKOTA":"SD","TENNESSEE":"TN","TEXAS":"TX","UTAH":"UT","VERMONT":"VT",
                    "VIRGINIA":"VA","WASHINGTON":"WA","WEST VIRGINIA": "WV","WISCONSIN":"WI","WYOMING":"WY"}


for root,dirs,files in os.walk('.'):
    for name in files:
        if 'data' in root and '.csv' in name and 'Tb_10' in name:
            second = name[-6:-4]+"tbl10.csv"
            #print(name,second)
            fix_data(os.path.join(root,name),os.path.join(root,second))
