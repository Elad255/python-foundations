from pathlib import Path
p = Path("sample.txt")
p.write_text("hello\nworld\n", encoding="utf-8")
txt = p.read_text(encoding="utf-8")
assert txt.startswith("hello")


def load_tasks(db_path: Path = DEFAULT_DB) -> List[Task]:
    if not db_path.exists():
        return []
    text = db_path.read_text(encoding="utf-8", errors="ignore").strip()
    if text == "":
        return []
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("todo.json must contain a JSON list")
    tasks: List[Task] = []
    for t in data:
        if not isinstance(t, dict):
            continue
        # normalize
        tid = t.get("id", 0)
        title = t.get("title", "")
        done = bool(t.get("done", False))
        # accept only valid rows
        try:
            tid = int(tid)
        except Exception:
            continue
        if tid > 0 and isinstance(title, str) and title != "":
            tasks.append({"id": tid, "title": title, "done": done})
    return tasks




def save_tasks(tasks: List[Task], db_path: Path = DEFAULT_DB) -> None:
    text = json.dumps(tasks, indent=2, ensure_ascii=False)
    db_path.write_text(text, encoding="utf-8")




def _next_id(tasks: List[Task]) -> int:
    mx = 0
    for t in tasks:
        tid = int(t.get("id", 0))
        if tid > mx:
            mx = tid
    return mx + 1



def add_task(title: str, db_path: Path = DEFAULT_DB) -> Task:
    if not title or title.strip() == "":
        raise ValueError("title must be non-empty")
    tasks = load_tasks(db_path)
    new_task = {"id": _next_id(tasks), "title": title.strip(), "done": False}
    tasks.append(new_task)
    save_tasks(tasks, db_path)
    return new_task



def list_tasks(db_path: Path = DEFAULT_DB) -> List[Task]:
    return load_tasks(db_path)




def _find_index_by_id(tasks: List[Task], task_id: int) -> int:
    for i in range(len(tasks)):
        if int(tasks[i]["id"]) == task_id:
            return i
    return -1



def mark_done(task_id: int, db_path: Path = DEFAULT_DB) -> Task:
    tasks = load_tasks(db_path)
    idx = _find_index_by_id(tasks, task_id)
    if idx == -1:
        raise ValueError(f"Task id {task_id} not found")
    tasks[idx]["done"] = True
    save_tasks(tasks, db_path)
    return tasks[idx]



def delete_task(task_id: int, db_path: Path = DEFAULT_DB) -> None:
    tasks = load_tasks(db_path)
    idx = _find_index_by_id(tasks, task_id)
    if idx == -1:
        raise ValueError(f"Task id {task_id} not found")
    new_tasks: List[Task] = []
    for i in range(len(tasks)):
        if i != idx:
            new_tasks.append(tasks[i])
    save_tasks(new_tasks, db_path)
