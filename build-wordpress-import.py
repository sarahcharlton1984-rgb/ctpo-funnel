import re, html, datetime, os

PAGES = [
    ("accountant-cost-limited-company.html","How much should an accountant cost for a limited company?","accountant-cost-limited-company","post", "What limited company directors actually pay for accountancy, what should be included, and the extras that turn a quote into a bigger bill."),
    ("changing-accountants.html",         "How to change accountants, and why it is easier than you think", "changing-accountants", "post", "What actually happens when you switch accountants: professional clearance, records, timing, and whether you have to tell them yourself."),
    ("salary-vs-dividends.html",          "Salary vs dividends in 2026/27: how the split actually works",   "salary-vs-dividends",  "post", "Why a low salary plus dividends still beats an all salary route in 2026/27, and the point at which the advantage runs out."),
    ("how-much-to-pay-yourself.html",     "How much should I pay myself as a company director?",            "how-much-to-pay-yourself","post", "The question to answer before the salary and dividend split: how much do you actually need to take out?"),
]

SCOPE = ".t4p-doc"

def scope_css(css):
    """Prefix every rule selector with SCOPE so it cannot leak into the theme."""
    out, i = [], 0
    # strip comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    def scope_sel(sel):
        parts = []
        for s in sel.split(','):
            s = s.strip()
            if not s:
                continue
            if s in ('*', 'html', 'body', ':root'):
                parts.append(SCOPE)
            elif s.startswith('*'):
                parts.append(SCOPE + ' ' + s)
            else:
                parts.append(SCOPE + ' ' + s)
        return ', '.join(parts)
    # walk top level blocks, handling @media wrappers
    depth, buf, cur_at = 0, '', None
    tokens = re.split(r'([{}])', css)
    stack = []
    result = []
    pending = ''
    for tok in tokens:
        if tok == '{':
            sel = pending.strip(); pending = ''
            if sel.startswith('@'):
                result.append(sel + '{'); stack.append('at')
            else:
                result.append(scope_sel(sel) + '{'); stack.append('rule')
        elif tok == '}':
            result.append('}')
            if stack: stack.pop()
        else:
            if stack and stack[-1] == 'rule':
                result.append(tok)   # declarations
            else:
                pending += tok
    return ''.join(result)

items = []
pid = 900
now = datetime.datetime(2026, 8, 31, 7, 0, 0)

for fname, title, slug, ptype, excerpt in PAGES:
    src = open(fname, encoding='utf-8').read()
    css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', src, re.S))
    body = re.search(r'<div class="wrap">(.*?)</div>\s*</body>', src, re.S)
    inner = body.group(1) if body else ''
    # the site header carries the brand already: drop the page wordmark + rule
    inner = re.sub(r'<p class="wordmark">.*?</p>\s*<hr class="rule">', '', inner, flags=re.S)
    # h1 becomes the WordPress post title
    inner = re.sub(r'<h1>.*?</h1>', '', inner, count=1, flags=re.S)
    # Rewrite internal links for their new home.
    # Pages that move to tax4pros.co.uk stay relative; the calculators live on
    # apply.ctprivateoffice.com, so those must become absolute or they 404.
    ON_WP = {'accountant-cost-limited-company','changing-accountants',
             'salary-vs-dividends','how-much-to-pay-yourself'}
    def fix(m):
        href = m.group(1)
        path, _, qs = href.partition('?')
        name = path.strip('/')
        if name in ON_WP:
            return 'href="/%s/%s"' % (name, ('?'+qs) if qs else '')
        return 'href="https://apply.ctprivateoffice.com%s"' % href
    inner = re.sub(r'href="(/[^"]*)"', fix, inner)
    content = '<style>\n%s\n</style>\n<div class="%s">\n%s\n</div>' % (
        scope_css(css), SCOPE.lstrip('.'), inner.strip())
    pid += 1
    items.append((pid, title, slug, ptype, excerpt, content))

def esc(s): return html.escape(s, quote=False)

parts = ['''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
  xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:wfw="http://wellformedweb.org/CommentAPI/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.2/">
<channel>
  <title>Tax 4 Pros insight articles</title>
  <link>https://tax4pros.co.uk</link>
  <description>Four search articles for the Insights blog</description>
  <language>en-GB</language>
  <wp:wxr_version>1.2</wp:wxr_version>
  <wp:base_site_url>https://tax4pros.co.uk</wp:base_site_url>
  <wp:base_blog_url>https://tax4pros.co.uk</wp:base_blog_url>''']

for pid, title, slug, ptype, excerpt, content in items:
    parts.append('''  <item>
    <title>%s</title>
    <link>https://tax4pros.co.uk/%s/</link>
    <pubDate>%s</pubDate>
    <dc:creator><![CDATA[admin]]></dc:creator>
    <guid isPermaLink="false">https://tax4pros.co.uk/?p=%d</guid>
    <description></description>
    <content:encoded><![CDATA[%s]]></content:encoded>
    <excerpt:encoded><![CDATA[%s]]></excerpt:encoded>
    <wp:post_id>%d</wp:post_id>
    <wp:post_date><![CDATA[%s]]></wp:post_date>
    <wp:post_date_gmt><![CDATA[%s]]></wp:post_date_gmt>
    <wp:comment_status><![CDATA[closed]]></wp:comment_status>
    <wp:ping_status><![CDATA[closed]]></wp:ping_status>
    <wp:post_name><![CDATA[%s]]></wp:post_name>
    <wp:status><![CDATA[draft]]></wp:status>
    <wp:post_parent>0</wp:post_parent>
    <wp:menu_order>0</wp:menu_order>
    <wp:post_type><![CDATA[%s]]></wp:post_type>
    <wp:is_sticky>0</wp:is_sticky>
  </item>''' % (esc(title), slug, now.strftime('%a, %d %b %Y %H:%M:%S +0000'),
                pid, content, excerpt, pid,
                now.strftime('%Y-%m-%d %H:%M:%S'), now.strftime('%Y-%m-%d %H:%M:%S'),
                slug, ptype))

parts.append('</channel>\n</rss>')
open('tax4pros-wordpress-import.xml','w',encoding='utf-8').write('\n'.join(parts))
print('wrote tax4pros-wordpress-import.xml', os.path.getsize('tax4pros-wordpress-import.xml'), 'bytes,', len(items), 'items')
