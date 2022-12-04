from __future__ import annotations
from typing import Any, Dict, Tuple, List, Set, Optional, TextIO

import math
# Descriptions taken from https://codeofgeeks.com/important-algorithms-for-competitive-programming
# Eventually will look at these https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/


def binary_search(lst: List[Any], low, high, query: float) -> int:
	"""
		Parameters
	    ----------
	    lst : List[Any]
	        List of elements that need to be search,
	        the list MUST BE SORTED!!!

	    Returns
	    -------
	    return : boolean
	
		Description
		-----------
			Binary Search is a search algorithm that finds the 
			position of a target value within a sorted array.

		Time Complexity
		---------------
			O(log n)(base 2)
	"""

	if high>=low:
		mid = (high+low)//2

		if lst[mid]==query:
			return mid

		elif lst[mid]>query:
			return binary_search(lst, low, mid-1, query)

		elif lst[mid]<query:
			return binary_search(lst, mid+1, high, query)

	else:
		return -1 #item not found


def ternary_search(lst: List[Any]) -> List[Any]:
	"""
		Parameters
	    ----------
	    lst : List[Any]
	        List of elements that need to be search,
	        the list MUST BE SORTED!!!

	    Returns
	    -------
	    Todo: Implement

		PreConditions
		-------------
			lst must be presorted!!!

		Description
		-----------
			This algorithm is used to find an element in an 
			array. It is similar to binary search where we 
			divide the array into two parts but in this algorithm. 
			In this, we divide the given array into three parts.

		Time Complexity
		--------------- 
			O(log n)(base 3)
	"""

	raise NotImplementedError


def quick_sort(lst: List[Any]) -> List[Any]:
	"""
		Parameters
	    ----------
	    lst : List[Any]
	        List of elements that need to be search,
	        the list MUST BE SORTED!!!

	    Returns
	    -------
	    sorted_lst: List[Any]
	    	Sorted list of elements

		Description
		-----------
			Quick Sort Algorithm is based on divide and 
			conquer approach of problem solving. This 
			algorithm is very useful to sort a sequence 
			of integers of characters.

		Time Complexity
		---------------
			O(nlog n) // Average case
			O(n^2) // Worst case
	"""

	pivot = lst[0]
	pivot_index = 0

	raise NotImplementedError


def merge_sort(lst: List[Any]) -> List[Any]:
	"""
		Description
		-----------
			Merge Sort Algorithm is based on divide and 
			conquer approach of problem solving. This 
			algorithm is very useful to sort a sequence 
			of integers of characters.

		Time Complexity
		---------------
			O(nlog n)
	"""

	if len(lst) <= 2:
		if len(lst)==1:
			return lst

		elif lst[0]>lst[1]:
			temp = lst[1]
			lst[1] = lst[0]
			lst[0] = temp
			return lst

		return lst

	else:
		mid = len(lst) // 2
		lst1 = lst[:mid]
		print("======")
		print("[][][]")
		print(lst1)
		lst2 = lst[mid:]
		print(lst2)
		print("=====")

		lst1 =  merge_sort(lst1)
		lst2 = merge_sort(lst2)

		print(lst1)
		lst2 = merge_sort(lst2)
		print(lst2)
		print("------")

		if lst1[-1]>lst2[0]  	:
			return lst1 + lst2
		else:
			return lst2 + lst1

		return lst1 + lst2


def rabin_karp(pattern: str, text: str) -> str:
	"""
		Description
		-----------
			It is a string-searching algorithm created by 
			Richard M. Karp and Michael O. Rabin that uses 
			hashing to find an exact match of a pattern 
			string in a text.

		Time Complexity
		---------------
			O(n)
	"""

	raise NotImplementedError


def kmp(word: str, text: str) -> str:
	"""
		Description
		-----------
			It is a searching algorithm that searches for 
			occurrences of a “word” W within a main “text 
			string” S.

		Time Complexity
		---------------
			 O(n)
	"""

	raise NotImplementedError

if __name__ == "__main__":
	lst = [7, 23, 55, -25, -2, 0, -73]

	print(merge_sort(lst))