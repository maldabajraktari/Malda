from bs4 import BeautifulSoup
html_content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Webpage</title>
</head>
<body>
    <h1>Welcome to My Simple Webpage</h1>
    <p class='intro'>This is a paragraph</p>
    <div id="content">
        <p>Check out these links:</p>
        <a href="https://example.com">Example 1</a>
        <a href="https://example2.com">Example 2</a>
        <a href="https://example3.com">Example 3</a>
    </div>
</body>
</html>
"""

soup=BeautifulSoup(html_content,'html.parser')
print("Title", soup.title.text)
div_content=soup.find("div", id="content")
links=div_content.find_all("a")
