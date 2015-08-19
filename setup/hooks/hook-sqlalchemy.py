import sqlalchemy.orm
hiddenimports = []
for n in dir(sqlalchemy.orm):
    hiddenimports.append("sqlalchemy.orm." + n)
    print "!!!!!!!!!!", n

