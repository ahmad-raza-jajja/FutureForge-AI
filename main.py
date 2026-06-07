# Career Navigator AI
# Final Project for Code in Place



print("Developed by Ahmad Raza Jajja")
print("Code in Place Final Project")

def display_welcome():
    print("=" * 50)
    print("        CAREER NAVIGATOR AI")
    print("=" * 50)
    print()
    print("Discover your future career path!")
    print()


def get_career_info(choice):
    careers = {
        "1": {
            "career": "AI Engineer",
            "skills": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "Data Structures",
                "Mathematics"
            ],
            "roadmap": [
                "Learn Python",
                "Learn Data Structures",
                "Study Machine Learning",
                "Build AI Projects",
                "Apply for Internships"
            ]
        },

        "2": {
            "career": "Software Engineer",
            "skills": [
                "Python",
                "Java",
                "Data Structures",
                "Algorithms",
                "Git & GitHub"
            ],
            "roadmap": [
                "Learn Programming",
                "Practice DSA",
                "Build Projects",
                "Learn GitHub",
                "Apply for Jobs"
            ]
        },

        "3": {
            "career": "Cybersecurity Specialist",
            "skills": [
                "Networking",
                "Linux",
                "Ethical Hacking",
                "Python",
                "Security Tools"
            ],
            "roadmap": [
                "Learn Networking",
                "Learn Linux",
                "Study Cybersecurity",
                "Practice in Labs",
                "Earn Certifications"
            ]
        },

        "4": {
            "career": "Data Scientist",
            "skills": [
                "Python",
                "Statistics",
                "Data Analysis",
                "Machine Learning",
                "Visualization"
            ],
            "roadmap": [
                "Learn Python",
                "Study Statistics",
                "Analyze Datasets",
                "Build Data Projects",
                "Create Portfolio"
            ]
        },

        "5": {
            "career": "Web Developer",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Backend Development"
            ],
            "roadmap": [
                "Learn HTML & CSS",
                "Learn JavaScript",
                "Build Websites",
                "Learn React",
                "Create Portfolio"
            ]
        }
    }

    return careers.get(choice)


def show_result(data, name):
    print("\n" + "=" * 50)
    print("CAREER REPORT FOR:", name.upper())
    print("=" * 50)

    print("\nRecommended Career:")
    print(data["career"])

    print("\nEssential Skills:")
    for skill in data["skills"]:
        print("-", skill)

    print("\nLearning Roadmap:")
    step = 1
    for item in data["roadmap"]:
        print(str(step) + ".", item)
        step += 1

    print("\nMotivational Advice:")
    print("Stay consistent, build projects, and never stop learning!")

    print("\nGood luck on your journey!")
    print("=" * 50)


def main():

    display_welcome()

    while True:

        name = input("Enter your name: ")

        print("\nChoose your area of interest:")
        print("1. Artificial Intelligence")
        print("2. Software Engineering")
        print("3. Cybersecurity")
        print("4. Data Science")
        print("5. Web Development")

        choice = input("\nEnter your choice (1-5): ")

        data = get_career_info(choice)

        if data:
            show_result(data, name)
        else:
            print("\nInvalid choice!")

        again = input("\nDo you want another recommendation? (yes/no): ")

        if again.lower() != "yes":
            print("\nThank you for using Career Navigator AI!")
            break


main()
