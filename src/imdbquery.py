import re

class ImdbQuery(str):
    def exclude_terms(self, terms_to_exclude):
        r = self
        for term in terms_to_exclude: r = r.replace(term, ' ')
        return ImdbQuery(r.lstrip().rstrip())
    
    def remove_non_alaphnumeric_chars(self):
        terms = re.compile(r'[^a-zA-Z0-9]+').split(self)
        r = ''
        for t in terms:  
            if t != '': r += ' ' + t
        return ImdbQuery(r).lstrip()
    
    def lower(self):
        return ImdbQuery(super(ImdbQuery, self).lower())
    
    def lstrip(self):
        return ImdbQuery(super(ImdbQuery, self).lstrip())
    
    def rstrip(self):
        return ImdbQuery(super(ImdbQuery, self).rstrip())