import zipfile
from pathlib import Path

output_path = Path("../build/true-classic.zip")
sources = ["../assets", "../style_164", "../pack.mcmeta", "../pack.png"]

with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for source in sources:
        source = Path(source).resolve()
        if (source.is_file()):
            zip_file.write(source, arcname=source.name)
        else:
            for file in source.rglob("*"):
                if (file.is_file()):
                    zip_file.write(file, file.relative_to(source.parent))
