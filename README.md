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
* I acknowledge that there have been temples that have had to go through major renovations or even reconstructions.  In most cases, it appears that the temple exterior has looked largely the same, in which case I will only be including one photo from the latest version of that temple.  HOWEVER, there are two cases where the temple looks substantially different from how it looked in the past.  Those include the Ogden Utah Temple and (at least once it's finished) the Provo Rock Canyon Temple.  Further on down the road, I hope to change my code so that I can display more than one photo and have both versions of each temple being displayed.
* Another one I have to contend with is the Anchorage Alaska Temple.  As of the time of writing this, the church is building a new temple right next to the one that's already there which will be larger than the original temple.  From everything I'm reading, the older temple will still be in operation until the new building is complete.  Now, I don't know at the moment if the new temple will look substanially different from the old one, but if it is, I will try to include both photos.  If not, I'll just get a newer photo of the new structure once it is complete.

## December 2025 Update

* At the last General Conference, Dallin H. Oaks stated that no new temples would be announced at the time.  I kinda figured it might happen since President Nelson announced 200 temples in just 7 and a half years, which is more temples than all of the other presidents of the church combined.  As exciting as those are, that also meant that there's now a lot of temples that are still in the very early stages of planning, approval, or construction.  So the First Presidency decided to slow down on announcing new temples.
* All this being said, we got a bit of a surprise this Christmas: a temple in Portland, Maine.  I figured I'd better update this map anyway with temples that have had a site announced, have started construction, or have been dedicated.  I almost wonder if the church is going to spread out these temple announcements and not do them during General Conference exclusively, which will keep me on my toes for sure.
* I ran into a little bit of a funny blunder when updating my JSON files to reflect the new changes.  Under my predictions file, I removed Augusta Maine from my list since Portland is fairly close by, especially in terms of temples in New England.  Well, when trying to remove that, I noticed that it didn't work.  The prediction for Augusta was still up on my map, even after shutting down the live server and starting again.  It confused me for a minute until I realized I removed it from the CSV file, which was no longer being used, and not the JSON file.  Because of this, I finally decided to delete all the legacy files since they're not being used anymore anyway.
* This made me realize how much easier the new system using JSON is compared to the old one where I was using CSV files and a Python script to read them.  With the old system, I had to delete the entirety of both lists, update the CSV files, run the Python script, copy and paste everything, and go through and fix various errors due to things like punctuation.  It was pretty tedious to do all that, especially since that punctuation issue would often happen with cities on the Polynesian islands that would use apostraphes in their name, such as Nuku'alofa.  Another issue that I had from time to time is when for some reason, formatting on the CSV file would get a bit screwed up and accent marks for certain cities or temple names would turn into a string of unreadable characters that I had to go through and fix, and there were a lot of them.  In JSON, the characters would always stay the same, and if I needed to make a change, I only had to do it in the JSON file itself without ever touching the main HTML file.

# Future Goals

* Learn how to impliment a filter to only display certain points at a time.
* Add a key to display on the map explaining what the different colored dots mean.
* Work in a way to display more than one photo on popups.