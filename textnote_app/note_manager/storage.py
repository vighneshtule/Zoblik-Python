import json
import os
from .note import Note

# Path is assumed to be running from the parent of note_manager/
FILE_PATH = 'notes.json'

def save_notes(notes_list):
    try:
        data = [note.save() for note in notes_list]
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving notes: {e}")
        return False

def load_notes():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                return []
            data = json.loads(content)
            return [Note.from_dict(item) for item in data]
    except json.JSONDecodeError:
        print("Error: notes.json contains invalid JSON data. Starting with an empty list.")
        return []
    except Exception as e:
        print(f"Error loading notes: {e}")
        return []
