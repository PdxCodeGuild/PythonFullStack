
# Overview

- [Intro](#intro)
- [The Script Tag](#the-script-tag)
- [JavaScript Preprocessors](#javascript-preprocessors)
- [Learning Resources](#learning-resources)
- [Frameworks](#frameworks)
  - [General UI](#general-ui)
  - [Data Visualization](#data-visualization)
  - [Music / Sound](#music--sound)
  - [3D Graphics](#3d-graphics)
  - [Games](#games)
- [Comparison of Python and JavaScript](#comparison-of-python-and-javascript)
  - [Conditionals](#conditionals)
  - [While Loops](#while-loops)
  - [For Loops](#for-loops)
  - [Modulus](#modulus)
    - [Modulus in Python](#modulus-in-python)
    - [Modulus in JavaScript](#modulus-in-javascript)

## Intro

JavaScript is a front-end language, written in `<script>` tags or in external `.js` files, and run by an interpreter in the browser. You can find more info in JavaScript [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) and [here](https://www.w3schools.com/js/default.asp). You can view a list of JavaScript frameworks [here]().

JavaScript has become the de-facto standard for front-end. There used to be Flash (which had a JavaScript-like language called ActionScript), Java Applets, and Microsoft's Silverlight. But with the development of stronger standards for JavaScript and the discovery of security holes in the other frameworks, browsers began dropping support.

JavaScript is part of the 'C Family' of languages, those with syntax based on that of C: C++, Java, C#, Objective-C, Swift, Go, and [more](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages). You can find a brief account of the history of C Family languages [here](https://softwareengineering.stackexchange.com/questions/135544/why-are-several-popular-programming-languages-influenced-by-c). Familiarizing yourself with JavaScript syntax will enable you to more easily transition to these languages. That said, a thorough understanding of the principles underlying any one language will enable you to transition to any others. In JavaScript, most of the forms familiar to Python are there: numbers, strings, loops, classes, etc.

JavaScript (as its name implies) is a **scripting** language, meaning it was designed to be quick to write and ad-hoc. This worked well when pages were simple, but as web applications became more complex, its loose syntax became more of a hindrance. It is much easier to write messy code which is difficult to read, debug, and extend. Therefore it's important to impose upon yourself strict organization and 'best practices'.

The latest iteration of the JavaScript specification (called ECMAScript) is ECMAScript 6. All major browsers support ES6, but older browsers might not. You can view a table of features and browse compatibility [here](https://kangax.github.io/compat-table/es6/).


## The Script Tag

In an HTML page, we can specify blocks of JavaScript code using `<script>` tags.You may see a `type="text/javascript"` attribute on script tags, this was necessary in HTML4.01, but not in HTML5. You can put `script` tags anywhere, but most often you'll want to put them in the `<head>` or at the bottom of the `<body>`. If you put in the head, you cannot do `document.getElementById`, `document.querySelector`, etc, on the elements in the body, because the JavaScript would be executed before the body is loaded. You have to either wrap it in a `window.onload = function () {...}` or put it at the bottom of the body.

```html
<html>
    <head>
        ...
        <script>
            let mydiv = document.querySelector('#mydiv')
            console.log(mydiv) // null - mydiv hasn't been loaded yet
        </script>
    </head>
    <body>
        <div id="mydiv"></div>
        <script>
            mydiv = document.querySelector('#mydiv')
            console.log(mydiv) // <div> - mydiv has already appeared in the page
        </script>
    </body>
</html>
```

A script tag may also reference an external file containing JavaScript, denoted with a `.js` suffix.

```html
<script src="myscript.js"></script>
```

JavaScript can also be written in-line, it's fine for testing but this is generally bad practice because it's harder to keep track of code when it's spread throughout the html.

```html
<button onclick="alert('Hello World!')">click me</button>
```

## JavaScript Preprocessors

There are various JavaScript preprocessors that make writing JavaScript easier: [CoffeeScript](http://coffeescript.org/), [Babel](https://babeljs.io/), [Typescript](https://www.typescriptlang.org/), [Livescript](http://livescript.net/)




## Learning Resources


- MDN
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [First Steps](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps)
- Books
  - [Eloquent JavaScript](https://eloquentjavascript.net/)
  - [JavaScript for Cats](http://jsforcats.com/)
  - [JSbooks](https://jsbooks.revolunet.com/)
  - [You Dont Know JS](https://github.com/getify/You-Dont-Know-JS)
- Online Courses
  - [codecademy](https://www.codecademy.com/learn/introduction-to-javascript)
  - [w3schools](https://www.w3schools.com/js/js_exercises.asp)
  - [edabit](https://edabit.com/challenges/javascript)
  - [w3resource](https://www.w3resource.com/javascript-exercises/)

## Frameworks

You can view a long list on [wikipedia](https://en.wikipedia.org/wiki/List_of_JavaScript_libraries), [javascripting.com](https://www.javascripting.com/), and [here](https://github.com/collections/front-end-javascript-frameworks).

### General UI

- [AngularJS](https://angularjs.org/)
- [Angular](https://angular.io/)
- [React](https://facebook.github.io/react/)
- [Vue.js](https://vuejs.org/)
- [Ember.js](https://www.emberjs.com/)
- [Riot.js](http://riotjs.com/)

### Data Visualization

- [D3](https://d3js.org/)
- [Chart.js](http://www.chartjs.org/)
- [Dygraph](http://dygraphs.com/)
- [Vega](https://vega.github.io/vega/)


### Music / Sound

- [Tone.js](https://tonejs.github.io/)
- [Howler.js](https://howlerjs.com/)
- [Sound.js](https://createjs.com/soundjs)


### 3D Graphics

- [three.js](https://threejs.org/)
- [A-Frame](https://aframe.io/)
- [wrld](https://www.wrld3d.com/)

### Games

- [Phaser](https://phaser.io/)
- [Babylon.js](http://www.babylonjs.com/)




## Comparison of Python and JavaScript

In Python `if`, `while` and `for` don't require parentheses, have colons, and use indentation to define the body. In JavaScript, these statements **do** require parentheses, don't have a colon, and require curly braces to define the body. If you don't write curly braces, the next statement will be considered the body.

| Python | JavaScript |
|--- |--- |
| True False | true false |
| and | && |
| or | &#124;&#124; |
| not | ! |
| None | null |
| self | this |
| if c: | if (c) {} |
| elif c: | else if (c) {} |
| else: | else {} |
| while c: | while (c) {} | 
| for i in range(len(mylist)): | for (let i=0; i<myarray.length; ++i) {} |
| a if c else b | c? a: b |


### Conditionals

```python
temperature = int(input('what is the temperature?'))
if temperature >= 80:
    print('hot')
elif temperature >= 70:
    print('warm')
elif temperature >= 60:
    print('chilly')
else:
    print('cold') 
```


```javascript
let temperature = prompt('what is the temperature?')
if (temperature >= 80) {
    alert('hot')
} else if (temperature >= 70) {
    alert('warm')
} else if (temperature >= 60) {
    alert('chilly')
} else {
    alert('cold')
}
```



### While Loops

In Python, `while` loops don't need parentheses and use a colon and indentation.

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

In JavaScript `while` loops need parentheses and use curly braces.

```javascript
let i = 0
while (i < 10) {
    console.log(i)
    i += 1
}
```

### For Loops

In Python, `for` loops are structured very differently:

```python
for i in range(10):
    print(i)
```

The three parts of a JavaScript for loop are the **initialization**, **condition**, and **increment**.

```javascript
for (let i=0; i<10; ++i) {
    console.log(i);
}
```


### Modulus

Modulus works differently in each language for negative numbers.

#### Modulus in Python

```python
for i in range(-4, 5):
    print(f'{i}%3={i%3}')
```
```
-4%3=2
-3%3=0
-2%3=1
-1%3=2
0%3=0
1%3=1
2%3=2
3%3=0
4%3=1
```

#### Modulus in JavaScript

```javascript
for (let i=-4; i<5; ++i) {
    console.log(i+'%3='+(i%3));
}
```

```
-4%3=-1
-3%3=0
-2%3=-2
-1%3=-1
0%3=0
1%3=1
2%3=2
3%3=0
4%3=1
```
