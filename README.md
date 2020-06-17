# Caching
 Design a caching library from scratch

## Introduction

In this project, I will use a dictionary for our cache.
A cache is a way to store a limited amount of data such that future requests for said data can be retrieved faster.

## Variables:
- cache: Defines the cache, dictionary data type;
- queue: It is used to realize the first-in, first-out functionality;
- size: Defines the maximum size of the cache.

## Design
A cache design should consider so many factors like size, speed etc. There is an inherent trade-off between size and speed (given that a larger resource implies greater physical distances) but also a tradeoff between expensive, premium technologies (such as SRAM) vs cheaper, easily mass-produced commodities. 

## Cache
I set the data type of cache as defaultdict(set). Because, the speed of defaultdict much faster than normal dict in python, especially when the dataset is very huge. As we know, the default value for defaultdict(set) is {}. We can simplely check its key’s existence by calling “not cache[key]” which will return True if the key doesn’t exist. Besides, a defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

## FIFO Queue
In this project, I use a FIFO queue to manage the sequence of the key, value pair. FIFO stands for first-in, first-out. It's an algorithm which used by the stack memory. When the stack memory is full, some data of the memory need to be cleared to stored new data, as figure 1 shows. FIFO – an acronym for first in, first out – in computing and in systems theory, is a method for organizing the manipulation of a data structure – often, specifically a data buffer – where the oldest (first) entry, or 'head' of the queue, is processed first.

## Functions:

- Insert(key, value): insert key, value into cache
- Update(key, value): update the value by key
- Delete(key): Delete the value by key
- remove_redundance(): Remove the oldest record once the cache is full. 


## Author: Zuo Rui
## Date: 17 June, 2020