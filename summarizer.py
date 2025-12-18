"""
Podicals - AI Summarizer
Generates article-style summaries from podcast transcripts using Claude.
"""

import os
import json
import glob
from datetime import datetime
from anthropic import Anthropic

# Initialize Anthropic client (expects ANTHROPIC_API_KEY env var)
client = Anthropic()

SUMMARY_PROMPT = """You are a skilled writer for Podicals, a site that creates engaging article summaries of podcast episodes. Think of yourself as writing for The Ringer or Morning Brew - casual, smart, and fun to read.

Given the following podcast transcript, write an article-style summary that:

1. Has an engaging, clickable headline (not clickbait, but genuinely interesting)
2. Opens with a 2-3 sentence hook that captures what made this episode worth listening to
3. Covers 5-8 key topics or moments with 2-3 sentences each
4. Uses a conversational, friendly tone - like you're telling a friend about a podcast you just listened to
5. Includes any notable quotes or memorable moments (paraphrased or very briefly quoted)
6. Ends with a quick "Bottom line" - who should listen and why

Keep it around 500-700 words. Be accurate to what was discussed - don't make things up.

PODCAST: {podcast_name}
EPISODE TITLE: {episode_title}

TRANSCRIPT:
{transcript}

Write the article summary now:"""


class PodicalsSummarizer:
    def __init__(self, transcripts_dir="./transcripts", output_dir="./summaries"):
        self.transcripts_dir = transcripts_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def summarize_episode(self, transcript_path):
        """Generate a summary for a single episode."""
        
        # Load transcript
        with open(transcript_path, 'r', encoding='utf-8') as f:
            episode_data = json.load(f)
        
        podcast_name = episode_data.get('podcast_name', 'Unknown Podcast')
        episode_title = episode_data.get('title', 'Unknown Episode')
        transcript = episode_data.get('transcript', '')
        
        if not transcript:
            return {
                'success': False,
                'error': 'No transcript content',
                'source_file': transcript_path,
            }
        
        # Truncate transcript if too long (Claude has context limits)
        max_chars = 300000
        if len(transcript) > max_chars:
            transcript = transcript[:max_chars] + "\n\n[TRANSCRIPT TRUNCATED]"
        
        # Generate summary
        prompt = SUMMARY_PROMPT.format(
            podcast_name=podcast_name,
            episode_title=episode_title,
            transcript=transcript
        )
        
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            summary = response.content[0].text
            
            return {
                'success': True,
                'summary': summary,
                'podcast_name': podcast_name,
                'episode_title': episode_title,
                'video_id': episode_data.get('video_id'),
                'youtube_url': episode_data.get('youtube_url'),
                'upload_date': episode_data.get('upload_date'),
                'duration_seconds': episode_data.get('duration_seconds'),
                'genre': episode_data.get('genre'),
                'view_count': episode_data.get('view_count'),
                'source_file': transcript_path,
                'summarized_at': datetime.now().isoformat(),
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'source_file': transcript_path,
            }
    
    def summarize_all(self, limit=None):
        """Summarize all transcripts."""
        
        # Find all transcript files
        transcript_files = glob.glob(
            os.path.join(self.transcripts_dir, '**', '*.json'),
            recursive=True
        )
        
        # Skip the stats file
        transcript_files = [f for f in transcript_files if 'stats' not in f]
        
        if limit:
            transcript_files = transcript_files[:limit]
        
        print(f"\n{'='*60}")
        print(f"PODICALS SUMMARIZER")
        print(f"{'='*60}")
        print(f"Found {len(transcript_files)} transcripts to summarize")
        print(f"{'='*60}\n")
        
        results = []
        
        for i, filepath in enumerate(transcript_files):
            print(f"[{i+1}/{len(transcript_files)}] {os.path.basename(filepath)[:50]}...")
            
            result = self.summarize_episode(filepath)
            
            if result['success']:
                self._save_summary(result)
                print(f"  ✓ Done")
            else:
                print(f"  ✗ Error: {result.get('error')}")
            
            results.append(result)
        
        # Summary stats
        successful = sum(1 for r in results if r['success'])
        print(f"\n{'='*60}")
        print(f"COMPLETE: {successful}/{len(results)} successful")
        print(f"{'='*60}")
        
        return results
    
    def _save_summary(self, result):
        """Save a summary to the output directory."""
        
        genre = result.get('genre', 'unknown')
        podcast_name = self._sanitize_filename(result.get('podcast_name', 'unknown'))
        
        # Create directory structure
        podcast_dir = os.path.join(self.output_dir, genre, podcast_name)
        os.makedirs(podcast_dir, exist_ok=True)
        
        # Create filename
        upload_date = result.get('upload_date', 'unknown')
        title_slug = self._sanitize_filename(result.get('episode_title', 'episode')[:50])
        filename = f"{upload_date}_{title_slug}.json"
        
        filepath = os.path.join(podcast_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    
    def _sanitize_filename(self, name):
        """Remove invalid characters from filename."""
        import re
        return re.sub(r'[<>:"/\\|?*]', '', name).strip()


def export_for_website(summaries_dir="./summaries", output_file="./data/episodes.json"):
    """
    Export all summaries into a single JSON file for website consumption.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    summary_files = glob.glob(
        os.path.join(summaries_dir, '**', '*.json'),
        recursive=True
    )
    
    all_episodes = []
    
    for filepath in summary_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if data.get('success'):
                # Parse upload date for sorting
                upload_date = data.get('upload_date', '')
                if upload_date:
                    formatted_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
                else:
                    formatted_date = ''
                
                all_episodes.append({
                    'id': data.get('video_id'),
                    'podcast': data.get('podcast_name'),
                    'title': data.get('episode_title'),
                    'genre': data.get('genre'),
                    'date': formatted_date,
                    'duration_seconds': data.get('duration_seconds'),
                    'view_count': data.get('view_count'),
                    'summary': data.get('summary'),
                    'youtube_url': data.get('youtube_url'),
                })
    
    # Sort by date descending
    all_episodes.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Also create genre and podcast indexes
    genres = {}
    podcasts = {}
    
    for ep in all_episodes:
        genre = ep.get('genre', 'unknown')
        podcast = ep.get('podcast', 'unknown')
        
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(ep['id'])
        
        if podcast not in podcasts:
            podcasts[podcast] = {'genre': genre, 'episodes': []}
        podcasts[podcast]['episodes'].append(ep['id'])
    
    # Save everything
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'episodes': all_episodes,
            'genres': genres,
            'podcasts': podcasts,
            'total_count': len(all_episodes),
            'exported_at': datetime.now().isoformat(),
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"EXPORT COMPLETE")
    print(f"{'='*60}")
    print(f"Episodes: {len(all_episodes)}")
    print(f"Genres: {len(genres)}")
    print(f"Podcasts: {len(podcasts)}")
    print(f"Output: {output_file}")
    print(f"{'='*60}")
    
    return all_episodes


if __name__ == "__main__":
    # Summarize all transcripts
    summarizer = PodicalsSummarizer()
    summarizer.summarize_all()
    
    # Export for website
    export_for_website()
