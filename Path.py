from pathlib import Path
path=Path("test")
path.mkdir()
print(path.exists())
path.rmdir()
print(path.exists())