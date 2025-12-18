"""
Podicals - Podcast Transcript Scraper
Pulls transcripts from YouTube for top podcasts across genres.
Target: 500 episodes for MVP
"""

import os
import json
import time
from datetime import datetime, timedelta
from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL
import re


# Top 5 podcasts by genre from Apple Podcasts charts + Joe Rogan
# YouTube channel handles for scraping
PODCASTS_BY_GENRE = {
    "comedy": [
        {"name": "The Joe Rogan Experience", "youtube_channel": "@joerogan"},
        {"name": "Call Her Daddy", "youtube_channel": "@callherdaddy"},
        {"name": "Kill Tony", "youtube_channel": "@KillTony"},
        {"name": "Flagrant", "youtube_channel": "@Flagrant2"},
        {"name": "Bad Friends", "youtube_channel": "@BadFriends"},
    ],
    "news_politics": [
        {"name": "The Daily", "youtube_channel": "@NYTimes"},
        {"name": "Pod Save America", "youtube_channel": "@PodSaveAmerica"},
        {"name": "The Ben Shapiro Show", "youtube_channel": "@BenShapiro"},
        {"name": "The Megyn Kelly Show", "youtube_channel": "@MegynKelly"},
        {"name": "Breaking Points", "youtube_channel": "@BreakingPoints"},
    ],
    "business": [
        {"name": "The Diary of a CEO", "youtube_channel": "@TheDiaryOfACEO"},
        {"name": "The All-In Podcast", "youtube_channel": "@alaboratory"},
        {"name": "My First Million", "youtube_channel": "@MyFirstMillionPod"},
        {"name": "How I Built This", "youtube_channel": "@HowIBuiltThis"},
        {"name": "The Tim Ferriss Show", "youtube_channel": "@timferriss"},
    ],
    "health_fitness": [
        {"name": "Huberman Lab", "youtube_channel": "@hubaboratorylab"},
        {"name": "The Mel Robbins Podcast", "youtube_channel": "@melrobbins"},
        {"name": "The Peter Attia Drive", "youtube_channel": "@PeterAttiaMD"},
        {"name": "On Purpose with Jay Shetty", "youtube_channel": "@JayShettyPodcast"},
        {"name": "Zoe Science & Nutrition", "youtube_channel": "@zaboratorehealth"},
    ],
    "true_crime": [
        {"name": "Crime Junkie", "youtube_channel": "@CrimeJunkie"},
        {"name": "Morbid", "youtube_channel": "@maboratorbidpodcast"},
        {"name": "Serial", "youtube_channel": "@serialpodcast"},
        {"name": "Casefile True Crime", "youtube_channel": "@CasefilePresents"},
        {"name": "My Favorite Murder", "youtube_channel": "@myfavoritemurder"},
    ],
    "sports": [
        {"name": "New Heights with Jason & Travis Kelce", "youtube_channel": "@NewHeightShow"},
        {"name": "The Pat McAfee Show", "youtube_channel": "@PatMcAfeeShow"},
        {"name": "Pardon My Take", "youtube_channel": "@PardonMyTake"},
        {"name": "The Bill Simmons Podcast", "youtube_channel": "@TheBillSimmonsPodcast"},
        {"name": "Spittin' Chiclets", "youtube_channel": "@spaboratoritinchiclets"},
    ],
    "technology": [
        {"name": "Lex Fridman Podcast", "youtube_channel": "@lexfridman"},
        {"name": "Acquired", "youtube_channel": "@AcquiredFM"},
        {"name": "Hard Fork", "youtube_channel": "@hardfaboratork"},
        {"name": "All-In Podcast", "youtube_channel": "@alaboratory"},
        {"name": "Darknet Diaries", "youtube_channel": "@JackRhysider"},
    ],
    "society_culture": [
        {"name": "Armchair Expert with Dax Shepard", "youtube_channel": "@ArmchairExpertPod"},
        {"name": "SmartLess", "youtube_channel": "@SmartLess"},
        {"name": "We Can Do Hard Things", "youtube_channel": "@wecandohardthings"},
        {"name": "Stuff You Should Know", "youtube_channel": "@StuffYouShouldKnow"},
        {"name": "Freakonomics Radio", "youtube_channel": "@Freakonomics"},
    ],
    "education": [
        {"name": "The Jordan B. Peterson Podcast", "youtube_channel": "@JordanBPeterson"},
        {"name": "Hidden Brain", "youtube_channel": "@HiddenBrain"},
        {"name": "Radiolab", "youtube_channel": "@Radiolab"},
        {"name": "TED Talks Daily", "youtube_channel": "@TED"},
        {"name": "Making Sense with Sam Harris", "youtube_channel": "@samharrisorg"},
    ],
    "history": [
        {"name": "Hardcore History", "youtube_channel": "@dancaraboratolin"},
        {"name": "The Rest is History", "youtube_channel": "@restishistory"},
        {"name": "History That Doesn't Suck", "youtube_channel": "@HistoryThatDoesntSuck"},
        {"name": "Revolutions", "youtube_channel": "@RevolutionsPodcast"},
        {"name": "American History Tellers", "youtube_channel": "@Wondery"},
    ],
}


