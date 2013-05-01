# Pyscape

A script to grab data from the [Mozscape 
API](http://apiwiki.seomoz.org/). Requires Python &ge; 3.2.

## Disclaimer

_I am not representing SEOmoz through my development of this tool; it
is completely independent. Neither SEOmoz nor me should be held accountable
if this doesn't work as expected._

That said, I hope you find this useful!

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
    "secret-key": "your-key-here",
    "level": "access-level"
}
```

...where `access-level` is one of `free`, `pro`, or `full` 
depending on the [level of rate 
limiting](http://apiwiki.seomoz.org/rate-limiting) you need.

## Usage


```
usage: pyscape.py [-h] [-d | -s | -p] [-o | -m | -f | -t] [-j | -c]
                  {metrics,bulk-metrics,anchor,top,links,ose-style} source
                  dest

Interface with the Mozscape API to provide link metrics

positional arguments:
  {metrics,bulk-metrics,anchor,top,links,ose-style}
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

Notes:

1. URLs must not be preceded by http:// or https://. Currently there is no built in filtering for this.
2. On Windows you'll probably have to prepend "python" or "python3" to all of the following calls.

```
pyscape.py links www.example.com links.csv -d -m
# export a CSV with all available links to example.com

pyscape.py ose-style www.example.com report.csv -d -o
# export a CSV matching OSE's format with all domains
# linking to the target domain

pyscape.py bulk-metrics urls.txt output.csv -p
# export page level metrics for a list of urls

pyscape.py bulk-metrics urls.txt output.csv -d
# export domain level metrics for a list of urls

pyscape.py anchor www.example.com anchor.csv -d -f
# export CSV with anchor text phrases pointed at all
# pages on www.example.com
```

## OSE-style reports

Often use of the Mozscape API is an extension of working with 
[Open Site Explorer](http://www.opensiteexplorer.org/). When then 
10,000 lines it provides are insufficient, we can use the command 
line to extend the amount of information available. Or, if we're 
just trying to pull a lot of reports it will be more convenient to 
use a command line tool. Use the `ose-style` command to generate
reports that match the formatting you would get from OSE.

## Thanks

The [SEOmoz team](http://www.seomoz.org/about/team) deserves a lot 
of credit for their work on creating a useful tool. If you're 
a dev looking for a great place to work, [check them 
out](http://www.seomoz.org/about/jobs). And tell them I sent you!

Also, preparing all of the data required to set up intelligent 
defaults and provide human-readable output would have been 
impossible without http://jsoneditoronline.com. It's bitchin'.
