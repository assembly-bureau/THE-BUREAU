import os

# Define the base path for the book project within your Obsidian vault  
base_path = "V:\\0.0 OBSIDIAN MASTER VAULT\OBSIDIAN MASTER VAULT\FINAL VAULT\\1.0 Book Projects"

# Define the chapters and their respective sections  
chapters = {
    "00 Introduction": ["Chapter Outline", "Introduction", "Main Content", "Worksheets", "Conclusion", "Key Takeaways",
                        "Additional Resources", "Reflection"],
    "01 Discover Your Archetype - A Gateway to Personalized Planning": ["Chapter Outline", "Introduction",
                                                                        "Main Content", "Worksheets", "Conclusion",
                                                                        "Key Takeaways", "Additional Resources",
                                                                        "Reflection"],
    "02 Additional Personality Assessments - Broadening Your Self-Understanding": ["Chapter Outline", "Introduction",
                                                                                   "Main Content", "Worksheets",
                                                                                   "Conclusion", "Key Takeaways",
                                                                                   "Additional Resources",
                                                                                   "Reflection"],
    # Add additional chapters as needed  
}


def create_directory(path):
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
    except Exception as e:
        print(f"Failed to create directory {path}: {e}")


def create_file(path, filename, content):
    """Create a file with specified content."""
    full_path = os.path.join(path, f"{filename}.md")
    try:
        with open(full_path, 'w') as file:
            file.write(content)
        print(f"File created: {full_path}")
    except Exception as e:
        print(f"Failed to create file {full_path}: {e}")

    # Loop through the chapters and their sections to create the structure


for chapter_title, sections in chapters.items():
    chapter_path = os.path.join(base_path, chapter_title)
    create_directory(chapter_path)

    for section in sections:
        section_content = f"# {section}\n\n"  # Basic Markdown content for the section  
        create_file(chapter_path, section, section_content)

print("Book project structure created successfully.")
