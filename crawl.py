url = 'http://ryanstecher.net/'
def get_page(url):
    try:
        import urllib
        import urllib2
        return urllib2.urlopen(url).read()
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def store_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    words = content.split() 
    for word in words: 
        add_to_index(index,word,url)
    return index

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    if len(crawled) < 6:
        while tocrawl:
            print crawled
            page = tocrawl.pop()
            if page not in crawled:
                    content = get_page(page)
                    add_page_to_index(index,page,content)
                    union(tocrawl, store_all_links(get_page(page)))
                    crawled.append(page)
        return index