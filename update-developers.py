#!/usr/bin/env python

import kmldom
import urllib2
import re

factory = kmldom.KmlFactory_GetFactory()
folder = factory.CreateFolder()

coords = urllib2.urlopen("https://www.debian.org/devel/developers.coords").readlines()

for line in coords:
	coord = line.strip()[:-2].strip()
	lat, lon = re.split("  *", coord)
	placemark = factory.CreatePlacemark()
	placemark.set_name('Debian Developer')
	coordinates = factory.CreateCoordinates()
	coordinates.add_latlng(float(lat), float(lon)) 
	point = factory.CreatePoint()
	point.set_coordinates(coordinates)
	placemark.set_geometry(point)
	folder.add_feature(placemark)

document = factory.CreateDocument()
document.add_feature(folder)
kml = factory.CreateKml()
kml.set_feature(document)

with open("/srv/map.debian.net/html/data/developers.kml", "w") as out:
	out.write(kmldom.SerializePretty(kml))
