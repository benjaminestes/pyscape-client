import json

class FlagIndex:

    def __init__(self, infile):
        self.index = self.load_index(infile)

    def load_index(self, infile):
        """Load an index of bitflag information from infile."""

        return json.load(infile)

    def human_readable(self, label):
        """Get a human readable description from a bitflag label."""

        return self.index[label]['human']

    def bitflag(self, label):
        """Return bitflag value for given label."""

        return int(self.index[label]['flag'])

    def to_headers(self, labels):
        
        headers = []

        for label in labels:
            headers.append(self.human_readable(label))

        return headers
