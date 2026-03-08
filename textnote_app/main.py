import sys
from note_manager import Note, save_notes, load_notes

def add_note(notes):
    title = input("Enter title: ").strip()
    if not title:
        print("Title cannot be empty. Note creation cancelled.")
        return
        
    content = input("Enter content: ").strip()
    tags_str = input("Enter tags (comma-separated): ").strip()
    tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
    
    new_note = Note(title, content, tags)
    notes.append(new_note)
    save_notes(notes)
    print("Note added successfully!")

def view_all_notes(notes):
    if not notes:
        print("No notes available.")
        return
    for note in notes:
        note.display()

def search_notes(notes):
    term = input("Enter search keyword: ").strip()
    if not term:
        print("Search keyword cannot be empty.")
        return
        
    matches = [note for note in notes if note.matches_search(term)]
    if not matches:
        print("No matches found.")
        return
    for note in matches:
        note.display()

def delete_note(notes):
    if not notes:
        print("No notes to delete.")
        return
        
    for idx, note in enumerate(notes):
        print(f"[{idx}] {note.title}")
        
    try:
        idx = int(input("Enter the index of the note to delete: ").strip())
        if 0 <= idx < len(notes):
            deleted_note = notes.pop(idx)
            save_notes(notes)
            print(f"Note '{deleted_note.title}' deleted successfully!")
        else:
            print("Invalid index. No note deleted.")
    except ValueError:
        print("Please enter a valid number. No note deleted.")

def filter_by_tag(notes):
    tag = input("Enter tag to filter by: ").strip()
    if not tag:
        print("Tag cannot be empty.")
        return
        
    matches = [note for note in notes if any(tag.lower() == t.lower() for t in note.tags)]
    if not matches:
        print(f"No notes found with tag '{tag}'.")
        return
    for note in matches:
        note.display()

def main():
    print("Loading notes...")
    notes = load_notes()
    
    while True:
        print("\n--- Modular Note-Taking Utility ---")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Filter by Tag (Bonus)")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_all_notes(notes)
        elif choice == '3':
            search_notes(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            filter_by_tag(notes)
        elif choice == '6':
            save_notes(notes)
            print("Notes saved. Exiting gracefully.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
