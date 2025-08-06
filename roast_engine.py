import random
from textblob import TextBlob
from roast_bank import positive_roasts, negative_roasts, neutral_roasts

def detect_sentiment(text):
    blob=TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'
    
def smart_sentiment_roast(user_input,override_sentiment=None):
    user_input = user_input.strip()
    
    """
    returns a single roast based on sentiment or emoji mood slider,
    :param user_input: str, the input text from the user
    :param override_sentiment: float(-1.0 to 1.0) or string, optional sentiment override from mood slider
    :return: str, a roast based on the detected sentiment or mood slider value
    """
    #strip and check input
    if not user_input:
        return "No roast for silence, sweetie. Say something spicy! 🌶️"
    
    #Handle override from mood slider
    if isinstance(override_sentiment, float):
        if override_sentiment > 0.3:
            sentiment = 'positive'
        elif override_sentiment < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
    
    #silence roast list based on sentiment
    if sentiment == 'positive':
        roast_list = positive_roasts
    elif sentiment == 'negative':
        roast_list = negative_roasts
    else:
        roast_list = neutral_roasts
        
    #choose on single roast
    roast = random.choice(roast_list)
    return roast 