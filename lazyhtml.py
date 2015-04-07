# Lazy Html
# code by Zachary Hutchinson
#
# Makes it slightly easier to produce html docs from python data. I said slightly.

# Makes use of the webbrowser module to open html docs
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
        self.page = ""

    def addTitle(self, title):
        self.title = title

    def addMetaTag(self, name, content):
        if name not in self.meta.keys():
            self.meta[name] = content
    
    def removeMetaTag(self, name):
        if name in self.meta.keys():
            del self.meta[name]

    def addStyle(self, element, style):
        if element not in self.styles.keys():
            self.styles[element] = []
        self.styles[element].append(style)

    def changeFilename(self, filename):
        self.filename = filename

    # Removes all style attributes for a specific element,
    # allowing a reset.
    def removeStyle(self, element):
        if element in self.styles.keys():
            del self.styles[element]

    # Pulls together all the components and creates the html page,
    # storing the result in self.page. It overwrites any previously
    # created pages.
    def createPage(self):
        self.page = ""

        self.page += ("<!doctype " + self.doc_type + ">")
        self.page += ("<html lang=\"" + self.lang + "\">")
        self.page += ("<head>")
        self.page += ("<meta charset=\"" + self.encoding + "\">")
        self.page += ("<title>" + self.title + "</title>")

        if len(self.styles) > 0:
            self.page += ("<style>")

        for element, styles in self.styles.items():
            self.page += (element + "{")
            for style in styles:
                self.page += (style + ";")
            self.page += ("}")
        if len(self.styles) > 0:
            self.page += ("</style>")


        self.page += ("</head>")
        self.page += ("<body>")
        self.page += self.body
        self.page += ("</html>")

    # Saves self.page to a file using the filename stored in self.filename.
    def savePage(self):
        with open(self.filename, 'w') as f:
            f.write(self.page)

    def clearPage(self):
        self.page = ""

    def openPage(self):
        webbrowser.open_new_tab(self.filename)

    def clearBody(self):
        self.body = ""

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


