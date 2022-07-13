# HTML Cheat Sheet

HTML &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Hyper text markup language

Tags   &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; ```<a href="https://github.com/"></a>```

Element &nbsp; &nbsp; &nbsp; &nbsp;   a

Attributes &nbsp; &nbsp; &nbsp; &nbsp;href="https://github.com"\
Common Attributes

- src
- href
- class
- id

Elements can have unique identifiers used by javascript and CSS\
 ```<p id="fruit"> Apple Orange Banana </p>```

Elements can be styled by belonging to a class of Elements\
```<p class="redThings"> This text will be colored red if "redThings" says so```

**Index.html**\
The index.html page is the most common name used for the default page shown on a website if no other page is specified when a visitor requests the site. In other words, index.html is the name used for the homepage of the website

```HTML
<!DOCTYPE HTML>
<html lang="en">

<html>
    <head>

        <!-- meta tags - start with those 3 metatags before anything else
            Description and language support for HTML-->
        <meta charset="UTF-8">
        <meta name="description" content="الوصف اللى بيظهر تحت الموقع بتاعك لما بتعمل سيرش">
        <title>Cheat Sheet</title>

        <!-- add a link with a relation of style sheet for css -->
        <link rel="stylesheet" type="text/css" href="../index.css">
        <script type="text/javascript" src="../index.js"></script>
    </head>

    <body>
        <h1><strong><em>Cheat Sheet</em></strong></h1>
        <h2>A <ul>semi</ul> complete <mark>HTML </mark>Cheat sheet</h2>

        <p>In order to <sub>practice</sub> my <sup>muscle memory</sup>, I'll try to remember as much as possible, from HTML, Tags, Elements & Attributes.</p>

        // Must contain the link's protocol `https://`
        <a href="https://github.com/" target="_blank">Github.com</a>
        <a href="#container">Go to the div line</a>

        <script src="https://ajax.googleapis.com/ajax/lib">JS</script>

        <audio></audio>
        <video></video>
        <canvas></canvas>
        <div class="container" id="myID">The div line.</div>
        <span></span>

        <!-- Button element, contains unique id to be called using, CSS or javascript, and contains count() function which will be called when the button is clicked -->
        <button id="count-el" onclick="count();">Count</button>



        <!DOCTYPE>  Defines the document type
        <html> Defines the root of an HTML document </html>
        <title> Defines a title for the document </title>
        <header> Defines a header for a document or section </header>
        <main> Specifies the main content of a document </main>
        <footer> Defines a footer for a document or section </footer>


        <p style="font-family:serif; color:black; max-width:100%; background-color:white; font-weight:bold"> Defines a paragraph </p>
        <a> Defines a hyperlink </a>
        <b> Defines bold text </b>
        <br> Defines a single line break </br>
        <button> Defines a clickable button </button>
        <div> Defines a section in a document </div>
        <footer> Defines a footer for a document or section </footer>
        <h1> to <h6> Defines HTML headings </h1> to </h6>
        
        // width will scale the image, but the height will distort the image.
        <img src="../passengers.jpg" alt="passengers" width="300"/> Defines an image
        
        // Defines ordered/unordered lists & list items
        <ol> Defines an ordered list </ol>
        <ul> Defines an unordered list </ul>
        <li> Defines a list item  </li>

        <script> Defines a client-side script </script>
        <span> Defines a section in a document</span>
        

        // Defines a Table, cells and rows.
        <table border="2" bgcolor="yellow"> Defines a table
        <thead bgcolor="red"> Defines a table header
            <tr> Defines a row in a table
            <th>header1</th> Defines a header cell in a table 
            <th>header2</th>
            <th>header3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td>text1.1</td> Defines a cell in a table
            <td>text1.2</td>
            <td>text1.3</td>
            </tr>
            <tr>
            <td>text2.1</td>
            <td>text2.2</td>
            <td>text2.3</td>
            </tr>
            <tr>
            <td>text3.1</td>
            <td>text3.2</td>
            <td>text3.3</td>
            </tr>
            <tr>
            </tr>
        </tbody>
        </table>

    <div>
        <span>Hello</span>
    </div>

    <form>
        <button>Click me!</button><br>
        <input type="text" name="">
        
    </form>

    <div>
        <input type="text" placeholder="Enter your username"><br>
        <input type="email" placeholder="Enter your email"><br>
        <input type="password" placeholder="****************"><br>
        <input type="submit" value="Submit">
    </div>

    <script src="app.js"></script>
    </body>

</html>

```

![Differnce](https://i1.wp.com/www.differencebetween.com/wp-content/uploads/2018/02/Difference-Between-Block-and-Inline-Elements-fig-1.png?w=567&ssl=1)

## Resources

- [Best HTML cheat Sheet](https://htmlcheatsheet.com/)

- [Common CSS Properties Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference)
