def rewrite_prompt(email_text, tone):
    return f"""Rewrite the following email in a {tone} tone.
    Fix grammer.

    Email: {email_text}
"""

