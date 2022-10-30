# Overview

I'm a sucker for maps and data, so I decided to learn how to write this program to teach me how I can use GIS mapping.  What I wrote is a map application that displays the location of every temple of The Church of Jesus Christ of Latter-day Saints, including the ones that are under construction or have been announced.  Each point on the map shows the temple name and its dedication date when you click on it.

There were 300 points I put on this map, so I used a CSV file that showed the temples' names, latitudes and longitudes, their status (dedicated, under construction, or announced), and the dedication date (if applicable).  The CSV file was found online, but I did make sure to add some data and remove some data I didn't need for this program.

[Software Demo Video](https://youtu.be/40qOv5qBgOs)

# Development Environment

Text Editor: VS Code
Languages: JavaScript, HTML, & Python
Source Control System: GitHub
Other Tools: ArcGIS, CSV Library in Python

# Useful Websites

* [Tutorials for ArcGIS Developers](https://developers.arcgis.com/documentation/mapping-apis-and-services/tutorials/)
* [Church of Jesus Christ Temples](https://churchofjesuschristtemples.org/maps/downloads/) - This is actually where I got the starter CSV file to plot out all the points on my map.

# Future Work

* Learn how to impliment photos into the map pop-ups.
* Learn how to impliment a filter to only display certain points at a time.