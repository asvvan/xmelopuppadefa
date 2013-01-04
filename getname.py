def checkforanomaly(line):
	if line.split('>')[1]=="<b":
		return line.split('>')[2].split('<')[0]
	else:
		return line.split('>')[1].split('<')[0]

def gettitle(filename):
	artitle=""
	f = open(filename.strip(), 'r')
	for line in f:
		for line2 in line.split('>'):
			for word in line2.split():
				if word=="font=\"0\"":
					titlepart=checkforanomaly(line)
					artitle=artitle+titlepart
	return artitle


filelist = open('xmllist', 'r')
fileoutput = open('xmltitles', 'w')
for currentpdf in filelist:
	artitle=gettitle(currentpdf)
	strtowrite = currentpdf.strip() + "\t" + artitle + "\n"
	fileoutput.write(strtowrite)