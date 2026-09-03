import re
import json

OVERWORLD_JSON = "../assets/minecraft/polytone/dimension_modifiers/overworld.json"

with open("scripts/sky_color_inlined.mvel", "r") as file:
    sky_color_code = file.read()

sky_color_code = sky_color_code.replace("\n", "")
sky_color_code = sky_color_code.replace("   ", "")
sky_color_code = re.sub(r'/\*[\s\S]*?\*/', "", sky_color_code)

with open(OVERWORLD_JSON, "r") as file:
    overworld_modifiers = json.load(file)

overworld_modifiers["attributes_modifiers"]["minecraft:visual/sky_light_color"]["argument"] = sky_color_code

with open(OVERWORLD_JSON, "w") as file:
    json.dump(overworld_modifiers, file, indent=2)