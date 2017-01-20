import sys
from datetime import datetime

TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category:
:slug: {slug}
:summary:
:status: draft

"""



def new_post(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    post_name = str(title).lower().strip().replace(' ', '_')
    content_rst = 'content/' + post_name + '.rst'
    print 'content_rst = ', content_rst
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(content_rst, 'w') as w:
        w.write(t)
    print "New file in -> ", content_rst



if __name__ == '__main__':
    if len(sys.argv) > 1:
        new_post(sys.argv[1])
    else:
        print "No title given."
