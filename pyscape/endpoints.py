class EndpointsMixin:
        
    def get_anchor_text(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/anchor-text-metrics
        """
        
        # API breaks if scope isn't defined. This default is specified by the
        # documentation.
        if 'Scope' not in params.keys():
            params['Scope'] = 'phrase_to_page'
        
        self._add_smart_fields('anchor-text', params)
       
        return self.get('anchor-text', url, params=params)

    def get_links(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/link-metrics
        """
        
        # API breaks if scope isn't defined. This default is specified by the
        # documentation.
        if 'Scope' not in params.keys():
            params['Scope'] = 'page_to_page'
            
        self._add_smart_fields('links', params)
        
        return self.get('links', url, params)

    def get_url_metrics(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics
        """
        self._add_smart_fields('url-metrics', params)
        
        return self.get('url-metrics', url, params)
        
    def batch_url_metrics(self, urls, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics
        """
        self._add_smart_fields('url-metrics', params)
        
        return self.post('url-metrics', urls, params)

    def get_top_pages(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/top-pages
        """
        self._add_smart_fields('top-pages', params)
        
        return self.get('top-pages', url, params)
    
    def get_last_update(self):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/metadata
        """
        return self.get('metadata', 'last_update.json')
    
    def get_next_update(self):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/metadata
        """
        return self.get('metadata', 'next_update.json')
        
    def get_index_stats(self):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/metadata
        """
        return self.get('metadata', 'index_stats')