class PodcastScraper:
    def __init__(self, output_dir="./transcripts"):
        self.output_dir = output_dir
        self.ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'ignoreerrors': True,
        }
        os.makedirs(output_dir, exist_ok=True)
        
    def get_channel_videos(self, channel_handle, max_videos=20, days_back=90):
        """
        Get recent videos from a YouTube channel.
        Returns list of video IDs and metadata.
        """
        channel_url = f"https://www.youtube.com/{channel_handle}/videos"
        
        ydl_opts = {
            **self.ydl_opts,
            'playlistend': max_videos,
            'extract_flat': True,
        }
        
        videos = []
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(channel_url, download=False)
                
                if result and 'entries' in result:
                    for entry in result['entries']:
                        if entry:
                            videos.append({
                                'id': entry.get('id'),
                                'title': entry.get('title'),
                                'url': entry.get('url'),
                            })
        except Exception as e:
            print(f"Error fetching channel {channel_handle}: {e}")
            
        return videos
    
    def get_video_metadata(self, video_id):
        """Get detailed metadata for a specific video."""
        url = f"https://www.youtube.com/watch?v={video_id}"
        
        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                result = ydl.extract_info(url, download=False)
                return {
                    'id': video_id,
                    'title': result.get('title'),
                    'description': result.get('description'),
                    'duration': result.get('duration'),  # in seconds
                    'upload_date': result.get('upload_date'),
                    'view_count': result.get('view_count'),
                    'channel': result.get('channel'),
                }
        except Exception as e:
            print(f"Error getting metadata for {video_id}: {e}")
            return None
    
    def get_transcript(self, video_id):
        """
        Fetch transcript for a YouTube video.
        Tries manual captions first, falls back to auto-generated.
        """
        try:
            # New API requires instantiation
            ytt_api = YouTubeTranscriptApi()
            
            # List available transcripts to check type
            transcript_list = ytt_api.list(video_id)
            
            # Prefer manual transcripts
            is_auto = True
            try:
                transcript = transcript_list.find_manually_created_transcript(['en'])
                is_auto = False
            except:
                # Fall back to auto-generated
                transcript = transcript_list.find_generated_transcript(['en'])
            
            # Fetch the actual transcript data
            transcript_data = transcript.fetch()
            
            # Combine into full text (new API uses .text attribute)
            full_text = ' '.join([entry.text for entry in transcript_data])
            
            # Convert to dict format for storage
            segments = [{'text': entry.text, 'start': entry.start, 'duration': entry.duration} 
                       for entry in transcript_data]
            
            return {
                'success': True,
                'transcript': full_text,
                'segments': segments,
                'is_auto_generated': is_auto,
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
            }
    
    def is_podcast_episode(self, title, duration):
        """
        Filter to identify actual podcast episodes vs clips/shorts.
        Podcasts are typically 20+ minutes.
        """
        if duration and duration < 1200:  # Less than 20 minutes
            return False
        
        # Filter out common non-episode patterns
        skip_patterns = [
            r'#shorts',
            r'\bclip\b',
            r'\bhighlight\b',
            r'\btrailer\b',
            r'\bteaser\b',
            r'\bpreview\b',
            r'\breaction\b',
        ]
        
        title_lower = title.lower() if title else ""
        for pattern in skip_patterns:
            if re.search(pattern, title_lower):
                return False
                
        return True
    
    def scrape_podcast(self, podcast_name, youtube_channel, genre, episodes_per_show=10):
        """
        Scrape transcripts for a single podcast.
        """
        print(f"\n{'='*60}")
        print(f"Scraping: {podcast_name}")
        print(f"Channel: {youtube_channel}")
        print(f"{'='*60}")
        
        # Create directory for this podcast
        podcast_dir = os.path.join(self.output_dir, genre, self._sanitize_filename(podcast_name))
        os.makedirs(podcast_dir, exist_ok=True)
        
        # Get recent videos
        videos = self.get_channel_videos(youtube_channel, max_videos=episodes_per_show * 3)
        print(f"Found {len(videos)} videos")
        
        episodes_saved = 0
        
        for video in videos:
            if episodes_saved >= episodes_per_show:
                break
                
            video_id = video['id']
            if not video_id:
                continue
            
            # Get detailed metadata
            metadata = self.get_video_metadata(video_id)
            if not metadata:
                continue
            
            # Check if it's a real episode (not a clip)
            if not self.is_podcast_episode(metadata['title'], metadata.get('duration')):
                print(f"  Skipping (not full episode): {metadata['title'][:50]}...")
                continue
            
            # Get transcript
            print(f"  Fetching: {metadata['title'][:50]}...")
            transcript_result = self.get_transcript(video_id)
            
            if not transcript_result['success']:
                print(f"    No transcript available: {transcript_result.get('error', 'Unknown error')}")
                continue
            
            # Save episode data
            episode_data = {
                'podcast_name': podcast_name,
                'genre': genre,
                'video_id': video_id,
                'title': metadata['title'],
                'description': metadata.get('description', ''),
                'duration_seconds': metadata.get('duration'),
                'upload_date': metadata.get('upload_date'),
                'view_count': metadata.get('view_count'),
                'transcript': transcript_result['transcript'],
                'is_auto_generated': transcript_result['is_auto_generated'],
                'youtube_url': f"https://youtube.com/watch?v={video_id}",
                'scraped_at': datetime.now().isoformat(),
            }
            
            # Save to file
            filename = f"{metadata.get('upload_date', 'unknown')}_{self._sanitize_filename(metadata['title'][:50])}.json"
            filepath = os.path.join(podcast_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(episode_data, f, indent=2, ensure_ascii=False)
            
            episodes_saved += 1
            print(f"    Saved! ({episodes_saved}/{episodes_per_show})")
            
            # Be nice to YouTube
            time.sleep(1)
        
        return episodes_saved
    
    def scrape_all(self, episodes_per_show=10, target_total=500):
        """
        Scrape all podcasts across all genres.
        """
        total_episodes = 0
        stats = {
            'by_genre': {},
            'by_podcast': {},
            'total': 0,
            'started_at': datetime.now().isoformat(),
        }
        
        # Calculate episodes per show to hit target
        total_podcasts = sum(len(podcasts) for podcasts in PODCASTS_BY_GENRE.values())
        episodes_per = max(5, target_total // total_podcasts)
        
        print(f"\n{'='*60}")
        print(f"PODICALS SCRAPER")
        print(f"{'='*60}")
        print(f"Podcasts: {total_podcasts}")
        print(f"Target: {target_total} episodes ({episodes_per} per show)")
        print(f"Output: {self.output_dir}")
        print(f"{'='*60}\n")
        
        for genre, podcasts in PODCASTS_BY_GENRE.items():
            stats['by_genre'][genre] = 0
            print(f"\n>>> GENRE: {genre.upper()}")
            
            for podcast in podcasts:
                if total_episodes >= target_total:
                    break
                    
                try:
                    count = self.scrape_podcast(
                        podcast['name'],
                        podcast['youtube_channel'],
                        genre,
                        episodes_per_show=episodes_per
                    )
                    
                    stats['by_podcast'][podcast['name']] = count
                    stats['by_genre'][genre] += count
                    total_episodes += count
                    
                except Exception as e:
                    print(f"Error scraping {podcast['name']}: {e}")
                    stats['by_podcast'][podcast['name']] = 0
                
                # Pause between podcasts
                time.sleep(2)
            
            if total_episodes >= target_total:
                break
        
        stats['total'] = total_episodes
        stats['completed_at'] = datetime.now().isoformat()
        
        # Save stats
        stats_path = os.path.join(self.output_dir, 'scrape_stats.json')
        with open(stats_path, 'w') as f:
            json.dump(stats, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"SCRAPING COMPLETE")
        print(f"Total episodes: {total_episodes}")
        print(f"Stats saved to: {stats_path}")
        print(f"{'='*60}")
        
        return stats
    
    def _sanitize_filename(self, name):
        """Remove invalid characters from filename."""
        return re.sub(r'[<>:"/\\|?*]', '', name).strip()


if __name__ == "__main__":
    scraper = PodcastScraper(output_dir="./transcripts")
    
    # Scrape target of 500 episodes
    stats = scraper.scrape_all(target_total=500)
    
    print("\nEpisodes by genre:")
    for genre, count in stats['by_genre'].items():
        print(f"  {genre}: {count}")
