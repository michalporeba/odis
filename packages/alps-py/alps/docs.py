from curses.ascii import HT
from diogi.functions import *

class Doc:
    #href, format, tag
    def __init__(self, href: str=None, format: str=None, tag: str=None, value: str=None):
         self.href = href 
         self.format = format
         self.tag = tag 
         self.value = value 

    def as_data(self):
        data = {}
        set_if_not_none(data, self.href, 'href')
        set_if_not_none(data, self.format, 'format')
        set_if_not_none(data, self.tag, 'tag')
        set_if_not_none(data, self.value, 'value')
        return data 

    def parse(obj: dict):
        if str == type(obj):
            return TextDoc(obj)

        if dict == type(obj):
            value = get_if_exists(obj, 'value', None)
            format = get_if_exists(obj, 'format', 'text')
            href = get_if_exists(obj, 'href', None)

            if format == 'markdown':
                return MarkDownDoc(default_if_none(value, ''))
            if format == 'html':
                return HtmlDoc(
                    href = href,
                    value = default_if_none(value, '')
                )
                
            return TextDoc(default_if_none(value, str(obj)))

        return TextDoc()

class WithDocsMixin:
    def __init__(self, *args, **kwargs):
        super(WithDocsMixin, self).__init__(*args, **kwargs)
    
    def add_doc(self, doc: Doc):
        append_if_not_none(self.contents, doc, 'doc')
        return self


class HtmlDoc(Doc):
    def __init__(self, href: str, value: str):
        super(HtmlDoc, self).__init__(
            href = href,
            format = 'html',
            value = value
        )


class MarkDownDoc(Doc):
    def __init__(self, value: str):
        super(MarkDownDoc, self).__init__(
            format = 'markdown',
            value = value 
        )


class TextDoc(Doc):
    def __init__(self, value: str=''):
        super(TextDoc, self).__init__(
            format = 'text',
            value=value
        )