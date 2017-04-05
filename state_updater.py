from xlrd import open_workbook

def xls_to_csv(srcfile,destfolder):
    book = open_workbook(srcfile)  # open workbook
    sheet = book.sheet_by_index(0)  # select first sheet
    
    destfolder = destfolder[:-1]+destfolder[-1].replace('/','')+'/'+srcfile.split(sep='/')[-1][:-3]+'csv'
    wfile = open(destfolder,'w')   # open new csv file
    
    if sheet.cell_value(3,0) == '' or sheet.cell_value(3,1) != '':
        write_line(wfile, sheet.row_values(3,0)) # potential additional header info
    missing = ""
    row = 4
    while sheet.cell_type(row,1) > 0:    # take all but the footnotes
        line = sheet.row_values(row,0)
        if sheet.cell_type(row,0) > 0:
            missing = sheet.cell_value(row,0)
        else:
            line[0] = missing
        write_line(wfile, line)
        row += 1
    wfile.close()

def write_line(wfile, row):
    global x
    for x in row:
        x = str(x).replace('\n','')
        try:
            wfile.write(x+',')
        except: # weird character that pops up in the older files
            x = x.replace('\ue83a',' ')
            wfile.write(x+',')
    wfile.write('\n')
            
while(True):
	src = input("src: ")
	print("1 "+src)
	src = src.replace('\"','')
	xls_to_csv(src,"./data")
