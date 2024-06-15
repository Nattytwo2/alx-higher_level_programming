#!/usr/bin/node
function factorial (num) {
  if (num <= 1 | !num) {
    return 1;
  } else {
    return factorial(num - 1) * num;
  }
}

const num = Number(process.argv[2]);

console.log(factorial(num));
