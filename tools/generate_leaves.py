LEAF_TYPES = [
    "acacia",
    "azalea",
    "birch",
    "cherry",
    "dark_oak",
    "flowering_azalea",
    "jungle",
    "mangrove",
    "oak",
    "pale_oak",
    "spruce"
]

leaves_mcmeta = """{
    "texture": {
        "mipmap_strategy": "cutout"
    }
}"""

leaves_mcmeta_1122 = """{
  "texture": {
      "mipmap_strategy": "mean"
  }
}"""

# This should probably be more elegant
def generate_mcmeta_rpo(leaf_type):
    return """{
    condition: "style16",
    fallback: "1122_""" + leaf_type + """_leaves.png.mcmeta"
}"""


for leaf_type in LEAF_TYPES:
    with open(f"../assets/minecraft/textures/block/{leaf_type}_leaves.png.mcmeta", "w") as file:
        file.write(leaves_mcmeta)
    
    with open(f"../assets/minecraft/textures/block/1122_{leaf_type}_leaves.png.mcmeta", "w") as file:
        file.write(leaves_mcmeta_1122)

    with open(f"../assets/minecraft/textures/block/{leaf_type}_leaves.png.mcmeta.rpo", "w") as file:
        file.write(generate_mcmeta_rpo(leaf_type))