#liansip_1&2.py

inv = {"索仔": 1, "火把": 6, "銀角仔": 42, "刀仔": 1, "箭": 12}
dragonLoot = ["銀角仔", "刀仔", "銀角仔", "銀角仔", "紅寶石"]

def addToInventory(inventory, addedItems):
	for a in addedItems:
		if a in inventory:
			inventory[a] += 1
		elif a not in inventory:
			inventory[a] = 1
	return inventory

def displayInventory(inv):
	sum_inventory = 0
	print("裝備：")
	for a in inv.items():
		print(a[1], a[0])
		sum_inventory += a[1]
	print("裝備總數：", sum_inventory, "\n")

displayInventory(inv)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)