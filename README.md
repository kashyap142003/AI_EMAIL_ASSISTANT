# Email Rewriter AI

An AI-powered email rewriting tool that uses OpenRouter API to rewrite emails in different tones.

## Features
- Rewrite emails in various tones (professional, casual, friendly, etc.)
- Grammar correction
- Powered by GPT-4o-mini via OpenRouter

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the parent directory:
```
OPENAI_API_KEY="your-openrouter-api-key-here"
```

4. Get your API key from [OpenRouter](https://openrouter.ai/)

5. Copy `config.example.py` to `config.py` (already done if you cloned)

## Usage

Run the main script:
```bash
python main.py
```

Enter your email text and choose a tone (e.g., professional, casual, friendly).

## Files
- `main.py` - Entry point
- `email_ai.py` - Core email rewriting logic
- `prompts.py` - Prompt templates
- `config.py` - Configuration (not tracked in git)

## Note
Never commit your `.env` file or `config.py` with real API keys!
