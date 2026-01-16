"""One-off script to create initial Sketch objects."""
from sketches.models import Sketch


def create_initial_sketches():
    """Create initial Sketch objects from the existing TS files."""
    sketches_data = [
        ("lotus", "Lotus"),
        ("sawtooth", "Sawtooth"),
        ("neural-chatgpt", "Neural ChatGPT"),
        ("neural-claude", "Neural Claude"),
        ("lins-with-patterns", "Lins with Patterns"),
    ]
    
    created_count = 0
    for slug, name in sketches_data:
        if not Sketch.objects.filter(slug=slug).exists():
            Sketch.objects.create(name=name, slug=slug)
            created_count += 1
    return created_count


if __name__ == "__main__":
    count = create_initial_sketches()
    print(f"Created {count} sketches.")
