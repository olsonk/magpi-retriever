import urllib

issue = 39

for i in range(47):
	current = issue + i
	url = "https://www.raspberrypi.org/magpi-issues/MagPi%02d.pdf" % current
	filename = "MagPi%02d.pdf" % current
	
	urllib.urlretrieve(url, filename)