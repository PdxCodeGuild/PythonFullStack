
# JavaScript Array Methods

 - [JavaScript Array Methods](#javascript-array-methods)
   - [`Array.prototype.forEach()`](#arrayprototpyeforeach)
   - [`Array.prototype.map()`](#arrayprototypemap)
   - [`Array.prototype.filter()`](#arrayprototypefilter)
   - [Combining `.map()` and `.filter()`](#combining-map-and-filter)
   - [`Array.prototype.reduce()`](#arrayprototypereduce)

JavaScript's Arrays come with some very helpful iteration methods: `.forEach()`, `.map()`, `.filter()` & `.reduce()`.  They all do different things, but are used in the same way: the methods take in a callback function to be called on each element of the array.  CSS Tricks has a very helpful guide right [here](https://css-tricks.com/an-illustrated-and-musical-guide-to-map-reduce-and-filter-array-methods/).

## `Array.prototype.forEach()`

[`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) (MDN Docs) is the simplest of the four methods in this document and can be used in place of a plain JavaScript for loop:

```javascript
const colors = ['red', 'green', 'blue']

// for loop
for (let i = 0; i < colors.length; i ++) {
  const color = colors[i]
  console.log(color)
}

// .forEach() with arrow function
colors.forEach(color => console.log(color))

// .forEach() with function keyword
colors.forEach(function(color) {
  console.log(color)
})
```

Note: `.forEach()`, `.map()` & `.filter()` can take callback functions with 3 parameters: element, index, & array.
```javascript
const colors = ['red', 'green', 'blue']

colors.forEach((color, index, arr) => console.log(color, index, arr))
// red 0 ['red', 'green', 'blue']
// green 1 ['red', 'green', 'blue']
// blue 2 ['red', 'green', 'blue']
```

## `Array.prototype.map()`

[`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) (MDN Docs) works very similarly to `.forEach()`.  However `.map()` returns a new array filled with what each callback function returns:

```javascript
const colors = ['red', 'green', 'blue']

// arrow function
let sentences = colors.map(color => 'I spy with my little eye something... ' + color + '.')

// function keyword
sentences = colors.map(function(color) {
  return 'I spy with my little eye something... ' + color + '.'
})

console.log(sentences)
// [
  // 'I spy with my little eye something... red.',
  // 'I spy with my little eye something... green.',
  // 'I spy with my little eye something... blue.'
// ]
```

## `Array.prototype.filter()`

[`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) (MDN Docs) is yet another useful array method.  Like `.map()`, `.filter()` returns a new array.  But `.filter()` returns an array of the elements which pass the test given to the callback function.  If the function returns a truthy value, the element will be included in the new array:

```javascript
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

const evens = nums.filter(num => num % 2 === 0)
const odds = nums.filter(num => num % 2 === 1)

console.log(evens, odds)
// [2, 4, 6, 8] [1, 3, 5, 7, 9]
```

## Combining `.map()` and `.filter()`

Often JavaScript developers will want to take in some array, filter out some elements, and transform the remaining ones.  Or perhaps they'd want to transform the existing elements and then filter out the transformed elements.  `map` and `filter` each return new arrays, so they can be chained together:

```javascript
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

const evenSentences = nums.filter(num => num % 2 === 0).map(num => `${num} is an even number.`)
console.log(evenSentences)
// [
  // '2 is an even number.',
  // '4 is an even number.',
  // '6 is an even number.',
  // '8 is an even number.'
//]

const oddSentences = nums.filter(num => num % 2 === 1).map(num => `${num} is an odd number.`)
console.log(oddSentences)
// [
  // '1 is an odd number.',
  // '3 is an odd number.',
  // '5 is an odd number.',
  // '7 is an odd number.',
  // '9 is an odd number.'
//]
```

## `Array.prototype.reduce()`
COMING SOON!  Check out the MDN Docs here: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)