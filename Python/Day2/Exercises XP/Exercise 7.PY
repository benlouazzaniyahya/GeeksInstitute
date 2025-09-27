# ex7_temperature.py
import random

def get_random_temp(season: str = None) -> float:
    """
    Return a random float temperature depending on season.
    Seasons: 'winter', 'spring', 'summer', 'autumn' (or 'fall').
    If season is None or unknown, use wide range -10..40.
    """
    season = (season or "").lower()
    if season in ("winter",):
        low, high = -10, 16
    elif season in ("spring",):
        low, high = 0, 23
    elif season in ("summer",):
        low, high = 16, 40
    elif season in ("autumn", "fall"):
        low, high = -2, 25
    else:
        low, high = -10, 40
    return round(random.uniform(low, high), 1)

def advice_for_temp(temp: float) -> str:
    """Return advice string based on temperature ranges."""
    if temp < 0:
        return "Brrr, that's freezing! Wear extra layers today."
    if 0 <= temp <= 16:
        return "Quite chilly! Don't forget your coat."
    if 17 <= temp <= 23:
        return "Nice weather — a light jacket should do."
    if 24 <= temp <= 32:
        return "Warm — dress comfortably."
    return "It's hot — stay hydrated and wear light clothing."

def month_to_season(month: int) -> str:
    """Convert month (1..12) to season (northern hemisphere)."""
    if month in (12, 1, 2):
        return "winter"
    if month in (3, 4, 5):
        return "spring"
    if month in (6, 7, 8):
        return "summer"
    if month in (9, 10, 11):
        return "autumn"
    return ""

def main():
    # Ask the user if they want to enter a month or a season
    choice = input("Do you want to enter a month number (m) or a season name (s)? (m/s): ").strip().lower()
    season = None
    if choice == "m":
        try:
            month = int(input("Enter month number (1-12): ").strip())
            season = month_to_season(month)
            if not season:
                print("Invalid month — using default temperature range.")
        except ValueError:
            print("Invalid input, using default range.")
    elif choice == "s":
        season = input("Enter season (winter/spring/summer/autumn): ").strip().lower()
    else:
        print("Using default season range.")

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp}°C.")
    print(advice_for_temp(temp))

if __name__ == "__main__":
    main()
