#!/usr/bin/node
const varOne = process.argv[2] ? process.argv[2] : 'undefined';
const varTwo = process.argv[3];
console.log(varOne.concat(' is ', varTwo));
