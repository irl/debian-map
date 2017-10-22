# debian-map
Mapping Debian Things

This used to run at map.debian.net but I no longer have the time to
maintain it.

The code in `update-developers.py` will fetch the coordinates of
Debian contributors from the website and convert them to a KML file.

The code in `html` was the webroot, and the KML files were pushed into
the `data` directory there to be used by the embedded OpenStreetMap.

To find a map of Debian mirrors, see:
http://ircbots.debian.net/mirrormap/

I believe the KML file for the mirrors was based on the above link, but
I do not have the code I used. To produce the KML, the same system of
grabbing the list of mirrors and then using GeoIP databases could be used,
instead of using the data from that site.
