DEFAULTS = {
    "url-metrics": {
        None: {
            "Endpoint": "url-metrics",
            "Description": "URL metrics on a domain level",
            "Fields": {
                "Cols": [
                    "ut",
                    "uu",
                    "upl",
                    "ueid",
                    "peid",
                    "uipl",
                    "pid",
                    "pmrp",
                    "ptrp",
                    "us",
                    "upa",
                    "pda"
                ]
            }
        }
    },
    "top-pages": {
        None: {
            "Endpoint": "top-pages",
            "Description": "Top pages report defaults",
            "Fields": {
                "Cols": [
                    "ut",
                    "uu",
                    "ueid",
                    "uipl",
                    "uid",
                    "us",
                    "upa"
                ],
            }
        }
    },
    "anchor-text": {
        "phrase_to_domain": {
            "Endpoint": "anchor-text",
            "Description": "Anchor text report, phrase to domain",
            "Scope": "phrase_to_domain",
            "Fields": {
                "Cols": [
                    "appt",
                    "appeu",
                    "appep"
                ]
            }
        },
        "phrase_to_subdomain": {
            "Endpoint": "anchor-text",
            "Description": "Anchor text report, phrase to subdomain",
            "Scope": "phrase_to_subdomain",
            "Fields": {
                "Cols": [
                    "apft",
                    "apfiu",
                    "apfeu",
                    "apfep"
                ]
            }
        },
        "phrase_to_page": {
            "Endpoint": "anchor-text",
            "Description": "Anchor text report, phrase to page",
            "Scope": "phrase_to_page",
            "Fields": {
                "Cols": [
                    "aput",
                    "apuiu",
                    "apueu",
                    "apuep"
                ]
            }
        },
        "term_to_domain": {
            "Endpoint": "anchor-text",
            "Description": "Anchor text report, term to domain",
            "Scope": "term_to_domain",
            "Fields": {
                "Cols": [
                    "atpt",
                    "atpeu",
                    "atpep"
                ]
            }
        },
        "term_to_subdomain": {
            "Endpoint": "anchor-text",
            "Description": "Anchor text report, term to subdomain",
            "Scope": "term_to_subdomain",
            "Fields": {
                "Cols": [
                    "atft",
                    "atfiu",
                    "atfeu",
                    "atfep"
                ]
            }
        },
        "term_to_page": {
            "Endpoint": "anchor-text",
            "Description": "Anchor text report, term to page",
            "Scope": "term_to_page",
            "Fields": {
                "Cols": [
                    "atut",
                    "atuiu",
                    "atueu",
                    "atuep"
                ]
            }
        },
    },
    "links": {
        "domain_to_domain": {
            "Endpoint": "links",
            "Description": "Incoming links to specified domain, one per linking domain",
            "Scope": "domain_to_domain",
            "Sort": "domain_authority",
            "Fields": {
                "TargetCols": [
                    "luuu",
                    "luupl"
                ],
                "SourceCols": [
                    "uu",
                    "upl",
                    "uipl",
                    "pid",
                    "us",
                    "upa",
                    "pda"
                ],
                "LinkCols": [
                    "lnt"
                ]
            }
        },
        "domain_to_subdomain": {
            "Endpoint": "links",
            "Description": "Incoming links to specified subdomain, one per linking domain",
            "Scope": "domain_to_subdomain",
            "Sort": "domain_authority",
            "Fields": {
                "TargetCols": [
                    "luuu",
                    "luufq"
                ],
                "SourceCols": [
                    "uu",
                    "upl",
                    "uipl",
                    "pid",
                    "us",
                    "upa",
                    "pda"
                ],
                "LinkCols": [
                    "lnt"
                ]
            }
        },
        "domain_to_page": {
            "Endpoint": "links",
            "Description": "Incoming links to specified page, one per linking domain",
            "Scope": "domain_to_page",
            "Sort": "domain_authority",
            "Fields": {
                "TargetCols": [
                    "luuu"
                ],
                "SourceCols": [
                    "uu",
                    "upl",
                    "uipl",
                    "pid",
                    "us",
                    "upa",
                    "pda"
                ],
                "LinkCols": [
                    "lnt"
                ]
            }
        },
        "page_to_domain": {
            "Endpoint": "links",
            "Description": "Incoming links from pages to specified domain",
            "Scope": "page_to_domain",
            "Sort": "page_authority",
            "Fields": {
                "TargetCols": [
                    "luuu",
                    "luupl"
                ],
                "SourceCols": [
                    "uu",
                    "upl",
                    "uipl",
                    "pid",
                    "us",
                    "upa",
                    "pda"
                ],
                "LinkCols": [
                    "lnt"
                ]
            }
        },
        "page_to_subdomain": {
            "Endpoint": "links",
            "Description": "Incoming links from pages to specified subdomain",
            "Scope": "page_to_subdomain",
            "Sort": "page_authority",
            "Fields": {
                "TargetCols": [
                    "luuu",
                    "luufq"
                ],
                "SourceCols": [
                    "uu",
                    "upl",
                    "uipl",
                    "pid",
                    "us",
                    "upa",
                    "pda"
                ],
                "LinkCols": [
                    "lnt"
                ]
            }
        },
        "page_to_page": {
            "Endpoint": "links",
            "Description": "Incoming links from pages to specified page",
            "Scope": "page_to_page",
            "Sort": "page_authority",
            "Fields": {
                "TargetCols": [
                    "luuu"
                ],
                "SourceCols": [
                    "uu",
                    "upl",
                    "uipl",
                    "pid",
                    "us",
                    "upa",
                    "pda"
                ],
                "LinkCols": [
                    "lnt"
                ]
            }
        }
    }
}
