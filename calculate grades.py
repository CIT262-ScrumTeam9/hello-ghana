def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def main():
    try:
        score = float(input("Enter the numerical score: "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"Grade: {grade}")
        else:
            print("Invalid score. Score must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numerical score.")

if __name__ == "__main__":
    main()
