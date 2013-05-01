import json
from .flagindex import FlagIndex

class PresetHandler:
    
    def __init__(self, infile, flag_index):
        self.index = flag_index 
        self.load_data(infile) 
        pass

    def get_args(self):
        call = self.load_method()

        # Start with the method
        args = (call,)

        # Add the appropriate column values
        if call == 'anchor-text' or call == 'url-metrics' \
           or call == 'top-pages':
            args += (self.load_cols('c'),)
        elif call == 'links':
            args += ()
            for c in ['tc','sc','lc']:
                args += (self.load_cols(c),)

        # Now the scope
        if call == 'links' or call == 'anchor-text':
            args += (self.load_scope(),)

        # And finally the sort
        if call == 'links':
            args += (self.load_sort(),)

        return args

    def set_preset(self, label):
        self.preset_label = label

    def load_data(self, infile):
        self.presets = json.load(infile)

    def load_method(self):
        return self.presets[self.preset_label]['call']

    def load_cols(self, column_id):
        """Get the return fields the user's selection requires"""

        cols = 0

        for c in self.presets[self.preset_label][column_id]:
            # The bitflag.json generating script returns strings? 
            # Because the bitflag.json generator doesn't filter properly...
            cols = cols | self.index.bitflag(c)

        return cols

    def load_scope(self):
        """Find the scope for the API call user has selected."""
        return self.presets[self.preset_label]['scope']

    def load_sort(self):
        """Find an appropriate sort for the API call user has selected."""
        return self.presets[self.preset_label]['sort']
