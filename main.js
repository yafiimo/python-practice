
function sumAll(arr) {
  if(arr[0] == arr[1]) {
    return arr[0] + arr[1];
  }

  let start = Math.min(arr[0], arr[1]);
  let end = start == arr[0] ? arr[1] : arr[0];
  let sum = start;

  for(let i = start + 1; i <= end; i++) {
    sum += i;
  }
  return sum;
}

console.log(sumAll([1,10]));


