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
