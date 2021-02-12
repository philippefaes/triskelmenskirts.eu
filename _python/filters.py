import re

def dateformat(value, format="%d-%b-%Y"):
    return value.strftime(format)

filters = {}
filters['dateformat'] = dateformat


import datetime
filters = {}

try:
    import markdown
    def md(text):
        return markdown.markdown(text)
    filters['md'] = md
except ImportError:
    print ("Could not find module markdown. Continuing without markdown")


def license(licenseName):
    if licenseName == 'CC BY-ND 4.0':
        link = "http://creativecommons.org/licenses/by-nd/4.0/"
        return "the <a href='%s'>%s license</a>"%(link,licenseName)
    if licenseName == 'Sigasi Insights':
        return "the <a href='/LICENSE.html'>Sigasi Insights license</a>"
    else:
        raise "unknown license: " + licenseName
def today(unusedArgument):
    return str(datetime.date.today())
def dateformat(value, format="%Y-%m-%d"):
    return value.strftime(format).replace('-','&#8209;') #non-breaking hyphen

def coloredDot(title):
    return title.replace('.','<span style="color:#f47920">.</span>')


def author(name):
    return name
def cutoff(text,length=30):
    if '<' in text or '>' in text:
        text = re.sub('<[^<]+?>', '', text)
    if len(text) > length+3:
        return text[:length]+"..."
    else:
        return text
def recursecontent(items):
    contents = [item['content'] for item in items if 'content' in item]
    contents = sum(contents,[])
    if contents:
        children = recursecontent(contents)
        contents += children
    return contents
    
def filtercontent(sections,urls=["/tech/"]):
    return recursecontent (sections)

    # TODO: filter
    if type(urls)==str:
        urls=[urls]
#     print len(sections)
#     print type(sections[0])
#     print sections[0].keys()
    
    contents = [section['content'] for section in sections if section['url'] in urls]
    return sum(contents,[])

def filtertag(content,tag):
    return [item for item in content if tag in item.get('tags',[])]

def sortpopular(content):
    return content
    
def recurse(content):
    result = []
    for item in content:
        if 'content' in item:
            result += recurse(item["content"])
        else:
            result.append(item)
    return result
def filterlatest(content,count=10):
    content = [item for item in content if 'date' in item]
    c =  sorted(content,key=lambda c:c.get('date'),reverse=True)
    if len(c)>count:
        return c[:count]
    else:
        return c
    
def excludewithoutthumbnail(items):
    return [i for i in items if 'thumbnail'in i ]
    
def excludefuture(items, enabled):
    if not enabled:
        return items
    return [i for i in items if (not ('date' in i)) or i["date"]<=datetime.date.today()]

def filterfirst(content,count=10):
    if len(content)>count:
        return content[:count]
    else:
        return content
def split(items,i):
    return [items[:len(items)/2], items[len(items)/2:]] [i]
def wistia(videoid,video_width=600,video_height=400):
    return """
        <script src="//fast.wistia.com/embed/medias/j38ihh83m5.jsonp" async></script>
        <script src="//fast.wistia.com/assets/external/E-v1.js" async></script>
        <div class="wistia_embed wistia_async_{{videoid}}" style="height:{{video_height}}px;width:{{video_width}}px;margin: 0 auto;"></div>
        """.replace('{{video_width}}',str(video_width)).replace('{{video_height}}',str(video_height)).replace('{{videoid}}',str(videoid))
def youtube(videoid,video_width=600,video_height=400):
    return """
        <iframe src="https://www.youtube.com/embed/{{videoid}}?modestbranding=1&rel=0&showinfo=0" gesture="media" allow="encrypted-media" allowfullscreen="" width={{video_width}} height={{video_height}} frameborder="0" id={{videoid}}> 
        </iframe>
        """.replace('{{video_width}}',str(video_width)).replace('{{video_height}}',str(video_height)).replace('{{videoid}}',str(videoid))


filters['author'] = author
filters['cutoff'] = cutoff
filters['dateformat'] = dateformat
filters['filtercontent'] = filtercontent
filters['filterfirst'] = filterfirst
filters['filterlatest'] = filterlatest
filters['filtertag'] = filtertag
filters['recurse'] = recurse
filters['sortpopular'] = sortpopular
filters['split'] = split
filters['wistia'] = wistia
filters['youtube'] = youtube
filters['today'] = today
filters['license'] = license
filters['coloredDot'] = coloredDot
filters['excludefuture'] = excludefuture
filters['excludewithoutthumbnail'] = excludewithoutthumbnail
filters['recursecontent'] = recursecontent
