import logging, pytest
from utils import todo_manager
from utils.todo_manager import add_task, list_tasks, mark_done, delete_task, load_tasks

def test_add_list_and_done(tmp_path):
    db = tmp_path / "todo.json"
    add_task("Buy", db)
    add_task("Call", db)
    tasks = list_tasks(db)
    assert [t["title"] for t in tasks] == ["Buy", "Call"]
    t = mark_done(1, db)
    assert t["done"] is True

def test_delete_and_persistence(tmp_path):
    db = tmp_path / "todo.json"
    add_task("One", db)
    add_task("Two", db)
    delete_task(1, db)
    tasks = load_tasks(db)
    assert tasks == [{"id": 2, "title": "Two", "done": False}]


def test_add_task_logs(tmp_path, caplog):
    todo_manager.DEFAULT_DB = tmp_path / "todo.json"
    caplog.set_level(logging.INFO)

    todo_manager.add_task("Log me", todo_manager.DEFAULT_DB)
    assert "adding task id=" in caplog.text

    with pytest.raises(ValueError):
        todo_manager.add_task("   ", todo_manager.DEFAULT_DB)
    assert "empty title" in caplog.text