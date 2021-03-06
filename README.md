# COVID-19 Monitor

This app is a real-time tracker for global COVID-19 data using the public "covid19-api" (https://www.npmjs.com/package/covid19-api) package sourced from Worldometers and the Johns Hopkins Coronavirus Resource Center Dataset. It is designed to provide simple, at-a-glance information for a given country as well as a quick graphical view of relative case numbers across the globe. This document is designed to provide a simple introduction to the app's use and features as well as some basic troubleshooting and future plans. If you're looking for anything not addressed in this readme, feel free to shoot me an email at evan.carlstrom@gmail.com and I'll be happy to see what I can do.

## How To Run This App
The simplest way is to download the zipped version from (link here) and unpack it. The `main.exe` file is a standalone executable that will not require you to do anything else.

If you prefer a more manual method, you can download this repository and do one of two things:

- Run `/app/dist/main.exe` via terminal to access the same executable file.
- Install Python (https://www.python.org/downloads/), open up a terminal window, and run `python main.py` from the `/app` directory. Note that you will additionally need to install all required dependencies; a list of these is provided for convenience in `/app/setup.py`.

## Basic Features

The app provides data for four major categories:

- Confirmed cases, including total increases over the last 24 hours
- Confirmed deaths, including total increases over the last 24 hours
- Active cases, including cases in critical condition
- Recovered cases, expressed as a percentage of total cases

To look up this data for a particular country, enter the name in the search bar and hit enter or click the arrow button. Note that as of this writing (3/24/2021) some countries require an abbreviation to work properly, e.g. 'United States' should be entered as 'USA'. This will be addressed in a future update. Simple color coding is provided for convenience with negative statistics appearing in red and positive statistics in green.

The bottom of the app window also features a graph with bars representing the relative total case numbers for 35 countries across the globe. The aim in selecting these countries was to provide an even sampling of different geographic regions for an unbiased at-a-glance view of worldwide case statistics. The graph automatically renders when the app is opened and will not be impacted by search results.

## Troubleshooting

Here are a couple of issues that may arise. This section is limited for now but with more users will come more potential issues so it will be updated constantly. As mentioned in the first section, if these steps don't work or your issue is not listed here and you can't find a solution, send me an email so I can help.

- **The app closes immediately after opening**: This shouldn't happen with the standalone version but it can occur if there's something missing from the /dist directory. Since it's difficult to figure out what might be missing if the app closes immediately, try opening it via console instead; open a terminal window, navigate to the directory where you've unzipped the app, and type `main.exe` to run it. The console window will remain open even after the app closes and you'll see an error log in the console indicating while file(s) are missing. Everything you need is present in this repository and you should be able to download whatever you need for the app to work properly.

- **Most data field changes display 0**: This seems to be something that comes from the API and although I'm looking into it I'm not sure if there's anything I can do on my end to fix it. Towards the end of the day (in Eastern time so it may vary depending on where you are) the API data seems to refresh for a while and although the major field data will display correctly, any changes (such as increases in confirmed cases/deaths) will be listed as 0 during that time. This fixes itself once the data is completely refreshed.
