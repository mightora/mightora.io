#!/usr/bin/env python3
from pathlib import Path
import re
from urllib.parse import urlparse
root=Path(__file__).resolve().parents[1]
s=(root/'data/toolhub.yaml').read_text()
urls=re.findall(r'^\s+url: (https://[^\s]+)',s,re.M)
expected={'power-bi-diff','semantic-model','powerbi-inspector','dax','solution-explorer','rest','fetchflow','expression-lab','har','architecture-lab','code-diff','qr','radar','connect','roadmaps','beta.slides','feedback'}
got={urlparse(u).hostname.removesuffix('.mightora.io') for u in urls}
assert len(urls)==17 and len(set(urls))==17,(len(urls),len(set(urls)))
assert got==expected,got^expected
assert len(re.findall(r'^\s+- id: ',s,re.M))==6
for p in ('content/_index.md','content/tools/_index.md'):
 assert '{{< tool-hub >}}' in (root/p).read_text(),p
assert (root/'data/footer.yaml').read_text()==(root/'static/footer.yaml').read_text()
print('PASS: 17 external URLs, 6 categories, both pages and footer sync')

h=(root/'layouts/shortcodes/tool-hub.html').read_text(encoding='utf8')
for label in ('Build','Inspect','Architect','Deploy'):
 assert f'<strong>{label}</strong>' in h, label
assert 'THE ORIGINAL COLLECTION' not in h
assert 'Original Power Platform tools' not in h
assert 'id="mt-platform-resources"' in h
for anchor in ('#power-platform','#diagnostics','#architecture','#mt-platform-resources'):
 assert f'href="{anchor}"' in h, anchor
footer=(root/'layouts/partials/footer.html').read_text(encoding='utf8')
assert '<mightora-author>' in footer
assert '<section class="mt-author-wrapper"' in footer
assert 'author-avatar' in footer and 'author-blog-logo' in footer
print('PASS: four developer journeys and responsive author component')
