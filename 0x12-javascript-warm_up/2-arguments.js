#!/usr/bin/node
const myArgv = process.argv.length;
if (myArgv < 3) {
  console.log('No argument');
} else if (myArgv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
