# version : python-3.7.3
# author : hemanth-hk

# art lib for printing in different ways
from art import *
# to clear screen before printing
from subprocess import call

def clear(): 
	# check and make call for specific operating system to clear terminal/cmd
	_ = call('clear' if os.name =='posix' else 'cls')
clear()

# read index.html from template folder
index = open("./template/index.html", "r")

# remove \n,\t and spaces from html and get the content
cnt = (str(index.read())).replace('\n','').replace('\t','')

# remove <!DOCTYPE html><html> and </html>
cnt = cnt.replace('<!DOCTYPE html><html>','').replace('</html>','')

# print title and return body
def head(cnt):
	tprint(cnt[cnt.find('<head><title>')+ 13 : cnt.find('</title>')].strip().center(25),font='ascii_new_roman')
	body = cnt[cnt.find('</head>') + 7:]
	return body

body = head(cnt)

# find all the tags present in the body
def find_tags(body):
	tags = {}
	if body.find('<h1>'):
		h1s = [i for i in range(len(body)) if body.startswith('<h1>', i)]
		tags['h1'] = h1s
	if body.find('<p>'):
		ps = [i for i in range(len(body)) if body.startswith('<p>', i)]
		tags['p'] = ps
	if body.find('<div>'):
		divs = [i for i in range(len(body)) if body.startswith('<div>', i)]
		tags['div'] = divs
	if body.find('<ul>'):
		uls = [i for i in range(len(body)) if body.startswith('<ul>', i)]
		tags['ul'] = uls
	if body.find('<ol>'):
		ols = [i for i in range(len(body)) if body.startswith('<ol>', i)]
		tags['ol'] = ols

	# check if body is empty or not
	for x in tags:
		if len(tags[x]) != 0:
			return tags
		else:
			return 0

######### functions for individual tags #########

## h1 function
def h1(body,h1s):
	header = []
	for h1 in h1s:
		header.insert(len(header), str(body[h1 + 4:body.find('</h1>',h1)]))
	for h1 in header:
		tprint(h1.strip(),font="fancy67")

## p function
def p(body,ps):
	p = []
	for p1 in ps:
		p.insert(len(p), str(body[p1 + 3:body.find('</p>',p1)]))
	for p1 in p:
		tprint(p1.strip(),font="fancy57")

## div function
def div(body,divs):
	div = []
	for div1 in divs:
		check = str(body[div1 + 5:body.find('</div>',div1)]).find('</')
		if check == -1:
			div.insert(len(div), str(body[div1 + 5:body.find('</div>',div1)]))
	for div1 in div:
		tprint(div1.strip(),font="fancy72")

## ul function
def ul(body,uls):
	ul = []
	for ul1 in uls:
		ul.insert(len(ul), str(body[ul1 + 4:body.find('</ul>',ul1)]))
	for ul1 in ul:
		lis = [i for i in range(len(ul1)) if ul1.startswith('<li>', i)]
		for li in lis:
			lt = ul1[li + 4: ul1.find('</li>',li)]
			tprint((". " + lt.strip()).center(15),font="fancy66")

## ol function
def ol(body,ols):
	ol = []
	for ol1 in ols:
		ol.insert(len(ol), str(body[ol1 + 4:body.find('</ol>',ol1)]))
	for ol1 in ol:
		lis = [i for i in range(len(ol1)) if ol1.startswith('<li>', i)]
		for li,num in zip(lis,range(1,len(lis) + 1)):
			lt = ol1[li + 4: ol1.find('</li>',li)]
			tprint((str(num) + ". " + lt.strip()).center(15),font="fancy66")



tags = find_tags(body)
if tags:	
	h1(body,tags['h1'])
	p(body,tags['p'])
	div(body,tags['div'])
	ul(body,tags['ul'])
	ol(body,tags['ol'])
else:
	print('Body is empty or contains tags out of scope')





