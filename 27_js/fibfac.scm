(define (factorial n)
    (if(<=n 1)
    1
    (*n (fact(-n 1))
)

(define (fibonacci n)
    (if (or(= n 0)(=n 1))
    n
    (+ fibonacci(- n 1)(fibonacci(- n 2)))