# Assumes an ms has name 'm'
# run inside casapy run 'run -i '
nn=vishead(vis=m,mode="get",listitems=[],hdkey="field",hdindex="",hdvalue="")
names=nn[0]
listobs(vis=m)
for n in names:
    split(vis=m,field=n,outputvis=n+".ms",datacolumn="data")
#now have multiple ms
for n in names:
    exportuvfits(vis=n+".ms", fitsfile=n+".fits", datacolumn="data")
#the end

