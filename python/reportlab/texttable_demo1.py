import texttable as tt

tab = tt.Texttable()

header = ['Manager', 'Club', 'Year']
tab.header(header)

row = ['Ottmar Hitzfeld', 'Borussia Dortmund, Bayern Munich',\
 '1997 and 2001']
tab.add_row(row)
row = ['Ernst Happel', 'Feyenoord, Hamburg', '1970 and 1983']
tab.add_row(row)
row = ['Jose Mourinho', 'Porto, Inter Milan', '2004 and 2010']
tab.add_row(row)

tab.set_cols_width([18,35,15])

tab.set_cols_align(['l','r','c'])
tab.set_cols_valign(['t','b', 'm'])

tab.set_chars(['-','|','+','#'])


s = tab.draw()
print s


