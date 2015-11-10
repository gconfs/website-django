import re
import markdown

def markdown_to_html(md):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]'
            '|(?:%[0-9a-fA-F][0-9a-fA-F]))+', md)
    for url in urls:
        md = md.replace(url, '[' + url + '](' + url + ')')
    return markdown.markdown(md, extensions=['markdown.extensions.nl2br'])
