class EndpointsMixin:
        
    def get_anchor_text(self, url, **params):
        """Return anchor text from links pointed at a URL.
        
        :param Scope: specify results per page / per domain.
        :param Filter: limit types of rows returned.
        :param Limit: limit number of rows returned.
        :param Offset: specify starting row.
        :param Cols: bitfield specifying which columns to return.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/anchor-text-metrics
        """
        
        # API breaks if scope isn't defined. This default is specified by the
        # documentation.
        if 'Scope' not in params.keys():
            params['Scope'] = 'phrase_to_page'
        
        self._add_smart_fields('anchor-text', params)
       
        return self.get('anchor-text', url, params=params)

    def get_links(self, url, **params):
        """Return anchor text from links pointed at a URL.
        
        :param Scope: specify results per page / per domain.
        :param Filter: limit types of rows returned.
        :param Limit: limit number of rows returned.
        :param Sort: order rows returned.
        :param Offset: specify starting row.
        :param SourceCols: bitfield specifying which columns to return.
        :param TargetCols: bitfield specifying which columns to return.
        :param LinkCols: bitfield specifying which columns to return.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/link-metrics
        """
        
        # API breaks if scope isn't defined. This default is specified by the
        # documentation.
        if 'Scope' not in params.keys():
            params['Scope'] = 'page_to_page'
            
        self._add_smart_fields('links', params)
        
        return self.get('links', url, params)

    def get_url_metrics(self, url, **params):
        """Return metrics about a single URL.
        
        :param Cols: bitfield specifying which columns to return.

        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics
        """
        self._add_smart_fields('url-metrics', params)
        
        return self.get('url-metrics', url, params)
        
    def batch_url_metrics(self, urls, **params):
        """As 'get_url_metrics' above. Uses a POST request to get
        multiple urls at once, passed as a list.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics
        """
        self._add_smart_fields('url-metrics', params)
        
        return self.post('url-metrics', urls, params)

    def get_top_pages(self, url, **params):
        """Get information about the top URLs on a domain.
        
        :param Filter: limit types of rows returned.
        :param Limit: limit number of rows returned.
        :param Sort: order rows returned.
        :param Offset: specify starting row.
        :param Cols: bitfield specifying which columns to return.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/top-pages
        """
        self._add_smart_fields('top-pages', params)
        
        return self.get('top-pages', url, params)
    
    def get_last_update(self):
        """Return date of last index update.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/metadata
        """
        return self.get('metadata', 'last_update.json')
    
    def get_next_update(self):
        """Return date of next index update.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/metadata
        """
        return self.get('metadata', 'next_update.json')
        
    def get_index_stats(self):
        """Return stats about current index.
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/metadata
        """
        return self.get('metadata', 'index_stats')