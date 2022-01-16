from diogi.functions import *


class Doc:
    # href, format, tag
    def __init__(
        self, href: str = None, format: str = None, tag: str = None, value: str = None
    ):
        self.href = href
        self.format = format
        self.tag = tag
        self.value = value

    def as_data(self):
        data = {}
        set_if_not_none(data, self.href, "href")
        set_if_not_none(data, self.format, "format")
        set_if_not_none(data, self.tag, "tag")
        set_if_not_none(data, self.value, "value")
        return data

    @staticmethod
    def parse(obj: any):
        if str == type(obj):
            return TextDoc(obj)

        if dict == type(obj):
            value = get_if_exists(obj, "value", None)
            format = get_if_exists(obj, "format", "text")
            href = get_if_exists(obj, "href", None)
            tag = get_if_exists(obj, "tag", None)

            if format == "markdown":
                return MarkDownDoc(value=default_if_none(value, ""), href=href, tag=tag)
            if format == "html":
                return HtmlDoc(href=href, tag=tag, value=default_if_none(value, ""))

            return TextDoc(value=default_if_none(value, str(obj)), href=href, tag=tag)

        return TextDoc()

    def __eq__(self, other):
        if type(other) is type(self):
            return (
                self.format == other.format
                and self.href == other.href
                and self.tag == other.tag
                and self.value == other.value
            )
        else:
            return False

    def __hash__(self):
        return hash((self.format, self.href, self.tag, self.value))


class WithDocsMixin:
    def __init__(self, *args, **kwargs):
        super(WithDocsMixin, self).__init__(*args, **kwargs)

    def add_doc(self, doc: any):
        if not isinstance(doc, Doc):
            doc = Doc.parse(doc)
        append_if_not_none(self.contents, doc, "doc")
        return self

    @property
    def docs(self):
        return always_a_list(get_if_exists(self.contents, "doc", []))


class HtmlDoc(Doc):
    def __init__(self, href: str, value: str, *args, **kwargs):
        super(HtmlDoc, self).__init__(
            href=href, format="html", value=value, *args, **kwargs
        )


class MarkDownDoc(Doc):
    def __init__(self, value: str, *args, **kwargs):
        super(MarkDownDoc, self).__init__(
            format="markdown", value=value, *args, **kwargs
        )


class TextDoc(Doc):
    def __init__(self, value: str = "", *args, **kwargs):
        super(TextDoc, self).__init__(format="text", value=value, *args, **kwargs)
