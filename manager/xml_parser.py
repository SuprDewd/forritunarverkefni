ENTITIES = { 'lt': '<', 'gt': '>', 'amp': '&', 'quot': '"' }
ENTITIES_rev = { v: k for k,v in ENTITIES.items() }

class Text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return ''.join(map(lambda c: ENTITIES_rev[c] if c in ENTITIES_rev else c, self.text))

def escape_quotes(s):
    res = ''
    for c in s:
        if c in ['"', '\\']:
            res += '\\'
        res += c
    return res

class Element:
    def __init__(self, tag, attr={}, children=[]):
        self.tag = tag
        self.attr = attr
        self.children = children

    def __str__(self):
        return '<%s%s>%s</%s>' % (self.tag,
                                  ''.join(map(lambda (k,v): ' %s="%s"' % (k, escape_quotes(v)), self.attr.items())),
                                  ''.join(map(str, self.children)),
                                  self.tag)

    def __repr__(self):
        return '<%s%s>%s</%s>' % (self.tag,
                                  ''.join(map(lambda (k,v): ' %s="%s"' % (k, escape_quotes(v)), self.attr.items())),
                                  ''.join(map(repr, self.children)),
                                  self.tag)

def decode_entities(s):
    res = ''
    at = 0
    cnt = len(s)
    while True:
        while at < cnt and s[at] != '&':
            res += s[at]
            at += 1

        if at == cnt:
            break

        at += 1
        buff = ''
        while s[at] != ';':
            buff += s[at]
            at += 1

        at += 1
        res += ENTITIES[buff]

    return res

def encode_entities(s):
    return ''.join(map(lambda c: '&%s;' % ENTITIES_rev[c] if c in ENTITIES_rev else c, s))

def parse_xml(s, text_nodes=[], decode=False, decode_nodes=[]):
    tnodes = set(text_nodes)
    dnodes = set(decode_nodes)

    def is_whitespace(c):
        return c in [ ' ', '\n' ]

    def rec(s, at, is_text, decode=False):
        res = []
        while True:
            buff = ''
            while at < len(s) and s[at] != '<':
                assert s[at] != '>'
                buff += s[at]
                at += 1

            if is_text:
                res.append(Text(decode_entities(buff) if decode else buff))
                # print(res[-1])

            if at >= len(s) or s[at+1] == '/':
                break

            cdata_open = '<![CDATA['
            cdata_close = ']]>'

            if s[at:at+len(cdata_open)] == cdata_open:
                at += len(cdata_open)
                buff = ''
                while s[at:at+len(cdata_close)] != cdata_close:
                    buff += s[at]
                    at += 1

                at += len(cdata_close)
                res.append(Text(buff))
                continue

            tag = ''
            at += 1
            while not is_whitespace(s[at]) and s[at] != '>' and s[at] != '/':
                tag += s[at]
                at += 1

            attr = {}
            children = []
            while True:
                while at < len(s) and is_whitespace(s[at]): at += 1
                if s[at] == '/':
                    at += 1
                    assert s[at] == '>'
                    at += 1
                    break

                if s[at] == '>':
                    at += 1
                    at, children = rec(s, at, is_text or tag in tnodes or '*' in tnodes, decode or tag in decode_nodes)
                    close = '</%s>' % tag
                    assert s[at:at + len(close)] == close
                    at += len(close)
                    break

                key = ''
                while s[at] != '=':
                    key += s[at]
                    at += 1

                at += 1
                assert s[at] == '"'
                at += 1

                val = ''
                while s[at] != '"':
                    if s[at] == '\\':
                        if s[at+1] == '\\':
                            val += '\\'
                            at += 2
                        elif s[at+1] == '"':
                            val += '"'
                            at += 2
                        else:
                            assert False
                    else:
                        val += s[at]
                        at += 1

                attr[key] = val
                at += 1

            res.append(Element(tag, attr=attr, children=children))

        return at, res

    return rec(s, 0, False, decode)[1]
