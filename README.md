# MoodMap

## Plotting sentiment analysed tweets to show the mood of the country

[visit the site](http://themoodmap.co.uk/)

MoodMap is an online application which correlates data from Twitter with data 
from the government. Tweets are put through sentiment analysis (to assess the 
overall mood) and then plotted on a map according to the location from which 
they were tweeted from. Goverment data for deprivation is then overlayed on 
top of this.

## Authors

 - Priyesh Patel
 - Daniel Saul

## Setting up

### Dependencies

All dependencies are listed in `requirements.txt`. Inside your VirtualEnv
execute:

```
pip install -r requirements.txt
```

### Installation

It is recommended to run the MoodMap daemon with Supervisor. To do this setup
Foreman by copying `env.example` to `.env` and filling out the details. Foreman
can then be used to export a Supervisor configuration file:

```
foreman export supervisor ./
```

This resulting file will need to be edited so that `/bin/sh venv_run.sh` is run
as the command and then added to the system's Supervisor directory (often
`/etc/supervisor/conf.d/`).

Supervisor can then be reloaded with `sudo supervisorctl reload`.

The web root should be set to `./web`.

## License

To be confirmed
