MUSICAL TIME MACHINE

# --- THE PREMISE -----
an app that takes in a date input by user and then uses this 
date to scrape the Billboard Top 100 website for the songs 
that were most popular on this day and then generate a Spotify 
playlist. 

# --- HOW TO RUN THE PROGRAM -----
I am on a windows machine and for whatever reason I typically always
 need to clear the stale pid file before my program will run. 
 This command for this is:
>
> sudo pg_ctlcluster 13 main start
>
From there, I create a virtual environment using the following commands:
> virtualenv env
> source env/bin/activate
>
then load the shell script and run the file:
>
> source secrets.sh
> python3 server.py
>
Next, I navigate to the browser where the page has loaded and create 
an account and/or login. Currently there is no verification on
any of the input fields so the login can be anything. 
Once logged in, a user can see the form. 
The dates on this form match the dates that are available for scraping 
via the Billboard 100 website. 