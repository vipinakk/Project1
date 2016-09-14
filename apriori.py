def powerset(s):
    n = len(s)
    masks = [1<<j for j in xrange(n)]
    for i in xrange(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]


trans1=open('test.txt','r')
lines=trans1.readlines()
item_count = {}		# dict to store item(s) and their frequency
all_freq_item_sup_cnt = {}
print lines
for line in lines:
	line = line.strip()		#strip off extra spaces at the ends
	line = line.replace('\n','')	#replace new line by empty string
	items = line.split(',')		#split the comma separated transaction into individual items
	for item in items:
		item = item.strip()	#strip off extra space(if any)
		if item in item_count:	
			item_count[item]= item_count[item]+1	#counting the frequency of each item
		else:
			item_count[item]=1
print item_count

min_sup = input('Enter the minimum support')
min_conf = input('Enter the minimum confidence')
print min_sup,min_conf
sup_count = {}					# dict to store the support count in % of each item(s)
for item in item_count:
	sup_count[item]=item_count[item]/float(len(lines))*100	#compute and store support count
print sup_count
freq_item = []						#list to store frequent itemset
for item in sup_count:
	if sup_count[item] >= min_sup:			#comparing support count with minimum support and finding frequent 1-itemset.
		freq_item.append(str(item))
		all_freq_item_sup_cnt[str(item)] = sup_count[item]
freq_item = sorted(freq_item)
print freq_item


r = 0
while len(freq_item) is not 0:				#loop until there are no more frequent items
	print "*******************************************"
	item_count = {}
	sup_count = {}
	for i in range(0,len(freq_item)-1):
		for j in range(i+1, len(freq_item)):
			s1 = freq_item[i].split(',')	#separate items in frequent item set and store in an array
			s2 = freq_item[j].split(',')
			s3 = [k for k in s1 if k in s2]		#checking for common items in s1 and s2
			if len(s3) == r:
				s3 = set(s1).union(set(s2))	#union of s1 and s2
				s4 = list(s3)
				key = str(s4[0])		#make a string out of the list s4
				for k in range(1,len(s4)):
					key = key + ',' + s4[k]
				if key not in item_count:	#removing duplicates in candidate k-itemset
					item_count[key] = 0
	
	for line in lines:				#checking for each transaction the number of times the candidate k-itemset appears
		line = line.strip()
		line = line.replace('\n','')
		items = line.split(',')
		for key in item_count:
			s3 = key.split(',')
			if set(s3).issubset(set(items)):	#calculating the frequency of candidate k-itemset
				item_count[key] = item_count[key] + 1
	if len(item_count) is not 0:				#printing the frequency of candidate k-itemset				
		print item_count	
	for item in item_count:					#calculate the support count of candidate k-itemset
		sup_count[item] = item_count[item]/float(len(lines))*100
	if len(sup_count) is not 0:
		print sup_count
	freq_item = []
	for item in sup_count:					#calculate frequent k-itemsets
		if sup_count[item] >= min_sup:
			freq_item.append(str(item))
			all_freq_item_sup_cnt[str(item)] = sup_count[item]
	if len(freq_item) is not 0:
		freq_item = sorted(freq_item)
		print freq_item
	for item in freq_item:
		items = item.split(',')
		for s in powerset(items):
			if (len(list(s)) is not 0 and len(list(s)) is not len(items)):
				rh_list = list(set(items).difference(set(s)))
				#print s
				s = sorted(list(s))
				rh_list = sorted(rh_list)
				lh = str(s[0])
				for i in range(1,len(s)):
					lh = lh + ',' + s[i]
				rh = str(rh_list[0])
				for i in range(1,len(rh_list)):
					rh = rh + ',' + rh_list[i]
				if lh in all_freq_item_sup_cnt:
					conf = all_freq_item_sup_cnt[item] / all_freq_item_sup_cnt[lh]*100
				if conf >= min_conf:
					print lh+'-->'+rh
	r = r + 1

print all_freq_item_sup_cnt











		















