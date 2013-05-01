def get_bulk_metrics(pys, urls, args):
    """run a query for url metrics for many urls"""

    params = args[1:]
    data = []
    count = 0

    for url in urls:
        # Let it rest between calls...
        pys.sleep()
        count += 1
        pys.report('Grabbing metrics for URL [', count, ']')

        data.extend(pys.call_url_metrics(url, *params))

    return data
