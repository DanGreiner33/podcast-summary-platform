import { episodes, genres, podcasts } from '@/data/episodes'

// Helper to format genre names
function formatGenre(genre: string): string {
  return genre
    .split('_')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
}

// Helper to format duration
function formatDuration(seconds: number): string {
  const hours = Math.floor(seconds / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  if (hours > 0) {
    return `${hours}h ${minutes}m`
  }
  return `${minutes}m`
}

// Helper to format date
function formatDate(dateStr: string): string {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

export default function Home() {
  const latestEpisodes = episodes.slice(0, 6)
  const genreList = Object.keys(genres)
  
  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-b from-cream to-white py-16 md:py-24">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h1 className="font-display text-4xl md:text-6xl text-warm-black mb-6">
            Podcast summaries you can<br />
            <span className="text-accent">actually read</span>
          </h1>
          <p className="text-warm-gray text-lg md:text-xl max-w-2xl mx-auto mb-8">
            Get the highlights from your favorite podcasts in 5 minutes. 
            Stay in the conversation without spending hours listening.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a 
              href="/latest" 
              className="bg-accent hover:bg-accent-light text-white px-8 py-3 rounded-full font-medium transition-colors"
            >
              Browse Latest Episodes
            </a>
            <a 
              href="/genres" 
              className="bg-white hover:bg-gray-50 text-warm-black px-8 py-3 rounded-full font-medium border border-gray-200 transition-colors"
            >
              Explore by Genre
            </a>
          </div>
        </div>
      </section>

      {/* How it Works */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4">
          <h2 className="font-display text-3xl text-center mb-12">How it works</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-accent/10 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">📻</span>
              </div>
              <h3 className="font-semibold text-lg mb-2">We listen</h3>
              <p className="text-warm-gray">
                We pull transcripts from the biggest podcasts across every genre, every week.
              </p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-accent/10 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">✍️</span>
              </div>
              <h3 className="font-semibold text-lg mb-2">We summarize</h3>
              <p className="text-warm-gray">
                AI creates article-style summaries with the key points, moments, and takeaways.
              </p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-accent/10 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-3xl">💬</span>
              </div>
              <h3 className="font-semibold text-lg mb-2">You stay informed</h3>
              <p className="text-warm-gray">
                Read in 5 minutes what took 3 hours to record. Know enough to join any conversation.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Browse by Genre */}
      <section className="py-16">
        <div className="max-w-6xl mx-auto px-4">
          <div className="flex items-center justify-between mb-8">
            <h2 className="font-display text-3xl">Browse by genre</h2>
            <a href="/genres" className="text-accent hover:text-accent-light font-medium">
              View all →
            </a>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {genreList.map(genre => (
              <a
                key={genre}
                href={`/genre/${genre}`}
                className={`genre-${genre} p-4 rounded-xl text-center font-medium card-hover`}
              >
                {formatGenre(genre)}
                <span className="block text-sm opacity-75 mt-1">
                  {genres[genre].length} episodes
                </span>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* Latest Episodes */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4">
          <div className="flex items-center justify-between mb-8">
            <h2 className="font-display text-3xl">Latest episodes</h2>
            <a href="/latest" className="text-accent hover:text-accent-light font-medium">
              View all →
            </a>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {latestEpisodes.map(episode => (
              <a
                key={episode.id}
                href={`/episode/${episode.id}`}
                className="bg-cream rounded-xl p-6 card-hover block"
              >
                <div className="flex items-center gap-2 mb-3">
                  <span className={`genre-${episode.genre} text-xs px-2 py-1 rounded-full`}>
                    {formatGenre(episode.genre)}
                  </span>
                  {episode.duration_seconds && (
                    <span className="text-warm-gray text-xs">
                      {formatDuration(episode.duration_seconds)}
                    </span>
                  )}
                </div>
                <h3 className="font-display text-xl mb-2 line-clamp-2">
                  {episode.title}
                </h3>
                <p className="text-warm-gray text-sm mb-3">{episode.podcast}</p>
                <p className="text-warm-gray text-sm line-clamp-3">
                  {episode.summary?.slice(0, 150)}...
                </p>
                <div className="mt-4 text-accent font-medium text-sm">
                  Read summary →
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* Newsletter CTA */}
      <section className="py-16">
        <div className="max-w-3xl mx-auto px-4 text-center">
          <div className="bg-warm-black rounded-2xl p-8 md:p-12">
            <h2 className="font-display text-3xl text-white mb-4">
              Get the week's best podcasts in your inbox
            </h2>
            <p className="text-gray-400 mb-6">
              Every Sunday, we send you summaries of the top 10 podcast episodes. 
              Stay informed in 10 minutes.
            </p>
            <form className="flex flex-col sm:flex-row gap-3 max-w-md mx-auto">
              <input
                type="email"
                placeholder="your@email.com"
                className="flex-1 px-4 py-3 rounded-full bg-white/10 text-white placeholder-gray-500 border border-white/20 focus:outline-none focus:border-accent"
              />
              <button
                type="submit"
                className="bg-accent hover:bg-accent-light text-white px-6 py-3 rounded-full font-medium transition-colors whitespace-nowrap"
              >
                Subscribe
              </button>
            </form>
          </div>
        </div>
      </section>
    </div>
  )
}
