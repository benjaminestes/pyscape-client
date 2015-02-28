class EndpointsMixin:
    def get_anchor_text(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/anchor-text-metrics
        """
        
        # API breaks if scope isn't defined.
        if 'Scope' not in params.keys():
            params['Scope'] = 'phrase_to_page'
       
        return self.get('anchor-text', url, params=params)

    def get_links(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/link-metrics
        """
        
        # API breaks if scope isn't defined.
        if 'Scope' not in params.keys():
            params['Scope'] = 'page_to_page'
        
        return self.get('links', url, params)

    def get_url_metrics(self, url, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics
        """
        return self.get('url-metrics', url, params)

    def get_top_pages(self, url, smart_fields = False, **params):
        """
        
        Docs: http://moz.com/help/guides/moz-api/mozscape/api-reference/top-pages
        """
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