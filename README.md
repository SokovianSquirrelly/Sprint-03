# Overview

I'm a sucker for maps and data, so I decided to learn how to write this program to teach me how I can use GIS mapping.  What I wrote is a map application that displays the location of every temple of The Church of Jesus Christ of Latter-day Saints, including the ones that are under construction or have been announced.  Each point on the map shows the temple name and its dedication date when you click on it.

There were 300 points I put on this map, so I used a CSV file that showed the temples' names, latitudes and longitudes, their status (dedicated, under construction, or announced), and the dedication date (if applicable).  The CSV file was found online, but I did make sure to add some data and remove some data I didn't need for this program.

[Software Demo Video](https://youtu.be/40qOv5qBgOs)

# Development Environment

Text Editor: VS Code

Languages: JavaScript, HTML, & Python

Source Control System: GitHub

Other Tools: ArcGIS, CSV Library in Python, JSON

# Useful Websites

* [Tutorials for ArcGIS Developers](https://developers.arcgis.com/documentation/mapping-apis-and-services/tutorials/)
* [Church of Jesus Christ Temples](https://churchofjesuschristtemples.org/maps/downloads/) - This is actually where I got the starter CSV file to plot out all the points on my map.
* [Temple List on Official Church Website](https://www.churchofjesuschrist.org/temples/list?lang=eng) - All photos were retrieved from here.

# Updates

Frankly I wish I would have done more update notes as I continued working on this throughout the years, but I figured I might as well start now.

I should note that techically, I do update this program depening on changes to temples throughout the world.  However, I feel like not every single update like that warrants a whole section about new temples or temples that started construction or whatever.  Instead, this section will only be dedicated to software or UI changes.

## 2022-2025

* I added a very similar CSV file full of predictions on where temples could be announced.  There is also a "confidence level" with each one, ranging from "Very Low" to "High".  Put simply, this is a gauge of how likely I think a temple will be announced in that city/area in the near future.
* If a temple is dedicated, I decided to put a little number next to their dedication date to show when each temple was dedicated chronologically.  For example, since the St. George Utah Temple was the first one dedicated, I put "#1: 6 April 1877" in its popup.
* The announced temples (i.e. not yet under construction) has been split into two categories: the ones where the building site has been announced and the ones where we do not yet know where specifically each temple will be.  If the site has been announced for a temple, the points on the map will be orange.  Otherwise, they will be red.  Truth be told, this is more for me specifically because if a temple site/address has actually been announced, I don't want to worry about checking every single latitude and longitude to see if they match up.  Thankfully, something that has helped is that the website that I get my information from has also specified which temples have had their sites announced and which ones haven't.

## September 2025 Update

* I decided to do away with CSV files and instead use JSON files to populate all the points.  Beforehand, what I did is use a python program to list out a displayPoint() function for each temple and prediction and then copy and paste them into the main file.  This made the HTML file absolutely massive and pretty clunky to navigate.  So I put all the data from the CSV files into two JSON files and changed the main file to read the JSON files and populate the points automatically as if it was fetching from an API.  The program now functions the same way on the UI while reducing the HTML file down to a fraction of the size.  As for the python script and the CSV files, I couldn't bring myself to fully delete them, even though technically, they're still saved on previous versions on GitHub anyway.  So I decided, at least for the time being, to put them in a folder called "legacy".

## October 2025 Update

* Dedicated temples (and those very close to dedication) will now have a displayed photo with them when they pop up.  These photos are linked directly to the church's website.  I am linking actual photographs ONLY, so there won't be any artistic renderings of temples that are under construction.
* There are two temples that were completely torn down and, as of the time of writing this, are being completely reconstructed.  Those are the Stockholm Sweden Temple and the Provo Utah Temple.  The one in Stockholm (from what info I could find) is going to look incredibly similar on the exterior once it is completed.  As for the one in Provo, it will look completely different.  So for now, both temples will have photos from before demolition being displayed.  More than likely, I'll just update the photo to the new temple in Stockholm once construction is complete unless it ends up looking substantially different, in which case I'll include photos of both versions of the temple.  As for the Provo Utah Rock Canyon Temple, I'll include both versions of the temple once construction is complete.

# Future Goals

* Learn how to impliment a filter to only display certain points at a time.
* Add a key to display on the map explaining what the different colored dots mean.