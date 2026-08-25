def calculate_similarity(user_interests, movie_tags):
    """
    Calculate similarity between user interests
    and movie tags.

    Formula:

    Similarity Score =
    Matching Interests / Total User Interests × 100
    """

    # Convert user interests to lowercase
    user_interests = set(
        interest.lower().strip()
        for interest in user_interests
    )

    # Convert movie tags to lowercase
    movie_tags = set(
        tag.lower().strip()
        for tag in movie_tags
    )

    # Find common interests
    matching_interests = user_interests.intersection(movie_tags)

    # Avoid division by zero
    if len(user_interests) == 0:
        return 0

    # Calculate percentage
    score = (
        len(matching_interests)
        / len(user_interests)
    ) * 100

    return round(score, 2)


def recommend_movies(user_interests, movies, top_n=5):
    """
    Generate movie recommendations
    based on user interests.
    """

    recommendations = []

    for movie in movies:

        score = calculate_similarity(
            user_interests,
            movie["tags"]
        )

        recommendations.append({
            "title": movie["title"],
            "genre": movie["genre"],
            "score": score
        })

    # Sort by highest similarity score
    recommendations.sort(
        key=lambda movie: movie["score"],
        reverse=True
    )

    # Return top recommendations
    return recommendations[:top_n]