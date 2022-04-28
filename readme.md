# `find-n`

Alice asks Bob to find the index of the value given in the cards; while turning the least amount of cards. This repository presents the solution of the problem, generalized for any card set.

## Table of Contents

- [Preview](https://github.com/xeptao/find-n#preview)
- [Solution](https://github.com/xeptao/find-n#solution)
- [License](https://github.com/xeptao/find-n#license)

<br>

## Preview

Input:

```python
find_n([1, 3, 5, 7, 9], 7)
```

Output:

```python
{'wanted': 7, 'pos': 4}
```

And in fact, it is on pos 4 (result is 1-based).

<br>

## Solution

### Formula of n'th Item

![Formula](/assets/formula.png)

### Proof of Formula

![Proof](/assets/proof.png)

### Formula for `n`

Make the [formula](https://github.com/xeptao/find-n#formula-of-nth-item) equal to the wanted number and solve it.

![Find N](/assets/find-n.png)

And in fact, if you look above, 5 is the 3rd card.

### Applying the Solution in `Code`

We know that the `n`'th item is `an+c`. Since we can't solve an equation directly; we should do the inverse operations to isolate `n`. Divide by `a`, and subtract by `c`.

So we have to take in an array, and the number the user wants to find the index of.

Rest is pretty easy, just return `n`.

#### Summary

We derive `a` and `c` from the [formula](https://github.com/xeptao/find-n#formula-of-nth-item).

```
FUNCTION find_n, PARAMS (array, wanted_value):
  SET first = first item of array
  SET second = second item of array

  # an+c is the form.
  SET a = second-first
  SET c = 2\*first-second

  # do the inverse operations
  SET n = (wanted_value/a)-c

  RETURN n
```

<br>

## License

All of the contents inside the files of the repository "find-n" which is owned by **[xeptao](https://github.com/xeptao)**; is licensed under the [**MIT License**](https://github.com/xeptao/).
