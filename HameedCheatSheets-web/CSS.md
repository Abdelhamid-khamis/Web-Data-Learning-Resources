# CSS Cheat Sheet

## Syntax

![Syntax](https://www.w3schools.com/css/img_selector.gif)

## CSS Specifity

![CSS Specifity](https://res.cloudinary.com/practicaldev/image/fetch/s--XI6qg9BK--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dkerupv5p9lu9k10w5l1.png)

- CSS executes properties line by line, so that the last line is always the line that remains.
  
```CSS
/*Syntax*/
selector{
property: value;
property2: value2;
}

/*Include external css file*/
<link rel="stylesheet" type="text/css" href="/style.css" />

/* Inline styles */
<tag style="property: value"> </tag>



.class {
  /* Selects all elements with class = "class" */
}

#id {
  /* Selects all elements with id = "class" */
}

p {
  /* Selects all p elements */
}

p.class {
  /* Selects all p elements with class = "class" */
}

a[target="_blank"] {
  background-color: yellow;
}

h1, p {
  /* Selects all h1 elements and p elements */
}

h1 p {
    /* Selects all p elements inside h1 elements */
}

h1 > p {
    /* Selects all p elements whose parent is a h1 element */
}

h1 + p {
    /* Selects all p elements immediately after h1 elements */
}

h1 ~ p {
    /* Selects every p element preceded by a h1 element */
}


<!-- Add image by a HTML element: -->
<div style="background-image: url('img.jpg');">

<!-- Add to the entire body: -->
<style>
body {
  background-image: url('img.jpg');
}
</style>

.img-responsive{
    max-width: 100%;
    height: auto;
    width: auto\9; /* ie8 */
    object-fit: contain;
    background-image: url("https://cdn.vox-cdn.com/thumbor/ajQqX6GfVMuJoRYMh2pl3eJsRv0=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/13959855/acastro_190218_1777_apple_streaming_0003.jpg");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
  }
```

## Most Common CSS Properties with the equivalent of the DOM notation which is usually accessed from JavaScript

- if CSS property was 1 word, so DOM Notation is the same as CSS property `e.g. font == font`.
- if CSS property was 2 words, so DOM Notation is the same as CSS property but in camelCase `e.g. border-width == borderWidth`.

```CSS
Property            Description                     JavaScript

color               Element                         color  
background-color    Background color                backgroundColor
background-image    Sets the background image       backgroundImage
display             Display behavior {block, inline-block, inline, none}
width               Element width 
height              Element height 
min-width           Minimum width 
min-height          Minimum height 
max-width           Maximum width 
max-height          Maximum height 
margin Outter       margins property 
padding Inner       margin property 
border              Border property 
border-color        Border color 
border-width        Border width 
border-style        Border style {none, solid, dotted, inset, dashed solid}

border-radius       Border radius 
font                Font properties 
font-family         Defines the font 
font-style          Font style {normal, italic, oblique}
font-weight         Thickness of the font {normal, bold, lighter, bolder}
position            Type of positioning used for an element `{static, relative, absolute, fixed, sticky}`
z-index             Sets the order of overlapping elements `{auto, -1, 0, 1, 2, 3 ...}`
```

### Resources

- [Best CSS cheat Sheet](https://htmlcheatsheet.com/css/)

- [Common CSS Properties Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference)

- [CSS Styling Images](https://www.w3schools.com/css/css3_images.asp)
