'''
function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) 
where the list indices meet the requirement i < j < k.  
The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive. 

This is a O(n^2) solution given for this problem.
This uses a dictionary to fetch the results in O(1) time.
'''



def solution(l):
	count = 0
	d = {}
  
  # Initialize the dictionay with an empty list for all the keys in the dictionary
	
  for i in range(len(l)):
		d[i] = []
  
  # Looping all the values in the list, this adds the position of the element to 
  #the list of a specific key of the dictionary if the number is divisible by the current number
  
  
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[j]%l[i] == 0:
				d[i].append(j)
	key = list(d.keys())
	for i in range(len(key)):
		for j in range(len(d[key[i]])):
			count += len(d[d[key[i]][j]])
	return count
print(solution(list(map(int,input().split()))))
