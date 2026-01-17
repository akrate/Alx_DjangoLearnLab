## Create Book

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```
Expected Output:
```
<Book: 1984>
The book instance is successfully created in the database.
```
