from libgen_api import LibgenSearch
import sys
import json

def search(mode: str, bysearch: str):
    s = LibgenSearch()
    match mode:
        case "--author":
            author = ' '.join(sys.argv[3:])
            results = s.search_author(author)
            json_results = json.dumps(results)
            data = json.loads(json_results)
            for book in data:
                 print(f"ID: {book['ID']}, Author(s): {book['Author']}, Title: {book['Title']}, Publisher: {book['Publisher']}, Year: {book['Year']}, Pages: {book['Pages']}, Language: {book['Language']}, Size: {book['Size']}, Extension: {book['Extension']}, Mirror 1: {book['Mirror_1']}, Mirror 2: {book['Mirror_2']}, Mirror 3: {book['Mirror_3']}")
        case "--title":
            results = s.search_title(bysearch)
            json_results = json.dumps(results)
            data = json.loads(json_results)
            for book in data:
                print(f"ID: {book['ID']}, Author(s): {book['Author']}, Title: {book['Title']}, Publisher: {book['Publisher']}, Year: {book['Year']}, Pages: {book['Pages']}, Language: {book['Language']}, Size: {book['Size']}, Extension: {book['Extension']}, Mirror 1: {book['Mirror_1']}, Mirror 2: {book['Mirror_2']}, Mirror 3: {book['Mirror_3']}")
        case _:
            print(f"Invalid mode: {mode}")

operation = sys.argv[1]
mode = sys.argv[2]
bysearch = sys.argv[3]

match operation:
    case "--search":
        search(mode, bysearch)
    case _:
        print(f"Invalid operation: {operation}")
