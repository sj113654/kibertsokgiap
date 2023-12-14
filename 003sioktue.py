#這是2023.09.26佮2023.10.03愛交的作業，今2023.12.14補交。

#建立一個數字串列並列印串列的長度。
lst = [2, 0, 2, 3, 1, 2, 1]
print("建立一個數字串列並列印串列的長度。")
print(lst, "長度：", len(lst))

#在串列的末尾新增一個數字並再次列印串列。
lst.append(4)
print("在串列的末尾新增一個數字並再次列印串列。")
print(lst)

#從串列中移除第一個數字並再次列印串列。
lst.pop(0)
print("從串列中移除第一個數字並再次列印串列。")
print(lst)

#將串列排序為升序並再次列印串列。
lst.sort()
print("將串列排序為升序並再次列印串列。")
print(lst)

#反轉串列並再次列印串列。
lst.reverse()
print("反轉串列並再次列印串列。")
print(lst)

#在串列中尋找一個數字的索引。
print("在串列中尋找一個數字的索引。")
print("4的索引：", lst.index(4))
#檢查一個數字是否在串列中。
print("檢查一個數字是否在串列中。")
if 5 in lst:
	print("5在串列中")
else:
	print("5不在串列中")

#取得串列的切片。
print("取得串列的切片。")
print("lst[1:4] = ", lst[1:4])

print("==========")

#建立一個數字元組並列印元組。
tp = (2, 0, 2, 3, 1, 2, 1)
print("建立一個數字元組並列印元組。")
print(tp)

#檢查一個數字是否在元組中。
print("檢查一個數字是否在元組中。")
if 5 in tp:
	print("5在元組中")
else:
	print("5不在元組中")

#取得元組的切片。
print("取得元組的切片。")
print("tp[1:4] = ", tp[1:4])

print("==========")

#建立一個數字集合並列印集合。
st = {2, 0, 2, 3, 1, 2, 1}
print("建立一個數字集合並列印集合。")
print(st)

#在集合中新增一個數字並再次列印集合。
print("在集合中新增一個數字並再次列印集合。")
st.add(4)
print(st)

#從集合中移除一個數字並再次列印集合。
print("從集合中移除一個數字並再次列印集合。")
st.remove(0)
print(st)

#檢查一個數字是否在集合中。
print("檢查一個數字是否在集合中。")
if 5 in st:
	print("5在集合中")
else:
	print("5不在集合中")

print("==========")

#建立一個名字和年齡的字典並列印字典。
d = {"Li Katsuan": 21, "Loo Kianhong": 22, "Ngoo Binghong": 23, "Lim Giapkun": 24, "Tan Kiantiong": 25}
print("建立一個名字和年齡的字典並列印字典。")
print(d)

#在字典中新增一個新的名字和年齡並再次列印字典。
d["Ngoo Itsing"] = 26
print("在字典中新增一個新的名字和年齡並再次列印字典。")
print(d)

#從字典中取得一個名字的年齡。
print("從字典中取得一個名字的年齡。")
print("Tan Kiantiong", d["Tan Kiantiong"], "歲")



