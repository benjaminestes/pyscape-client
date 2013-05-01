import argparse

def build_parser():
    parser = argparse.ArgumentParser(description = 'Interface with the Mozscape API to provide link metrics')
    
    input_mode = parser.add_mutually_exclusive_group()
    scope_mode = parser.add_mutually_exclusive_group()
    output_mode = parser.add_mutually_exclusive_group()

    command_opts = ['metrics',
                    'bulk-metrics',
                    'anchor',
                    'top',
                    'links']

    parser.add_argument('command', 
                        choices = command_opts,
                        help = 'select operating mode')

    parser.add_argument('source', 
                        help = 'specify a URL or text file as appropriate')

    parser.add_argument('dest', 

                        help = 'specify an output file')
    
    # Mutually exclusive flags for URL input mode
    input_mode.add_argument('-d', '--domain-mode',
                            action = 'store_true',
                            help = 'interpret input URL(s) as domains only')
    
    input_mode.add_argument('-s', '--subdomain-mode',
                            action = 'store_true',
                            help = 'interpret input URL(s) as subdomains only')

    input_mode.add_argument('-p', '--page-mode',
                            action = 'store_true',
                            default = True,
                            help = 'interpret input URL(s) as individual pages; default')

    # Mutually exclusive flags for scope in link/anchor modes
    scope_mode.add_argument('-o', '--one-page',
                            action = 'store_true',
                            help = 'in link mode, return one page per linking domain')
    
    scope_mode.add_argument('-m', '--many-pages',
                            action = 'store_true',
                            default = True,
                            help = 'in link mode, return many pages per linking domain; default')

    scope_mode.add_argument('-f', '--phrase',
                            action = 'store_true',
                            help = 'in anchor mode, return phrase matches')
    
    scope_mode.add_argument('-t', '--term',
                            action = 'store_true',
                            default = True,
                            help = 'in anchor mode, return term matches; default')
 
    # Mutually exclusive flags for output format
    output_mode.add_argument('-j', '--json',
                            action = 'store_true',
                            help = 'write data in JSON format')
    
    output_mode.add_argument('-c', '--csv',
                            action = 'store_true',
                            default = True,
                            help = 'write data in CSV format; default')
   
    return parser

def get_preset(args):
    """Determine the label of the preset the user wants."""

    if args.command == 'metrics' or args.command == 'bulk-metrics':
        if args.domain_mode:
            preset = 'u_d'
        elif args.subdomain_mode:
            preset = 'u_s'
        elif args.page_mode:
            preset = 'u_p'

    elif args.command == 'top':
        preset = 't'

    elif args.command == 'bulk-metrics':
        if args.domain_mode:
            preset = 'u_d'
        elif args.subdomain_mode:
            preset = 'u_s'
        elif args.page_mode:
            preset = 'u_p'

    elif args.command == 'links':
        preset = 'l_'

        if args.one_page:
            preset += 'dt'
        elif args.many_pages:
            preset += 'pt'

        if args.domain_mode:
            preset += 'd'
        elif args.subdomain_mode:
            preset += 's'
        elif args.page_mode:
            preset += 'p'

    elif args.command == 'anchor':
        preset = 'a_'

        if args.phrase:
            preset += 'pt'
        elif args.term:
            preset += 'tt'
        
        if args.domain_mode:
            preset += 'd'
        elif args.subdomain_mode:
            preset += 's'
        elif args.page_mode:
            preset += 'p'

    return preset
