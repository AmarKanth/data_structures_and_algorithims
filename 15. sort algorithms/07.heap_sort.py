def heapify(custom_list, n, i):
	smallest = i
	l = 2*i + 1
	r = 2*i + 2
	
	if l < n and custom_list[l] < custom_list[smallest]:
		smallest = l

	if r < n and custom_list[r] < custom_list[smallest]:
		smallest = r

	if smallest != i:
		custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
		heapify(custom_list, n, smallest)

"""
TimeComplexity O(NLogN)
SpaceComplexity O(1)
"""
def heap_sort(custom_list):
	n = len(custom_list)

	for i in range(int(n/2)-1, -1, -1):
		heapify(custom_list, n, i)

	for i in range(n-1, 0, -1):
		custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
		heapify(custom_list, i, 0)
	return custom_list

res = heap_sort([2,1,7,6,5,3,4,9,8])
print(res)