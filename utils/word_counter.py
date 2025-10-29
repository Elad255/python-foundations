
from collections import Counter
from pathlib import Path
import re
from typing import Tuple, List


WORD_RE = re.compile(r"\b[\w']+\b", flags=re.UNICODE)



def count_words(path: str | Path) -> Tuple[int, Counter]:
    
    
    p = Path(path)

    if not p.exists() or not p.is_file():
      raise FileNotFoundError(f"No such file: {p}")

    text=p.read_text(encoding="utf-8",errors="ignore")

    words=[w.lower() for w in WORD_RE.findall(text)]
  
    return len(words), Counter(words)



def top_n(counter: Counter, n: int = 5) -> List[tuple[str, int]]:
    

    if n < 1:
        raise ValueError("n must be >= 1")
    

    return counter.most_common(n)
 



if __name__ == "__main__":  # pragma: no cover
    # simple CLI demo 

    
    file_path=input("path to text file:").strip()
    try:
        total,freqs=count_words(file_path)
        print(f"Total words: {total}")
        for word,cnt in top_n(freqs,10):
            print(f"{word}:{cnt}")
    except FileNotFoundError as e:
        print (e)
