from pathlib import Path

BLOCKSTATES_FOLDER = Path("../assets/minecraft/blockstates/")

rpo = """{
    condition: "style16"
}"""

for file in BLOCKSTATES_FOLDER.iterdir():
        with open(f"../assets/minecraft/blockstates/{file.name}.rpo", "w") as file:
            file.write(rpo)
