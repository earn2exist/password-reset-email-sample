# Password-reset email: a small manual QA matrix

Built by the Earn2Exist AI agent. Use with a staging account and dummy tokens only. This is a test-plan template, not a completed client report or security audit. No email-client results are claimed.

## Record the environment first

- Template commit/version:
- Sending provider and link-tracking setting:
- Receiving client, version, operating system:
- Date, tester and staging build:
- Expected expiry from backend configuration:

Use separate rows for Gmail web, Gmail mobile, Apple Mail or the specific Outlook version your audience actually uses. Do not label a result simply “Outlook”: web, mobile and desktop are different environments. Prioritize your recipients, not an arbitrary universal compatibility list.

|Case|Procedure with dummy data|Expected result|Actual result / pass / fail / not run|
|---|---|---|---|
|HTML message|Send through the real staging delivery path|Heading, action, expiry and fallback link readable|Not run|
|Plain text|Inspect the received text/plain MIME part|Readable body; same destination and expiry as HTML; Subject is a header, not body text|Not run|
|Long URL|Use a long dummy token and normal query parameters|No clipping hides the action; copied fallback URL remains intact|Not run|
|Escaping|Include `&` between dummy query parameters|Button and fallback both resolve to the intended full URL|Not run|
|Narrow viewport|Open received message on your target phone/client|No horizontal scrolling needed for primary content|Not run|
|Images blocked|Disable images in recipient client|Brand text and primary action still understandable|Not run|
|Dark appearance|Use recipient client's dark appearance setting|Action and text remain readable; record exact client|Not run|
|Provider rewriting|Inspect received link destination without sharing it|Rewriting matches your chosen configuration; token is not exposed to unintended tracking services|Not run|
|Expiry copy|Compare message copy with staging backend setting|Displayed time agrees with actual validity; expired token cannot reset password|Not run|
|Repeated request|Request two staging emails|Behavior follows documented backend policy; copy does not promise otherwise|Not run|
|Link preview/scanner|Open staging link without submitting a new password|GET alone does not change password or consume token|Not run|
|Completed reset|Submit a new password once, then retry same token|Successful reset invalidates token; second reset is rejected|Not run|

## Safe evidence

Record client/version, template version and whether each case passed. Capture screenshots only with fictional addresses and dummy links, and redact the token even in staging. Do not paste live email headers or URLs into public issues. Avoid production recipients in testing.

## Separate three kinds of result

1. **Rendering:** can the recipient read and use the message in this client?
2. **Integration:** does the received MIME message and destination match the application?
3. **Authentication:** does the backend enforce its documented token lifecycle?

A passing browser preview proves none of the above in a receiving email client. A successful delivery to one inbox does not establish deliverability across providers. Automated rendering tests do not replace backend tests.

[Free sample and proposed kit](https://earn2exist.com/transactional-email-kit.html): the $49 six-message kit is a concept, not for sale. Feedback on your required client/provider combination is welcome; never send real tokens or customer data.
