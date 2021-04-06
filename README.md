
# paginateit

Used to paginate REST API Calls / Mostly on MultiThreaded API Calls via Python

## Description

Takes 2 inputs:
* count -> total number of items in all pages
* max_workers -> number of threads need to be created (Based upon the number provided, skip and limits are calculated dynamically)

## Getting Started

### Dependencies
Python 3.6 and further releases.

### Installing

```
pip install paginateit
```

### Executing program
```
page(23052, 4)

----------------|---------------|---------------|------------|
|SKIP           | LIMIT         | FLIMIT        | COUNT      |
|---------------|---------------|---------------|------------|
|skip1: 0       |limit1: 5763	|flimit1: 763	|count1: 5763|
|---------------|---------------|---------------|------------|
|skip2: 5763	|limit2: 11526	|flimit2: 1526	|count2: 5763|
|---------------|---------------|---------------|------------|
|skip3: 11526	|limit3: 17289	|flimit3: 7289	|count3: 5763|
|---------------|---------------|---------------|------------|
|skip4: 17289	|limit4: 23052	|flimit4: 3052	|count4: 5763|
|---------------|---------------|---------------|------------|
|skip5: 23052	|limit5: 28815	|flimit5: 8815	|count5: 5763|
|---------------|---------------|---------------|------------|

```

## Help

Any advise for common problems or issues.
```
page(count, max_workers) # max_workers defaults to 2 unless specified
```

## Authors

Contributors names and contact info

Manjesh N
[manjesh_n@hotmail.com](mailto:manjesh_n@hotmail.com)


## License

This project is licensed under the Apache License 2.0 License - see the LICENSE file for details

## Acknowledgments