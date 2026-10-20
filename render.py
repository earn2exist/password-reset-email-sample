"""Render the sample; URLs must come from your trusted application, not user input."""
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

def render(reset_url, minutes=30):
    parts = urlsplit(reset_url)
    if parts.scheme != 'https' or not parts.hostname or parts.username or parts.password or any(c.isspace() for c in reset_url):
        raise ValueError('Expected an absolute HTTPS URL without credentials or whitespace')
    if not isinstance(minutes, int) or isinstance(minutes, bool) or not 1 <= minutes <= 1440:
        raise ValueError('Expected expiry in minutes, 1–1440')
    root = Path(__file__).parent
    html = (root / 'reset.html').read_text().replace('{{RESET_URL}}', escape(reset_url, quote=True)).replace('{{MINUTES}}', str(minutes))
    text = (root / 'reset.txt').read_text().replace('{{RESET_URL}}', reset_url).replace('{{MINUTES}}', str(minutes))
    return html, text

if __name__ == '__main__':
    html, text = render('https://example.com/reset?token=DEMO_ONLY&source=email')
    Path('preview.html').write_text(html)
    print(text)
