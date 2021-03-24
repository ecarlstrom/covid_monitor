# COVID-19 Monitor
This app is a real-time tracker for global COVID-19 data using the public "covid19-api" (https://www.npmjs.com/package/covid19-api) package sourced from Worldometers and the Johns Hopkins Coronavirus Resource Center Dataset. It is designed to provide simple, at-a-glance information for a given country as well as a quick graphical view of relative case numbers across the globe. This document is designed to provide a simple introduction to the app's use and features as well as some basic troubleshooting and future plans. If you're looking for anything not addressed in this readme, feel free to shoot me an email at evan.carlstrom@gmail.com and I'll be happy to see what I can do.

## How To Run This App
The simplest way is to download the zipped version from (link here) and unpack it. This is a standalone executable that will not require you to do anything else.

If you prefer a more manual method, you can download this repository and do one of two things:

- Run `/app/dist/main.exe` to access the same executable file.
- Install Python (https://www.python.org/downloads/), open up a terminal window, and run `python main.py` from the `/app` directory. Note that you will additionally need to install all required dependencies; a list of these is provided for convenience in `/app/setup.py`.

## Basic Features
