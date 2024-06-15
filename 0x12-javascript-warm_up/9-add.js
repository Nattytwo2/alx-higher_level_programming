#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const numOne = Number(process.argv[2]);
const numTwo = Number(process.argv[3]);

console.log(add(numOne, numTwo));
