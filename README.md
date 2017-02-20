# Naive-Solver-for-Word-Guessing-Games
A general but naïve solver for word guessing games.

Got stuck while playing word games?
The solver may be naïve. It deserves a try, though.

### Usage
```
chmod +x ./guess_word.py 
./guess_word.py <dictionary> <dot-letter pattern> <letters in pool(candidates)>
```
You can get a plain dictionary of English words at [here](https://github.com/dwyl/english-words).

##### Explaining the "dot-letter pattern".
In a dot-letter pattern, dot(".") represents an unknown letter.
So if you have a word ```??ple??ed```(appleseed) to guess, the corresponding pattern will be ```"..ple..ed"```.

##### Explaining the "letters in pool".
Let's use the word ```??ple??ed```(appleseed) mentioned above.
If you have ```a, p, e, x, x, x, s, e, d``` as candidates to fill in the blanks, the letters in pool will be ```"apexxxsed"```.
Duplicated letters are accepted. As you can see, we have got 3 x's and 2 e's in this example. 

### Examples
##### Guessing the word "??pl?" (with candidates: a, b, e, e, e, t, p, l, z, x)
```
./guess_word.py ~/english-words-master/words.txt "..pl." "abeeetplzx"
```
You'll get the output as follows:
```
Dot-letter pattern given: 
	..pl.
Letters in pool: 
	a 	b 	e 	e 
	e 	t 	p 	l 
	z 	x 	p 	l 
Performing loose match ... 
	Progress: 354985, zyzzyvas                                        
Result: 2/354985
	apple 	pepla 
Performing strict match ...
Refined result: 2/2
	apple 	pepla
```

##### Guessing the word "b?si?e??" (with candidates: b, r, s, r, q, u, y, e, n, s)
```
./guess_word.py ~/english-words-master/words.txt "b.si.e.." "brsrquyens"
```
You'll get the output as follows:
```
Dot-letter pattern given: 
	b.si.e..
Letters in pool: 
	b 	r 	s 	r 
	q 	u 	y 	e 
	n 	s 	b 	s 
	i 	e 
Performing loose match ... 
	Progress: 354985, zyzzyvas                                        
Result: 1/354985
	business 
Performing strict match ...
Refined result: 1/1
	business 
```

### Could you buy me a cup of cappuccino?
PayPal | Alipay
----|----
[PayPal](https://www.paypal.me/makito) | [Alipay](https://qr.alipay.com/a6x02021re1jk4ftcymlw79)

### License
Beloved **MIT**

```
MIT License

Copyright (c) 2017 Makito Sumi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```