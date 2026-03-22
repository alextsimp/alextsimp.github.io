import yaml
import os
from scholarly import scholarly
from scholarly.proxies import ScraperAPI

# --- ScraperAPI Proxy Setup ---
# Get the API key from the environment variable
api_key = os.environ.get('SCRAPER_API_KEY')
if not api_key:
    print("Error: SCRAPER_API_KEY environment variable not set.")
    exit(1)

# Set up the proxy generator
print("Setting up ScraperAPI as the proxy...")
scraper = ScraperAPI(api_key)
scholarly.use_proxy(scraper)
# --- End Proxy Setup ---

# The user ID from the Google Scholar URL
scholar_id = '4jir8zYAAAAJ'
output_file = '_data/publications.yml'


def get_scholar_publications():
    """Fetches publications from Google Scholar and returns them."""
    print(f"Fetching publications for author ID: {scholar_id}")
    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(author, sections=['publications'])
    
    # Fill each publication with its details, including abstract and URL
    for i, pub in enumerate(author['publications']):
        print(f"Fetching details for publication {i+1}/{len(author['publications'])}: {pub['bib']['title']}")
        try:
            scholarly.fill(pub)
        except Exception as e:
            print(f"  - Could not fetch details for this publication. Error: {e}")

    print(f"Found {len(author['publications'])} publications.")
    return author['publications']

def format_publications(publications):
    """Formats the raw publication data into the desired YAML structure."""
    
    pub_list = []
    for pub in publications:
        try:
            bib = pub.get('bib', {})
            if not bib.get('title'):
                continue

            pub_type = pub.get('container_type', 'journal').lower()

            pub_list.append({
                'type': 'conference' if 'conference' in bib.get('ENTRYTYPE', '') else 'journal',
                'year': bib.get('pub_year', 'N/A'),
                'title': bib.get('title', 'No Title'),
                'authors': bib.get('author', 'N/A'),
                'journal': bib.get('venue', bib.get('booktitle', 'N/A')),
                'url': pub.get('pub_url', '#'),
                'abstract': bib.get('abstract', 'No abstract available.')
            })
        except Exception as e:
            print(f"Skipping a publication due to a formatting error: {e}")

    pub_list.sort(key=lambda x: str(x['year']), reverse=True)

    formatted_data = {
        'journals': [p for p in pub_list if p['type'] == 'journal'],
        'conferences': [p for p in pub_list if p['type'] == 'conference']
    }

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
