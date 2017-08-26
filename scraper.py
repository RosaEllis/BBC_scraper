###############################################################################
# START HERE: Tutorial 2: Basic scraping and saving to the data store.
# Follow the actions listed in BLOCK CAPITALS below.
###############################################################################

import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
print "Click on the ...more link to see the whole page"
# print html

# -----------------------------------------------------------------------------
# 1. Parse the raw HTML to get the interesting bits - the part inside <td> tags.
# -- UNCOMMENT THE 6 LINES BELOW (i.e. delete the # at the start of the lines)
# -- CLICK THE 'RUN' BUTTON BELOW
# Check the 'Console' tab again, and you'll see how we're extracting 
# the HTML that was inside <td></td> tags.
# We use lxml, which is a Python library especially for parsing html.
# -----------------------------------------------------------------------------
# below is importing a library called lxml.html  
import lxml.html

# below makes a variable called root that is using the function called fromstring (from the lxml.html library)... 
# it uses the html variable created above and it into an lxml object, which means we can use lxml functions on it 
 
root = lxml.html.fromstring(html)
# so 'root' now holds the results of the fromstring function being on the html we've scraped 

# below is using the function cssselece with the root variable just created (which is the html we've just scraped turned... 
# ...into an lxml object, and it gives it the variable name tds. 
# this will grab all the td tags from the html, a td tag is for a cell in an html table 
tds = root.cssselect('td') 

# below is a for loop, that says for all the td(s) in tds, print the full html tag and print just the text 
for td in tds:
    print lxml.html.tostring(td) # the full HTML tag
    print td.text                # just the text inside the HTML tag

# -----------------------------------------------------------------------------
# 2. Save the data in the ScraperWiki datastore.
# -- UNCOMMENT THE THREE LINES BELOW
# -- CLICK THE 'RUN' BUTTON BELOW
# Check the 'Data' tab - here you'll see the data saved in the ScraperWiki store. 
# -----------------------------------------------------------------------------

# below is a for loop, inside the for loop is a dictionary. 
# a dictionary stores pairs of information, which (I think) are the a column header and the...
#... info that goes in the column. So for record = { "td" : td.text } "td" is the column header and td.txt givens the values to go in the colum 

for td in tds:
     record = { "td" : td.text } # column name and value
     scraperwiki.sqlite.save(["td"], record) # save the records one by one
    
# -----------------------------------------------------------------------------
# Go back to the Tutorials page and continue to Tutorial 3 to learn about 
# more complex scraping methods.
# -----------------------------------------------------------------------------
