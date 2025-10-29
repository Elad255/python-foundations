
from pathlib import Path
from typing import Tuple
import csv

def csv_mean(path: str | Path, column: str) -> Tuple[int, float]:

    p = Path(path)
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(f"No such file: {p}")

    count = 0
    total = 0.0
    with p.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        
        if not reader.fieldnames or column not in reader.fieldnames:
            raise KeyError(f"Missing column: {column}")


        for row in reader:
            raw = row.get(column)
            if raw is None:
                # Column exists in header, but row missing the field: treat as blank
                continue

            val = raw.strip()
            if val == "":
                # Skip empty cells
                continue

            try:
                num = float(val)
            except ValueError:
                raise ValueError(f"Non-numeric value '{val}' in column {column}")

            total += num
            count += 1

    if count == 0:
        raise ValueError(f"No numeric rows for column {column}")

    mean = total / count
    return count, mean
