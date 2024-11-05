# 3-dimensional associative array for RSS url
rss_data = {
    'bbc_news': {
        'top_stories': {
            'top_stories': 'https://feeds.bbci.co.uk/news/rss.xml',
        },
        'world_news': {
            'world': 'https://feeds.bbci.co.uk/news/world/rss.xml',
            'africa': 'https://feeds.bbci.co.uk/news/world/africa/rss.xml',
            'asia': 'https://feeds.bbci.co.uk/news/world/asia/rss.xml',
            'europe': 'https://feeds.bbci.co.uk/news/world/europe/rss.xml',
            'latin_america': 'https://feeds.bbci.co.uk/news/world/latin_america/rss.xml',
            'middle_east': 'https://feeds.bbci.co.uk/news/world/middle_east/rss.xml',
            'us_anada': 'https://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml',
        },
        'uk_news': {
            'uk': 'https://feeds.bbci.co.uk/news/uk/rss.xml',
            'england': 'https://feeds.bbci.co.uk/news/england/rss.xml',
            'northern_ireland': 'https://feeds.bbci.co.uk/news/northern_ireland/rss.xml',
            'scotland': 'https://feeds.bbci.co.uk/news/scotland/rss.xml',
            'wales': 'https://feeds.bbci.co.uk/news/wales/rss.xml'
        },
        'business_news':{
            'business': 'https://feeds.bbci.co.uk/news/business/rss.xml'
        },
        'politics_news': {
            'politics': 'https://feeds.bbci.co.uk/news/politics/rss.xml'
        },
        'health_news': {
            'health': 'https://feeds.bbci.co.uk/news/health/rss.xml'
        },
        'science_environment_news': {
            'science_and_environment': 'https://feeds.bbci.co.uk/news/science_and_environment/rss.xml'
        },
        'technology_news': {
            'technology': 'https://feeds.bbci.co.uk/news/technology/rss.xml'
        },
        'entertainment_arts_news': {
            'entertainment_and_arts': 'https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml'
        },
        'special_categories': {
            'have_your_say': 'https://feeds.bbci.co.uk/news/have_your_say/rss.xml',
            'magazine': 'https://feeds.bbci.co.uk/news/magazine/rss.xml',
            'in_pictures': 'https://feeds.bbci.co.uk/news/in_pictures/rss.xml',
            'the_reporters': 'https://feeds.bbci.co.uk/news/reporters/rss.xml'
        },
        'most_read_most_watched': {
            'most_read': 'https://feeds.bbci.co.uk/news/rss.xml?edition=uk#most_read',
            'most_watched': 'https://feeds.bbci.co.uk/news/rss.xml?edition=uk#most_watched'
        }
    }
}

# Looping through the 3-dimensional associative array and printing data
for channel, category in rss_data.items():
    print(f"Channel: {channel}")
    for category_name, news in category.items():
        print(f"Category: {category_name}")
        for key, value in news.items():
            print(f"    {key.capitalize()}: {value}")