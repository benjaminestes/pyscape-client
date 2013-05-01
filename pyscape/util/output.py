import csv

def to_json(outfile, data):
    "generate json output"

    outfile.write(str(data).replace('\'', '\"'))

def to_csv(outfile, ph, preset, data):
    "generate csv output"

    output = []
    headers = []
    keys = []
    col_types = ['c', 'tc', 'sc', 'lc']

    # Generate human-readable headers from our index
    for i in col_types:
        # Some col_types will always be missing,
        # so use try block.
        #
        # is there a better way to deal with this?
        try:    
            for j in ph.presets[preset][i]:
                keys.append(j)
                headers.append(ph.index.human_readable(j))
        except:
            pass

    output.append(headers)

    # Read appropriate columns from data
    for record in data:
        line = []
        for k in keys:
            line.append(record[k])
        output.append(line)

    writer = csv.writer(outfile, delimiter = ',',
                        quotechar = '"',
                        dialect = 'excel',
                        quoting = csv.QUOTE_ALL)
    writer.writerows(output)

def ose_style(outfile, data):

    output = []
    entry = []

    headers = ['URL',
               'Title',
               'Anchor Text', 
               'Page Authority',
               'Domain Authority',
               'Number of Linking Root Domains',
               'Followable',
               '301',
               'Origin',
               'Target URL']

    output.append(headers)

    for line in data:
        entry = ["http://" + line['uu'],
                 line['ut'],
                 line['lnt'],
                 str(round(line['upa'])),
                 str(round(line['pda'])),
                 str(line['uipl'])]
        
        # Check for nofollow
        # Reversed because field is 'Followable'
        if line['lf'] & 1:
            entry.append('No')
        else:
            entry.append('Yes')

        # Check link flag for 301 redirect
        if line['lf'] & 64:
            entry.append('Yes')
        else:
            entry.append('No')

        # Check for internal link
        if line['lf'] & 4096:
            entry.append('Internal')
        else:
            entry.append('External')

        # Add target page
        entry.append("http://" + line['luuu'])
        output.append(entry)
    
    writer = csv.writer(outfile, delimiter = ',',
                        quotechar = '"',
                        dialect = 'excel',
                        quoting = csv.QUOTE_ALL)
    writer.writerows(output)
