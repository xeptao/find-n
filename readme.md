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

Read [this](https://github.com/xeptao/find-n/blob/master/assets/info.pdf) nicely written PDF file to get information about the mathematics.

### Applying the Solution in `Code`

It's really easy. Just apply the formula of `n` and return `n`.

#### Summary

```
FUNCTION find_n, PARAMS (array, wanted_value):
  SET k = first item of array
  SET l = second item of array

  # apply formula of n
  SET n = (s-2*k+l)/(l-k)

  RETURN n
```

<br>

## License

All of the contents inside the files of the repository "find-n" which is owned by **[xeptao](https://github.com/xeptao)**; is licensed under the [**MIT License**](https://github.com/xeptao/).
