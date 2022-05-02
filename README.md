# NewSourceApp
An application that consumes the News - API and displays news sources and articles.

## ontribution
Ann Wangui

## Technology used
Python
Flask
HTML
CSS3

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser.

## Setup and Instruction
Clone the repository at here.
Extract and open the folder on VS code or navigate to the folder on your terminal.
On the terminal, create a virtual environment python3 -m venv virtual and activate it source virtual/bin/activate. NB virtual is the name of the environment.
Pip install dependancies highlighted on the requirements.txt by running pip install -r requirements.txt
Create a start.sh file in the root directory of the folder and define the api key. You can generate the api key from the News API here
Run chmod +x start.sh and ./start.sh respectively on the terminal.
View the application on your browser through http://127.0.0.1:5000.

## Behaviour Driven Development
BDD focuses on how the user will interact with the application.

What you will see and experience:

A landing page with a navbar, a Tech section, list of resources, What's new and a footer.
The navbar contains links with various types of news articles. Click on the Kenya link and get redirected to view Kenyan news articles.
The search form on the navbar allows the user to search for any article desired. Type in for example, shoes and submit. You will get redirected to a search page with the number of articles found related to shoes, article title, description and a link to the main article.
On the News Sources Available, click to be redirected to the sources main websites.
The news articles are displayed on cards, with a title and a brief description. Click on read article or view more to get redirected to the main article or video on the source website.
On the particular pages such as Kenya, a section of other articles are displayed, click on the titles to get redirected to the main articles.
On the footer, click on the social icons to interact with the owners of the website.

## Development
To fix a bug or enhance an existing module, follow these steps:

Fork the repo
Create a new branch (git checkout -b improve-feature)
Make the appropriate changes in the files
Add changes to reflect the changes made
Commit your changes (git commit -am 'Improve feature')
Push to the branch (git push origin improve-feature)
Create a Pull Request

## Known Bugs
There are no known bags

## Support and Contact DetailS
Feel free to call me or email me with respective contacts detail:

+254743715669
wanguia822@gmail.com

# License
MIT license copyright@ 2022 ann wangui
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



