# Musical Time Machine

an app that takes a user-selected date then uses this
date to scrape the Billboard Top 100 website for the songs
that were most popular on this day and then generate a Spotify
playlist.

## Technologies used

- Python
- JavaScript
- AJAX/JSON
- Flask
- Jinja
- Bootstrap
- SQL / SQL Alchemy
- BeautifulSoup
- Spotify API

(dependencies are listed in requirements.txt)

## Run the Musical Time Machine Flask app

This app has not yet been deployed, so here is how to run the app locally on your machine.

#### Create and activate a Python virtual enrivonment and install dependencies

```sh
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

#### Make sure you have PostgreSQL running

if you are on a windows machine you may need to clear any stale pid files using the following command:

```sh
sudo pg_ctlcluster 13 main start
```

#### Load the shell script and run the file

```sh
source secrets.sh
python3 server.py
```

Verify the deployment by navigating to your server address in your preferred browser

```sh
localhost:5000
```

## License

[CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/): This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator.
![CC](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.png)

## Author

Tavish Bell is a software engineer that lives in Bellingham, WA
