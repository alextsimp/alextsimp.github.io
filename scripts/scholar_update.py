import yaml
from scholarly import scholarly

# The user ID from the Google Scholar URL
scholar_id = '4jir8zYAAAAJ'
output_file = '_data/publications.yml'

def get_scholar_publications():
    """Fetches publications from Google Scholar and returns them."""
    print(f"Fetching publications for author ID: {scholar_id}")
    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(author, sections=['publications'])
    print(f"Found {len(author['publications'])} publications.")
    return author['publications']

def format_publications(publications):
    """Formats the raw publication data into the desired YAML structure."""
    
    # Using a list to store publications first to avoid duplicates
    pub_list = []
    for pub in publications:
        try:
            bib = pub.get('bib', {})
            # Skip publications that don't have a title
            if not bib.get('title'):
                continue

            # Default to 'journal' type if not specified
            pub_type = pub.get('container_type', 'journal').lower()

            pub_list.append({
                'type': 'conference' if 'conference' in bib.get('ENTRYTYPE', '') else 'journal',
                'year': bib.get('pub_year', 'N/A'),
                'title': bib.get('title', 'No Title'),
                'authors': bib.get('author', 'N/A'),
                'journal': bib.get('venue', bib.get('booktitle', 'N/A'))
            })
        except Exception as e:
            print(f"Skipping a publication due to an error: {e}")

    # Sort publications by year, descending
    pub_list.sort(key=lambda x: str(x['year']), reverse=True)

    # Separate into journals and conferences
    formatted_data = {
        'journals': [p for p in pub_list if p['type'] == 'journal'],
        'conferences': [p for p in pub_list if p['type'] == 'conference']
    }

    # Remove the 'type' key as it's no longer needed
    for pub in formatted_data['journals']:
        del pub['type']
    for pub in formatted_data['conferences']:
        del pub['type']

    return formatted_data

def write_to_yaml(data):
    """Writes the formatted data to the YAML file."""
    print(f"Writing {len(data['journals']) + len(data['conferences'])} publications to {output_file}")
    with open(output_file, 'w') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print("Successfully updated publications file.")

if __name__ == '__main__':
    raw_publications = get_scholar_publications()
    formatted_data = format_publications(raw_publications)
    write_to_yaml(formatted_data)
