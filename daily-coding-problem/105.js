/* Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds. */

function foo() {
  console.log("bar");
}

function debounce(f, N) {
  let timeoutId;
  return function() {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      f();
    }, N);
  };
}

const debouncedFoo = debounce(foo, 500);

for (let index = 0; index < 10; index++) {
  debouncedFoo();
}
