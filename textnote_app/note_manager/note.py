from datetime import datetime

class Note:
    def __init__(self, title, content, tags, timestamp=None):
        self.title = title
        self.content = content
        self.tags = tags if isinstance(tags, list) else [tag.strip() for tag in tags.split(',')]
        self.timestamp = timestamp if timestamp else datetime.now().isoformat()

    def save(self):
        return {
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'timestamp': self.timestamp
        }

    def display(self):
        print(f"Title: {self.title}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Content: {self.content}")
        print("-" * 27)

    def matches_search(self, term):
        term = term.lower()
        if term in self.title.lower() or term in self.content.lower():
            return True
        for tag in self.tags:
            if term in tag.lower():
                return True
        return False

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['content'], data['tags'], data.get('timestamp'))
