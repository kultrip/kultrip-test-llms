import random

STORY_TEMPLATES = {
    "impressionism": [
        "Follow in the footsteps of Monet and Renoir as you enjoy: {description}",
        "Experience the spirit of Impressionism in Paris: {description}",
        "Let the colors and light of Impressionist Paris inspire you: {description}",
        "Imagine the artists painting en plein air along the Seine: {description}"
    ],
    "romance": [
        "Set the scene for a romantic escape: {description}",
        "Share unforgettable moments with a loved one: {description}",
        "Let love blossom in Paris: {description}"
    ],
    "museum": [
        "Step inside and discover treasures of art and history: {description}",
        "Let the masterpieces captivate you: {description}"
    ],
    "landmark": [
        "Marvel at the iconic sights of Paris: {description}"
    ],
    "default": [
        "{description} This experience complements your journey inspired by {inspiration}."
    ]
}

FUN_FACTS = {
    "Musée d'Orsay": "Musée d'Orsay houses the largest collection of Impressionist masterpieces in the world.",
    "Louvre Museum": "Did you know the Louvre was originally a royal palace before becoming a museum?",
    "Montmartre": "Montmartre was a favorite haunt of Picasso, Monet, and Van Gogh."
}

def generate_storytelling(activity, inspiration):
    tags = [tag.lower() for tag in activity.get("story_tags", [])]
    act_type = activity.get("category", "").lower()
    location = activity.get("location", "")
    # Choose theme by priority: inspiration, activity type, default
    theme = "default"
    if inspiration:
        for key in STORY_TEMPLATES:
            if key in tags or key in inspiration.lower():
                theme = key
                break
    if theme == "default" and act_type in STORY_TEMPLATES:
        theme = act_type
    template = random.choice(STORY_TEMPLATES[theme])

    # Add fun fact if available
    fun_fact = FUN_FACTS.get(location)
    story = template.format(description=activity['description'], inspiration=inspiration)
    if fun_fact:
        story += f" Fun fact: {fun_fact}"
    return story