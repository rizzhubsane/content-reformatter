# prompts.py
PLATFORM_PROMPTS = {
    "Medium": """
You are a professional content writer. Take the following article and rewrite it for Medium.com readers. 

- Use a narrative tone with personal storytelling
- Add a strong hook at the beginning
- Include at least one short, punchy one-line paragraph in bold
- Use subheadings, spacing, and markdown for readability
- End with a reflective or thought-provoking takeaway

Content:
{article}
""",

    "Substack": """
You are writing a newsletter issue for Substack.

Take the article below and reframe it like a warm email to a friend. 
- Start with a casual greeting or relatable moment
- Maintain clarity and conversational tone
- Break it into small paragraphs
- Add a friendly sign-off like “Until next time,” or “Thanks for reading!”

Content:
{article}
""",

    "Dev.to": """
You are writing a tutorial-style post for Dev.to.

Take the article below and reformat it into an educational, step-by-step post for beginner devs.

- Add bullet points, numbered steps, or code block hints if possible
- Keep a neutral tone, avoid over-storytelling
- Start with a clear summary of what the post will teach
- End with “Let me know what you think in the comments!”

Content:
{article}
""",

    "Ko-fi": """
You are creating a short Ko-fi post that introduces this article and encourages tips or support.

- Write a short teaser (2–3 lines) summarizing what the article is about
- Add a personal note or “why it matters”
- End with a soft CTA like “Support my writing on Ko-fi if this helped you.”

Content:
{article}
"""
}
