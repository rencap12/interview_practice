# hi this is reneca
#h
"""
def filter_sustainable_brands(brands, criterion):
    res = []
    for brand in brands:
        
        name = brand['name']
        if criterion in brand['criteria']:
            res.append(name)

    return res

'''''''''
Time: 
The in operator on a list is O(m) where m = len(criteria) (worst-case scans whole list).
O(n · m)
	•	Space: O(n)



brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))

def count_material_usage(brands): # still O n*m
    counter = {}

    for brand in brands:
        curr_materials = brand["materials"]
        for material in curr_materials:
            if material in counter:
                counter[material] += 1
            else:
                counter[material] = 1

    return counter

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))


def find_trending_materials(brands):
    mp = count_material_usage(brands)
    res = []
    for key, val in mp.items(): # O n  ?
        if val >= 2:
            res.append(key)
    return res

def find_trending_materials(brands): # O n * m ?
    seen = set()
    trending = set()
    for brand in brands:
        for material in brand["materials"]:
            if material in seen:
                trending.add(material)
            else:
                seen.add(material)
    return list(trending)



brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))
"""
def find_best_fabric_pair(fabrics, budget):
    """
    currentMax = 0
    for tuple in fabrics:
        tuple[0] # name
        tuple[1] # cost
    """
    if len(fabrics) < 2:
        return None
# whaaaaa, lmao it was fun, best of luck!!!
    # Sort by cost (ascending). If you can mutate input, use fabrics.sort(key=...)
    items = sorted(fabrics, key=lambda x: x[1])

    l, r = 0, len(items) - 1
    best_sum = -1
    best_pair = None

    while l < r:
        cost = items[l][1] + items[r][1]
        if cost > budget:
            r -= 1                     # too expensive → try cheaper right
        else:
            if cost > best_sum:        # viable and better than current best
                best_sum = cost
                best_pair = (items[l][0], items[r][0])
            l += 1                     # try to increase sum a bit
    return best_pair
    
    
fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))