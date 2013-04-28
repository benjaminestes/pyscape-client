# Pyscape

A script to grab data from the [Mozscape 
API](http://apiwiki.seomoz.org/). Requires Python &ge; 3.2.

## Getting started

To use Pyscape you will need:

1. A Python installation &ge; 3.2.
2. A set of [Mozscape API 
   credentials](http://apiwiki.seomoz.org/create-and-manage-your-account), 
   free or paid. It's a phenomenal service they offer, so 
   I recommend you try it out if you aren't familiar.

Put your keys in a file called `keys.json` in the same directory 
as the script. The structure of this file should be:

```
{
    "access-id": "your-id-here",
    "secret-key": "your-key-here"
}
```

## Usage


```bash
usage: pyscape [-h] [-d | -s | -p] [-o | -m | -f | -t] [-j | -c]
               {metrics,bulk-metrics,anchor,top,links} source dest

Interface with the Mozscape API to provide link metrics

positional arguments:
  {metrics,bulk-metrics,anchor,top,links}
                        select operating mode
  source                specify a URL or text file as appropriate
  dest                  specify an output file

optional arguments:
  -h, --help            show this help message and exit
  -d, --domain-mode     interpret input URL(s) as domains only
  -s, --subdomain-mode  interpret input URL(s) as subdomains only
  -p, --page-mode       interpret input URL(s) as individual pages; default
  -o, --one-page        in link mode, return one page per linking domain
  -m, --many-pages      in link mode, return many pages per linking domain;
                        default
  -f, --phrase          in anchor mode, return phrase matches
  -t, --term            in anchor mode, return term matches; default
  -j, --json            write data in JSON format
  -c, --csv             write data in CSV format; default
```

### Examples

```bash
./pyscape links www.example.com links.csv -d -m
# export a CSV with all available links to example.com
```

## OSE-style reports

Often use of the Mozscape API is an extension of working with 
[Open Site Explorer](http://www.opensiteexplorer.org/). When then 
10,000 lines it provides are insufficient, we can use the command 
line to extend the amount of information available. Or, if we're 
just trying to pull a lot of reports it will be more convenient to 
use a command line tool.

## Thanks

The [SEOmoz team](http://www.seomoz.org/about/team) deserves a lot 
of credit for their work on creating a useful tool. If you're 
a dev looking for a great place to work, [check them 
out](http://www.seomoz.org/about/jobs). And tell them I sent you!

Also, preparing all of the data required to set up intelligent 
defaults and provide human-readable output would have been 
impossible without http://jsoneditoronline.com. It's bitchin'.
