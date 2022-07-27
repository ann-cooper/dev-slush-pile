Title: Starting a blog
Author: AC
Date: 2022-07-17
Tags: pelican, tutorials
Slug: starting-a-blog
Summary: Setting up a Pelican blog

After thinking about starting a blog for a few years but not actually taking any steps toward it, I was inspired to finally give it a try by [this](https://testandcode.com/191) episode in one of my favorite podcasts. One of the things that they discuss is that there are many reasons to have a blog and many ways of blogging, which spoke to me because one of my major hesitations was that I don't have a very focused topic and I don't want to go after any particular audience. My intention for this blog is to be a spot where I can keep notes about things I want to remember, projects, and useful tips & tricks. 

I used the project setup and static file publishing steps from [this Pelican tutorial](https://justinnaldzin.github.io/create-a-website-using-github-pages-and-pelican.html). I didn't use the theme section or the Jupyter Notebook section because neither worked quite right for me (and I like the default theme). I didn't look into the theme support enough to know what else might need to be updated to work, but I did note that JINJA_EXTENSIONS should now be `JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}`. Also, I was able to skip adding any submodules to my repo by keeping the default theme and using a different approach to sharing notebooks.
    
For notebook support, [the pelican-jupyter package](https://pypi.org/project/pelican-jupyter/) was easy to setup. I'm using "markup mode", which involves adding a few lines to the `pelicanconf.py` file, and I'm using metadata files to describe the notebook instead of putting that information in a cell inside the notebook.  

Here we go!

Edit: 

The `pre-push.sh` didn't work how I thought it was meant to, so I changed it a little:
    - `pre-push.sh` to just `pre-push`
    - set as executable witn `chmod 766 .git/hooks/pre-push`