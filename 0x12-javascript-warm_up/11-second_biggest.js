#!/usr/bin/node
// Parse command line arguments to integers
const numbers = process.argv.slice(2).map(Number);

numbers.sort((a, b) => b - a);

if (numbers.length < 2) {
  console.log(0);
} else {
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] !== numbers[0]) {
      console.log(numbers[i]);
      break;
    }
  }
}
