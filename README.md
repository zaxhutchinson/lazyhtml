# lazyhtml

Version 0.11

Tested with Python 3.4.3

Python module to create simple html pages. For another project I'm working on, I need a very simple, stupidly straight-forward way to generate lots of html pages using python. I will add features as I need them. This is not meant to provide full html support, so if I need something in my project, I'll add it.

<b>Instructions:</b>

Import module into your project

<code>import lazyhtml</code>

Create a new LazyHtml object:

<code>html_page = lazyhtml.LazyHtml()</code>

The constructor can take several html specifics to set up your page, but it comes with the usual defaults for doctype, lang, etc.

<b>Headings:</b> 

There are separate functions for headings h1 ... h6.

<pre>
html_page.addHeadingOne("Heading 1")
html_page.addHeadingTwo("Heading 2")
etc
</pre>

<b>Paragraph:</b>

<code>
html_page.addParagraph(string_of_text)
</code>

<b>Ordered and Unordered Lists:</b> 

Pass in a python list of strings, ints, etc. Ordered list function can take an optional arg that sets the type used to count the elements.

<pre>
html_page.addOrderedList(python_list, type="1")
html_page.addUnorderedList(python_list)
</pre>

<b>Table:</b> 

Tables are created from a list of lists. The first list is <i>always</i> considered to contain the headers. It does not do any check to make sure things line up. Again, this is a very dumb parse. LazyHtml takes no ownership of the data being fed to it.

<pre>
t = []
t.append(['Name', 'Age'])
t.append(['Bill', '50'])
t.append(['Carl', '70'])
html_page.addTable(t)
</pre>

<b>CSS:</b>

My intention is to set up global css styles using the addStyle() function, which get passed an element string and a full style string.

<code>
html_page.addStyle("p", "color:blue")
</code>

This will build the following in the style tag of the head section:

<code>
p{color:blue}
</code>

If you add another style for paragraph, it will add it properly to the list.

<b> Create & Open:</b>

Finally create the page.

<code>html_page.createPage()</code>

And you can open it in your default browser by calling

<code>html_page.openPage()</code>

<b>NOTES</b>
- Some values, such as those for lists or tables, are blindly converted to string using str() without type-checking.
- I have no idea which css styles work and which don't. For paragraph and heading you can pass in local styles, but only a few.
- There is a function to add and remove meta tags.

I will write more complete instructions if they are needed when I feel the module is further along. For now, examine the file test.py for use.

Version 0.11
- Adds helpers to clear both the whole page and the body so an object can be reused.
- Now page creating and saving are split and pages are stored in the object until another call to create or clear.
- Adds helper to change the filename used to save the page to disk.

Version 0.10 - Initial Commit
- Needs more testing. Code is first run. Read at your own risk. No comments.
- Supports paragraphs, headings, page title, tables, ordered and unordered lists, preformatted text, line breaks, horizontal lines, and css styles in some form or fashion.
