#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
console.log(isNaN(myNum) ? 'Not a number' : `My number: ${myNum}`);
