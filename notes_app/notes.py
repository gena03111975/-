import json
import os

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

def add_note(notes_list, note):
    notes_list.append(note)

def read_notes(notes_list):
    for note in notes_list:
        print(f"ID: {note.note_id}, Заголовок: {note.title}, Тело: {note.body}, Дата/время: {note.timestamp}")

def edit_note(notes_list, note_id, new_title, new_body):
    for note in notes_list:
        if note.note_id == note_id:
            note.title = new_title
            note.body = new_body
            break

def delete_note(notes_list, note_id):
    notes_list[:] = [note for note in notes_list if note.note_id != note_id]

def save_notes_to_json(notes_list, filename):
    with open(filename, 'w') as file:
        json.dump([note.__dict__ for note in notes_list], file, indent=4)

def main():
    notes = []
    while True:
        command = input("Введите команду (add/read/exit): ")
        if command == "add":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            timestamp = "2024-07-05 16:30:00"  # Здесь можно использовать текущее время
            new_note = Note(note_id=len(notes) + 1, title=title, body=body, timestamp=timestamp)
            add_note(notes, new_note)
            print("Заметка успешно сохранена")
        elif command == "read":
            read_notes(notes)
        elif command == "exit":
            break
        else:
            print("Неверная команда. Попробуйте снова.")

    # Укажите полный путь к файлу notes.json
    save_notes_to_json(notes, os.path.join(os.getcwd(), "notes.json"))

if __name__ == "__main__":
    main()
