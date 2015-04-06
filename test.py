import lazyhtml

html_page = lazyhtml.LazyHtml()
html_page.addTitle("Stop Testing Me!")
html_page.addHeadingOne("TEST PAGE")
html_page.addParagraph("This is a bunch of fake text that no one should read. It is, in fact, top secret.", color="blue", fontfamily="courier")
html_page.addStyle("h1", "color:blue")
html_page.addStyle("h1", "background-color:yellow")
html_page.addStyle("table, th, td", "border: 1px solid black")
html_page.addStyle("table, th, td", "padding: 15px")

stupid_list = [ "Cow", "Pig", "Goat", "Ape", "Monkey", "Cat"]

stupid_table = []
stupid_table.append(["First Name", "Last Name", "Age"])
stupid_table.append(["Jim", "Jimson", 10])
stupid_table.append(["Sven", "Svenson", 20])
stupid_table.append(["Paul", "Paulson", 30])
stupid_table.append(["Erik", "Erikson", 40])

html_page.addUnorderedList(stupid_list)
html_page.addOrderedList(stupid_list)
html_page.addTable(stupid_table)
html_page.createPage()
html_page.openPage()

