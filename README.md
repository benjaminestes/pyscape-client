# Pyscape 

[![Build Status](https://snap-ci.com/benjaminestes/pyscape-client/branch/master/build_image)](https://snap-ci.com/benjaminestes/pyscape-client/branch/master)

A script to grab data from the [Mozscape 
API](http://apiwiki.seomoz.org/). Requires Python &ge; 3.2. For 
more information please see the [pretty project 
page](http://projects.benjaminestes.com/Pyscape/).

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
