
import yaml
import bibtexparser
import os

def format_author(authors):
    """Formats a list of authors to 'F. Lastname'."""
    formatted_authors = []
    for author in authors:
        parts = author.split(', ')
        if len(parts) == 2:
            last_name, first_name = parts
            # Take only the first initial.
            first_initial = first_name.split(' ')[0][0]
            formatted_authors.append(f"{first_initial}. {last_name}")
        else:
            # Fallback for unexpected author formats
            formatted_authors.append(author)
    return ", ".join(formatted_authors)

def main():
    bib_file_path = 'scripts/own-bib.bib'
    output_file_path = '_data/publications.yml'

    try:
        with open(bib_file_path, 'r', encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
    except FileNotFoundError:
        print(f"Error: '{bib_file_path}' not found.")
        return

    publications = {
        'journals': [],
        'conferences': []
    }

    for entry in bib_database.entries:
        pub_type = entry.get('ENTRYTYPE', '').lower()

        # Basic filtering for required fields
        if not all(k in entry for k in ['title', 'author', 'year']):
            print(f"Skipping entry missing essential fields: {entry.get('ID', 'N/A')}")
            continue

        authors = entry['author'].split(' and ')
        # Custom formatting for a specific author if needed
        # authors = [f"<strong>{author}</strong>" if "YourLastName" in author else author for author in authors]
        
        formatted_entry = {
            'year': entry['year'],
            'title': entry['title'].replace('{', '').replace('}', ''),
            'authors': ", ".join(authors),
            'journal': entry.get('journal', entry.get('booktitle', 'N/A')),
            'url': entry.get('url', '#'),
            'abstract': entry.get('abstract', 'No abstract available.')
        }

        if pub_type == 'article':
            publications['journals'].append(formatted_entry)
        elif pub_type in ['inproceedings', 'conference']:
            publications['conferences'].append(formatted_entry)
        # You can add more rules for other entry types here

    # Sort publications by year (descending)
    publications['journals'].sort(key=lambda x: x['year'], reverse=True)
    publications['conferences'].sort(key=lambda x: x['year'], reverse=True)

    try:
        with open(output_file_path, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(publications, yaml_file, allow_unicode=True, default_flow_style=False, sort_keys=False)
        print(f"Successfully updated '{output_file_path}' with entries from '{bib_file_path}'.")
    except IOError:
        print(f"Error: Could not write to '{output_file_path}'.")

if __name__ == '__main__':
    main()
