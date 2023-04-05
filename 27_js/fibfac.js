// Team Gelded Devos :: Daniel Liu, Emerson Gelobter
// SoftDev pd7
// K27 -- Basic functions in JavaScript
// 2023-04-04
// --------------------------------------------------

// as a duo...
// pair programming style,
// implement a fact and fib fxn

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fact(n){
    if (n <= 1){
        return 1
    }else{
        return (n * fact(n-1))
    }
}

function fib(n){
    if (n == 0 || n == 1){
        return n
    }else{
        return (fib(n-1) + fib(n-2))
    }
}

console.log(fact(1) === 1);
console.log(fact(2) === 2);
console.log(fact(3) === 6);
console.log(fact(4) === 24);
console.log(fact(5) === 120);

console.log(fib(0) === 0);
console.log(fib(1) === 1);
console.log(fib(2) === 1);
console.log(fib(3) === 2);
console.log(fib(4) === 3);
