from bs4 import BeautifulSoup

html_sample = ' \
<html> \
    <body> \
        <h1 id = "title"> Hello World </h1>\
            <a href = "#" class = "link"> This is link1 </a> \
            <a href = "# link2" class = "link"> This is link2 </a> \
    </body> \
<\html>'

soup = BeautifulSoup(html_sample, 'html.parser')
print soup.select('a')