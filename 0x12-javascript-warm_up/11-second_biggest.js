#!/usr/bin/node
const arrayIni = process.argv;

if (arrayIni.length <= 3) {
  console.log(0);
} else {
  arrayIni.splice(0, 2);
  arrayIni.sort(function (a, b) { return b - a; });
  console.log(Number(arrayIni[1]));
}
