# 🎙️ Podicals

**Podcast summaries you can actually read.**

Get the highlights from your favorite podcasts in 5 minutes. Stay in the conversation without spending hours listening.

---

## What is this?

Podicals is a full-stack application that:
1. **Scrapes** transcripts from top podcasts via YouTube
2. **Summarizes** them into readable articles using AI
3. **Displays** them on a clean, fast website

Think of it as The Athletic or Morning Brew, but for podcasts.

---

## Project Structure

```
podicals/
├── scraper.py          # YouTube transcript scraper
├── summarizer.py       # AI-powered summarization
├── requirements.txt    # Python dependencies
├── transcripts/        # Raw scraped transcripts
├── summaries/          # Generated summaries
├── data/               # Exported JSON for website
└── website/            # Next.js frontend
    ├── src/
    │   ├── app/        # Pages and layouts
    │   └── data/       # Episode data
    └── package.json
```

---

## Quick Start

### 1. Scrape Transcripts

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the scraper (targets ~500 episodes)
python scraper.py
```

This pulls transcripts from YouTube for the top 5 podcasts in each genre:
- Comedy (Joe Rogan, Call Her Daddy, Kill Tony, etc.)
- News & Politics (The Daily, Pod Save America, etc.)
- Business (Diary of a CEO, All-In, My First Million, etc.)
- Health & Fitness (Huberman Lab, Mel Robbins, etc.)
- True Crime (Crime Junkie, Morbid, Serial, etc.)
- Sports (New Heights, Pat McAfee, Pardon My Take, etc.)
- Technology (Lex Fridman, Acquired, Hard Fork, etc.)
- Society & Culture (Armchair Expert, SmartLess, etc.)
- Education (Jordan Peterson, Hidden Brain, etc.)
- History (Hardcore History, Rest is History, etc.)

### 2. Generate Summaries

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY=your_key_here

# Run the summarizer
python summarizer.py
```

This creates article-style summaries for each episode and exports them to `data/episodes.json`.

### 3. Run the Website

```bash
cd website

# Install dependencies
npm install

# Copy the episode data
cp ../data/episodes.json src/data/

# Start development server
npm run dev
```

Visit `http://localhost:3000` to see your site!

---

## Costs

| Step | Cost |
|------|------|
| Scraping | Free (YouTube transcripts are public) |
| Summarization | ~$0.05-0.08 per episode (Claude Sonnet) |
| 500 episodes | ~$25-40 total |
| Hosting | Free on Vercel |

---

## Deployment

### Deploy to Vercel

```bash
cd website
npm run build
npx vercel
```

### Set up automated updates

For daily/weekly updates, you can:
1. Run the scraper on a cron job (GitHub Actions, server, etc.)
2. Run the summarizer
3. Rebuild and redeploy the site

Example GitHub Action:
```yaml
name: Update Episodes
on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python scraper.py
      - run: python summarizer.py
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      - run: cp data/episodes.json website/src/data/
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: cd website && npm install && npm run build
      # Deploy to Vercel or your platform
```

---

## Customization

### Add/Remove Podcasts

Edit `PODCASTS_BY_GENRE` in `scraper.py`:

```python
"your_genre": [
    {"name": "Podcast Name", "youtube_channel": "@ChannelHandle"},
]
```

### Change Summary Style

Edit `SUMMARY_PROMPT` in `summarizer.py` to adjust tone, length, or format.

### Customize the Website

The site uses:
- **Next.js 14** - React framework
- **Tailwind CSS** - Styling
- **DM Sans / DM Serif Display** - Typography

Colors and fonts are configured in `tailwind.config.js` and `globals.css`.

---

## Legal Notes

This project creates **original summaries** of podcast content, which is legally defensible because:

- Summaries are written in our own words (not transcripts)
- They don't substitute for the original content
- They link back to the original episodes
- They arguably drive traffic to the podcasts

That said, if any podcast asks to be removed, respect the request.

---

## Roadmap Ideas

- [ ] Search functionality
- [ ] Newsletter integration (Buttondown, ConvertKit)
- [ ] "Ask questions about this episode" with AI
- [ ] User accounts and saved episodes
- [ ] RSS feed of summaries
- [ ] Mobile app

---

## License

MIT - Do whatever you want with it.

---

Built with Claude.
