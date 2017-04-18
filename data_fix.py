global states
global extra

def fix_data(src):
    old = open(src)
    fips = open("./data/FIPS_national.txt")
    csv = ""
    i = 0
    lines = old.readlines()
    fipsids= fips.readlines()
    old.close()
    fips.close()
    for row in lines:
        row = row.split(',')
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
    row = add_fips(row,filedata)
    return row

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

src = input("src: ")
while src != '':
    src = src.replace('\"','')
    fix_data(src)
    src = input("src: ")
