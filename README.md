# smeerws-web

Install Pelican 3.7.1 on Ubuntu 16.04 LTS

Windows: 
+ Install python (Download from Website https://www.python.org/downloads/, install python !enable add to Path!)
+ Clone pelican themes with https: 
```
git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
```

Follow the instructions on http://docs.getpelican.com/en/stable/install.html

1) install pip
2) install virtualenv https://virtualenv.pypa.io/en/stable/installation/
3) install pelican
4) install Markdown
5) install typogrify


Links: 
On http://chdoig.github.io/create-pelican-blog.html you will find a nice description how to install a Pelican blog. 

Themes for Pelican can be found at http://pelicanthemes.com/

Documentations Pelican:  http://docs.getpelican.com/en/stable/


Open a new terminal session and create a new virtual environment:
	
virtualenv ~/virtualenvs/pelican
cd ~/virtualenvs/pelican
source bin/activate

If it works your promt starts with (Pelican) ... : 

update your content with: pelican content -s pelicanconf.py --ignore-cache


