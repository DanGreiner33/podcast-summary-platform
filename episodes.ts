// Sample episode data for development
// In production, this would be loaded from the JSON export

export interface Episode {
  id: string
  podcast: string
  title: string
  genre: string
  date: string
  duration_seconds: number
  view_count?: number
  summary: string
  youtube_url: string
}

export const episodes: Episode[] = [
  {
    id: "sample-1",
    podcast: "The Joe Rogan Experience",
    title: "Elon Musk Returns to Discuss AI, Mars, and the Future",
    genre: "comedy",
    date: "2024-12-15",
    duration_seconds: 10800,
    view_count: 15000000,
    summary: `# Elon Musk Returns for a Marathon Conversation About Everything

Joe Rogan welcomed Elon Musk back to the podcast this week for another sprawling three-hour conversation that touched on everything from artificial intelligence to the colonization of Mars—with plenty of detours along the way.

## The Big Picture on AI

Musk didn't hold back on his concerns about artificial intelligence development. He argued that we're approaching a critical juncture where AI capabilities are advancing faster than our ability to understand or control them. "We're essentially summoning a demon," he said, echoing warnings he's made before but with renewed urgency given recent developments in large language models.

## SpaceX and the Mars Timeline

On the space front, Musk was characteristically optimistic. He suggested that SpaceX could have humans on Mars within the decade, describing the red planet as "humanity's backup drive." Rogan pushed back on the timeline, pointing out that Musk's predictions have historically been... ambitious.

## Neuralink Updates

The conversation took a fascinating turn when discussing Neuralink's recent progress. Musk described watching patients with paralysis regain the ability to control devices with their thoughts as "the most meaningful thing I've ever been part of."

## The Social Media Question

Inevitably, the topic of X (formerly Twitter) came up. Musk defended his approach to content moderation, arguing that free speech—even uncomfortable speech—is essential for a functioning democracy. Rogan nodded along but raised questions about where the lines should be drawn.

## Bottom Line

This episode is essential listening for anyone interested in technology, space, or just the unique way Musk's mind works. At three hours, it's a commitment, but there's genuine substance here beyond the headlines. If you're short on time, the AI and Neuralink sections are the standouts.`,
    youtube_url: "https://youtube.com/watch?v=example1"
  },
  {
    id: "sample-2",
    podcast: "Huberman Lab",
    title: "The Science of Sleep: Tools for Better Rest",
    genre: "health_fitness",
    date: "2024-12-14",
    duration_seconds: 7200,
    view_count: 2500000,
    summary: `# Huberman Delivers the Ultimate Sleep Protocol

Andrew Huberman dedicated this week's episode to the science of sleep, and it might be his most practical episode yet. If you've been struggling with rest, this one's for you.

## The Morning Light Protocol

Huberman's number one recommendation: get sunlight in your eyes within 30-60 minutes of waking. Not through a window—actually outside. This sets your circadian rhythm and makes falling asleep later significantly easier. He spent a good twenty minutes on the science here, but the takeaway is simple.

## The Temperature Connection

Your body needs to drop its core temperature to initiate sleep. Huberman recommends keeping your bedroom cold (around 65-67°F) and taking a warm shower before bed—counterintuitively, this helps your body cool down faster afterward.

## Caffeine's Hidden Impact

Even if you fall asleep fine after afternoon coffee, caffeine disrupts your sleep architecture. Huberman suggests a hard cutoff at 2 PM, noting that caffeine has a half-life of 5-6 hours, meaning half of that 3 PM latte is still in your system at 9 PM.

## Supplements That Actually Work

Huberman walked through the evidence on magnesium (threonate specifically), theanine, and apigenin. He takes all three about 30-45 minutes before bed. He was notably skeptical of melatonin at typical doses, suggesting most supplements contain way more than the body naturally produces.

## The Wind-Down Routine

The last hour before bed should be low-light, low-stimulation. Huberman uses dim red lights and avoids screens, or uses blue-light blockers if he must. He emphasized that this isn't about being perfect—it's about being consistent.

## Bottom Line

This is Huberman at his best: actionable, science-backed advice you can implement tonight. Even if you've heard some of this before, the depth of explanation helps it stick. Worth the two hours.`,
    youtube_url: "https://youtube.com/watch?v=example2"
  },
  {
    id: "sample-3",
    podcast: "All-In Podcast",
    title: "Markets Crash, Fed Pivots, and the AI Bubble Question",
    genre: "business",
    date: "2024-12-13",
    duration_seconds: 5400,
    view_count: 1200000,
    summary: `# The Besties Debate Whether AI Is a Bubble

This week's All-In brought the heat, with the four co-hosts taking surprisingly different positions on whether we're in an AI bubble and what the Fed's recent moves mean for the economy.

## The Fed's Surprise Pivot

The episode opened with a deep dive into the Federal Reserve's latest signals. Chamath argued that the Fed is seeing something in the data that the market hasn't priced in yet—possibly early signs of a harder landing. Friedberg pushed back, suggesting the Fed is simply returning to normal after overcorrecting.

## Is AI a Bubble?

This is where things got spicy. Sacks made the case that current AI valuations are "absolutely insane" and compared the moment to 1999. Chamath countered that AI is fundamentally different because the technology actually works and is generating real revenue. Jason tried to play moderator and mostly failed.

## The Nvidia Question

All four agreed that Nvidia is the most important company in AI right now, but they disagreed wildly on valuation. The debate essentially came down to: is Nvidia a picks-and-shovels play in a gold rush, or is it building a moat that will last decades?

## Startup Market Update

The besties shared some candid observations about the current fundraising environment. Down rounds are becoming more common, and several unicorns are facing "come to Jesus" moments about their valuations. Chamath revealed he's passed on several deals recently that would have been automatic yeses two years ago.

## The TikTok Situation

A brief but interesting discussion about TikTok's uncertain future and what it means for the creator economy. Sacks thinks a ban is coming; Friedberg thinks it'll be spun off to American investors.

## Bottom Line

This is All-In at its best—smart people with different perspectives actually debating rather than just agreeing with each other. Essential listening if you're trying to understand where markets and tech are heading.`,
    youtube_url: "https://youtube.com/watch?v=example3"
  },
  {
    id: "sample-4",
    podcast: "Crime Junkie",
    title: "The Disappearance of Sarah Chen",
    genre: "true_crime",
    date: "2024-12-12",
    duration_seconds: 3600,
    view_count: 800000,
    summary: `# A Missing Persons Case That Will Haunt You

Ashley and Brit tackle one of 2024's most perplexing disappearances this week, and it's a case that has more questions than answers.

## The Night Sarah Vanished

Sarah Chen, a 28-year-old software engineer, left her San Francisco apartment on September 15th to meet a friend for dinner. She never arrived. Her phone pinged once near the Embarcadero, then went dark.

## The Investigation

Police initially treated this as a voluntary disappearance—Sarah was an adult, and there was no sign of foul play at her apartment. But her family knew something was wrong. Sarah was meticulous about communication; she wouldn't just vanish.

## The Boyfriend Question

Sarah's boyfriend of two years was quickly scrutinized, but his alibi checked out—he was at a work conference in Seattle with dozens of witnesses. Still, the hosts noted some inconsistencies in his initial statements to police that were never fully explained.

## The Digital Trail

This case is particularly interesting because of what wasn't found. Sarah's social media showed no signs of distress. Her bank accounts haven't been touched. Her passport was still in her apartment. Wherever she went—or was taken—she left her entire life behind.

## Where It Stands

The case remains open. Police recently announced they're reviewing new evidence, but haven't said what it is. Sarah's family has set up a foundation and offers a $50,000 reward for information.

## Bottom Line

This one will stick with you. The hosts handle the material sensitively while not shying away from the darker possibilities. If you have any information about Sarah Chen, the tip line is included in the episode.`,
    youtube_url: "https://youtube.com/watch?v=example4"
  },
  {
    id: "sample-5",
    podcast: "New Heights",
    title: "Chiefs Win, Eagles Drama, and Mom's Christmas Cookies",
    genre: "sports",
    date: "2024-12-11",
    duration_seconds: 4800,
    view_count: 3500000,
    summary: `# The Kelce Brothers Break Down Week 15

Jason and Travis Kelce delivered another entertaining episode that somehow managed to cover everything from playoff implications to their mom's holiday baking schedule.

## Chiefs Keep Rolling

Travis was in good spirits after another Chiefs victory, though he admitted the team isn't playing its best football right now. "We're finding ways to win, which is what matters in December," he said. Jason pushed him on whether the offense has become too predictable, leading to a surprisingly technical breakdown of route combinations.

## Eagles' Locker Room Situation

Jason addressed the elephant in the room: reports of tension in the Eagles locker room. Without naming names, he suggested that some players need to "stop talking to reporters and start talking to each other." It was as close to criticism as Jason typically gets about his own team.

## The Best NFL Defenses Right Now

Both brothers agreed that Baltimore's defense is playing at an elite level, with Travis adding that the Ravens are the team he least wants to see in the playoffs. They also gave props to Cleveland's defense despite the team's struggles on offense.

## Mom Corner

Donna Kelce called in to discuss her holiday plans, including her famous Christmas cookies that both brothers have been begging her to make. She also revealed she's been getting recognized more often at the grocery store, which she handles with good humor.

## Fantasy Football Advice

The brothers offered some start/sit advice for fantasy playoffs, though Jason admitted he's "completely checked out" of his own fantasy league after getting eliminated.

## Bottom Line

This is New Heights at its most fun—football analysis mixed with genuine family dynamics. Even if you're not a Chiefs or Eagles fan, the Kelce chemistry makes this an easy listen.`,
    youtube_url: "https://youtube.com/watch?v=example5"
  },
  {
    id: "sample-6",
    podcast: "Lex Fridman Podcast",
    title: "Sam Altman: OpenAI, GPT-5, and the Future of Intelligence",
    genre: "technology",
    date: "2024-12-10",
    duration_seconds: 14400,
    view_count: 5000000,
    summary: `# Four Hours with the Man Building AGI

Lex Fridman sat down with OpenAI CEO Sam Altman for an exhaustive conversation about artificial intelligence, the future of humanity, and everything in between.

## The State of GPT

Altman was characteristically coy about GPT-5 specifics but confirmed that the next generation represents a "significant leap" beyond current capabilities. He suggested that the improvement isn't just about the model being smarter—it's about making AI more useful in everyday contexts.

## The Safety Debate

A significant portion of the conversation focused on AI safety. Altman defended OpenAI's iterative deployment approach, arguing that releasing capable systems to the public allows for real-world learning about risks and benefits. He acknowledged critics but suggested that keeping AI development in secret labs would be far more dangerous.

## The Microsoft Partnership

Lex pushed Altman on OpenAI's relationship with Microsoft and whether it compromises the organization's mission. Altman insisted the partnership has been "net positive for humanity" by providing the compute resources needed to advance the research.

## AGI Timeline

When pressed on when we might achieve artificial general intelligence, Altman declined to give a specific year but suggested it could happen "much sooner than most people think." He defined AGI not as superhuman intelligence but as AI that can do most cognitive tasks that humans can do.

## Personal Reflections

The conversation took a philosophical turn when discussing Altman's personal life and motivations. He spoke candidly about the weight of responsibility he feels and the criticism he's faced. It was a rare vulnerable moment from someone usually laser-focused on the technical.

## Regulation and Governance

Both agreed that some form of AI regulation is needed but differed on what it should look like. Altman advocated for international coordination, while Lex expressed concerns about regulatory capture.

## Bottom Line

At four hours, this is a serious commitment. But if you want to understand where AI is heading from one of the people steering it, this conversation is essential. The safety and AGI sections alone are worth your time.`,
    youtube_url: "https://youtube.com/watch?v=example6"
  }
]

// Build genre and podcast indexes from episodes
export const genres: Record<string, string[]> = {}
export const podcasts: Record<string, { genre: string; episodes: string[] }> = {}

episodes.forEach(ep => {
  if (!genres[ep.genre]) {
    genres[ep.genre] = []
  }
  genres[ep.genre].push(ep.id)
  
  if (!podcasts[ep.podcast]) {
    podcasts[ep.podcast] = { genre: ep.genre, episodes: [] }
  }
  podcasts[ep.podcast].episodes.push(ep.id)
})
