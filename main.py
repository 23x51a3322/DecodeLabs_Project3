from data import movies
from recommender import recommend_movies


def display_movies(recommendations):
    """
    Display recommended movies.
    """

    print("\n")
    print("=" * 65)
    print("                 RECOMMENDED MOVIES")
    print("=" * 65)

    if not recommendations:
        print("No recommendations found.")
        return

    for index, movie in enumerate(recommendations, start=1):

        print(f"\n{index}. {movie['title']}")

        print(
            f"   Genre: {', '.join(movie['genre'])}"
        )

        print(
            f"   Similarity Score: {movie['score']}%"
        )

        print("-" * 65)


def main():

    print("=" * 65)
    print("             🎬 MOVIE RECOMMENDATION SYSTEM")
    print("=" * 65)

    print("\nAvailable interests:")
    print(
        "action, science fiction, sci-fi, thriller,"
    )
    print(
        "adventure, technology, ai, superhero,"
    )
    print(
        "romance, love, drama, comedy, science"
    )

    print("\nExample:")
    print("action, ai, technology")

    user_input = input(
        "\nEnter your movie interests: "
    )

    # Convert input into a list
    user_interests = [
        interest.strip().lower()
        for interest in user_input.split(",")
        if interest.strip()
    ]

    # Check input
    if not user_interests:

        print("\nPlease enter at least one interest.")

        return

    # Generate recommendations
    recommendations = recommend_movies(
        user_interests,
        movies,
        top_n=5
    )

    # Display recommendations
    display_movies(recommendations)


if __name__ == "__main__":
    main()