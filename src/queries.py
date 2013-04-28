from src.pyscape import Pyscape

def a_query(pys, url, cols, scope = Pyscape.A_PTP):
    return pys.anchor_text(url, cols, scope)

def l_query(pys, url, t, s, l, scope, sort):
    data = []

    # API documentation says 50 links per request is optimal
    offset = 0
    step = 50
    
    # Limited to 100,000 links total
    for i in range(int(100000 / step)):
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
    data = []
        
    # API documentation says that 50 links per
    # request is optimal
    offset = 0
    step = 50

    # Limited to 10,000 URLs
    for i in range(int(10000 / step)):
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
    return pys.url_metrics(url, cols)
    
def bulk_metrics(pys, urls, cols):
    data = []
    for url in urls:
        data.extend(pys.url_metrics(url, cols))

    return data
