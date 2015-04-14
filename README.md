# Pyscape 

[![Build Status](https://snap-ci.com/benjaminestes/pyscape-client/branch/master/build_image)](https://snap-ci.com/benjaminestes/pyscape-client/branch/master)

A script to grab data from the [Mozscape 
API](http://apiwiki.seomoz.org/). Requires Python &ge; 3.2.

## Overview

Pyscape is an open-source Python library for accessing the Moz API. The latest version is a complete rewrite focusing on improving the functionality of Pyscape as a library. You'll get the most out of this tool by getting paid credentials for the Moz API, but it will work with free credentials as well.

(Mostly new) features:
- **Easy installation.** Library can now be installed using `pip install pyscape-client`.
- **Intelligent defaults.** Some of the API endpoints break if you don't include parts of the query. Pyscape includes everything necessary to keep the endpoints from breaking, and requests reasonably useful default columns from the API if none are specified.
- **Better authentication.**
- **True batch URL metrics requests.** Faster / fewer requests / happiness.
- **Uses Requests library.** This means that Pyscape returns response objects that have many useful methods. Check the headers of responses to see how many rows were returned, response codes to check whether the request was successful, and more.

## Using the command line tool

In order to use this tool you'll need to create a file called `keys.json` in the project folder. The content of the file should be your Moz API access id and secret key. The format of the file should be as follows:

```
{
    "access_id": "xxxxxx-xxxxxxxxxx",
    "secret_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

Once you've done that, invocation of the pyscape-cli.py is as follows:

```
python pyscape-cli.py [input.txt] [output.csv]
```

...where input.txt is a text file with a list of URLs, one per line.

## Using the library in your project

To use the library, install it with pip:

```
pip install pyscape-client
```

The library is only tested with Python 3.4. I make no guarantees that it will work with earlier versions.
