import webbrowser

class LazyHtml:
    def __init__(self, filename="untitled", doc_type="html", lang="en", encoding="utf-8"):
        self.filename = filename
        self.doc_type = doc_type
        self.lang = lang
        self.encoding = encoding
        self.title = "UNTITLED"
        self.meta = {}
        self.body = ""
        self.styles = {}

    def addTitle(self, title):
        self.title = title

    def addMetaTag(self, name, content):
        if name not in self.meta.keys():
            self.meta[name] = content
    
    def removeMetaTad(self, name):
        if name in self.meta.keys():
            del self.meta[name]

    def addStyle(self, element, style):
        if element not in self.styles:
            self.styles[element] = []
        self.styles[element].append(style)

    def createPage(self):
        page = ""

        page += ("<!doctype " + self.doc_type + ">")
        page += ("<html lang=\"" + self.lang + "\">")
        page += ("<head>")
        page += ("<meta charset=\"" + self.encoding + "\">")
        page += ("<title>" + self.title + "</title>")

        if len(self.styles) > 0:
            page += ("<style>")

        for element, styles in self.styles.items():
            page += (element + "{")
            for style in styles:
                page += (style + ";")
            page += ("}")
        if len(self.styles) > 0:
            page += ("</style>")


        page += ("</head>")
        page += ("<body>")
        page += self.body
        page += ("</html>")

        with open(self.filename, 'w') as f:
            f.write(page)

    def openPage(self):
        webbrowser.open_new_tab(self.filename)

    def parseStyleTags(self, styles):
        color = None
        text_align = None
        font_family = None
        font_size = None
        title = None
        list_style_type = None
        
        style_phrase = ""
        style_lead = "style=\""
        style_tags = ""

        for k, v in styles.items():
            if "color" == k:
                if len(style_tags) > 0:
                    style_tags += ";"
                style_tags += ("color:" + str(v))
            if "textalign" == k:
                if len(style_tags) > 0:
                    style_tags += ";"
                style_tags += ("text-align:" + str(v))
            if "fontfamily" == k:
                if len(style_tags) > 0:
                    style_tags += ";"
                style_tags += ("font-family:" + str(v))
            if "fontsize"  == k:
                if len(style_tags) > 0:
                    style_tags += ";"
                style_tags += ("font-size:" + str(v))
            if "liststyle" == k:
                if len(style_tags) > 0:
                    style_tags += ";"
                style_tags += ("list-style-type:" + str(v))
        if len(style_tags) > 0:
            style_phrase = style_lead + style_tags + "\""

        return style_phrase

    def addHeadingOne(self, text):
        self.body += ("<h1>" + text + "</h1>")
    def addHeadingTwo(self, text):
        self.body += ("<h2>" + text + "</h2>")
    def addHeadingThree(self, text):
        self.body += ("<h3>" + text + "</h3>")
    def addHeadingFour(self, text):
        self.body += ("<h4>" + text + "</h4>")
    def addHeadingFive(self, text):
        self.body += ("<h5>" + text + "</h5>")
    def addHeadingSix(self, text):
        self.body += ("<h6>" + text + "</h6>")

    def addParagraph(self, text, **kwargs):
        style_tags = self.parseStyleTags(kwargs)
        self.body += ("<p " + style_tags + ">" + text + "</p>")

    def addLineBreak(self):
        self.body += "<br/>"

    def addHorizontalLine(self):
        self.body += "<hr/>"

    def addLink(self, href, text=None):
        link = "<a href=" + href + ">"

        if text:
            link += (text + "</a>")
        else:
            link += (href + "</a>")

        self.body += link

    def addPreformattedText(self, text):
        self.body += ("<pre>" + text + "</pre>")

    def addTable(self, table, **kwargs):

        style_tags = self.parseStyleTags(kwargs)

        self.body += ("<table " + style_tags + ">")

        table_body = ""

        headers = table[0]
        if len(headers) > 0:
            table_body += "<tr>"
        for header in headers:
            table_body += ("<th>" + str(header) + "</th>")
        if len(headers) > 0:
            table_body += "</tr>"

        for i in range(1, len(table)):
            table_body += "<tr>"
            for data in table[i]:
                table_body += ("<td>" + str(data) + "</td>")
            table_body += "</tr>"

        table_body += "</table>"

        self.body += table_body

    def addUnorderedList(self, ulist, **kwargs):
        style_tags = self.parseStyleTags(kwargs)

        list_body = "<ul " + style_tags + ">"

        for item in ulist:
            list_body += "<li>"
            list_body += str(item)
            list_body += "</li>"

        list_body += "</ul>"
        self.body += list_body

    def addOrderedList(self, olist, type="1", **kwargs):
        style_tags = self.parseStyleTags(kwargs)

        list_body = "<ol type=\"" + type + "\" " + style_tags + ">"

        for item in olist:
            list_body += "<li>"
            list_body += str(item)
            list_body += "</li>"

        list_body += "</ol>"
        self.body += list_body
