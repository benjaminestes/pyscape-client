import time
from src.pyscape import Pyscape

def a_query(pys, url, cols, scope = Pyscape.A_PTP):
    "run a query for anchor text"
    
    # anchor text query requires only one call
    return pys.anchor_text(url, cols, scope)

def l_query(pys, url, t, s, l, scope, sort):
    "run a query for links"

    data = []

    # API documentation says 50 links per request is optimal
    offset = 0
    step = 50
    
    # Limited to 100,000 links total
    for i in range(int(100000 / step)):
        time.sleep(.2)
        print('Grabbing URLs [', offset, ']', sep = '')
        call_data = pys.links(url, t, s, l, scope, sort, offset, step)
        if call_data:
            # If data was received...
            data.extend(call_data)
        else:
            # If call() failed to return data, stop collecting
            break   
        offset = offset + step

    return data
    
def t_query(pys, url, cols):
    "run a query for top pages"

    data = []
        
    # API documentation says that 50 links per
    # request is optimal
    offset = 0
    step = 50

    # Limited to 10,000 URLs
    for i in range(int(10000 / step)):
        time.sleep(.2)
        # Give user feedback
        print('Grabbing URLs [', offset, ']', sep = '')
        call_data = pys.top_pages(url, cols, offset, step)
        if call_data:
            # If data was received...
            data.extend(call_data)
        else:
            # If call() failed to return data, stop collecting
            break   
        offset = offset + step

    return data

def u_query(pys, url, cols):
    "run a query for url metrics"

    return pys.url_metrics(url, cols)
    
def bulk_metrics(pys, urls, cols):
    "run a query for url metrics for many urls"

    data = []
    count = 0
    for url in urls:
        time.sleep(.2)
        count += 1
        print('Grabbing metrics for URL [', count, ']', sep = '')
        data.extend(pys.url_metrics(url, cols))

    return data
