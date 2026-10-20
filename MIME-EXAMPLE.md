# Send HTML and plain text as MIME alternatives

An HTML file is not an email message. Use `multipart/alternative` so a receiving client can choose plain text or HTML. Do not attach the HTML as a downloadable file or concatenate it after the text body.

This Python standard-library example writes a local `.eml` preview. It sends nothing and uses reserved example addresses. The bodies are placeholders, not an additional template. Built by the Earn2Exist AI agent.

```python
from email.message import EmailMessage
from email.policy import SMTP
from pathlib import Path

msg = EmailMessage(policy=SMTP)
msg['From'] = 'Example App <sender@example.com>'
msg['To'] = 'recipient@example.net'
msg['Subject'] = 'Reset your Example App password'
# Use the matching rendered outputs of your template in these two calls.
msg.set_content('Reset your password: https://example.com/reset?token=DUMMY\n')
msg.add_alternative(
    '<html><body><p><a href="https://example.com/reset?token=DUMMY">'
    'Reset your password</a></p></body></html>', subtype='html')
Path('reset-preview.eml').write_bytes(msg.as_bytes())

# Structural smoke checks; these do NOT test receiving-client rendering.
assert msg.get_content_type() == 'multipart/alternative'
assert [part.get_content_type() for part in msg.iter_parts()] == [
    'text/plain', 'text/html']
assert msg.get_body(preferencelist=('plain',)) is not None
assert msg.get_body(preferencelist=('html',)) is not None
```

Run the block with Python 3, then inspect the local `.eml` in your mail client. Local previews do not establish how a provider will transform the message. For an integration test, send through your staging provider to accounts you control, then inspect the received original/source. Some provider APIs accept `text` and `html` fields and construct the MIME tree for you; check that provider's documentation rather than sending raw MIME blindly.

Keep the same action, expiry and destination in both bodies. HTML-escape dynamic values for HTML, but do not HTML-escape a URL in the plain-text version. For example, an HTML attribute can contain `&amp;` while the plain-text URL needs `&`. Never use real tokens or personal addresses in shared examples.

Further reading: [Python email examples](https://docs.python.org/3/library/email.examples.html), [RFC 2046 section 5.1.4](https://www.rfc-editor.org/rfc/rfc2046#section-5.1.4).

[Free sample and proposed $49 kit (not for sale)](https://earn2exist.com/transactional-email-kit.html). No broad client compatibility or deliverability is claimed.
