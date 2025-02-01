# Imports
import sys
import os
import platform
import json
import textwrap

# Data from JSON files
def getJsonFromFile(fileName):
    with open(fileName, 'r') as file:
        return json.load(file)

# Main Class
class PortfolioCLI:
    def __init__(self):
        self.name = "🍕 pizzalover125"
        self.skills = getJsonFromFile("pizzalover125/skills.json")
        self.contact = getJsonFromFile("pizzalover125/contact.json")
        self.projects = getJsonFromFile("pizzalover125/projects.json")
        self.experience = getJsonFromFile("pizzalover125/experience.json")
        self.introduction = getJsonFromFile("pizzalover125/introduction.json")
        self.certifications = getJsonFromFile("pizzalover125/certifications.json")


    @staticmethod
    def clear_screen():
        system = platform.system().lower()
        
        if system == 'windows':
            os.system('cls')
        else:
            os.system('clear')

    def display_header(self):
        self.clear_screen()
        print("\n" + "="*50)
        print(f"{self.name}'s Portfolio".center(50))
        print("="*50 + "\n")

    def display_intro(self):
        self.display_header()
        wrapped_intro = textwrap.fill(
            self.introduction["introduction"], 
            width=50,  
        )
        print(wrapped_intro)


    def display_skills(self):
        self.display_header()
        print("🛠️ Skills:\n")
        for category, skill_list in self.skills.items():
            print(f"{category}:")
            for skill in skill_list:
                print(f"  - {skill}")
            print()

    def display_projects(self):
        self.display_header()
        print("💻  Projects:\n")
        for project in self.projects:
            print(f"{project['name']}:")
            print(f"  Description: {project['description']}")
            print("  Technologies:")
            for tech in project['technologies']:
                print(f"    - {tech}")
            print("  Links:")
            for link_type, url in project['links'].items():
                print(f"    - {link_type}: {url}")
            print()

    def display_experience(self):
        self.display_header()
        print("🏆  Experience:\n")
        for exp in self.experience:
            print(f"{exp['title']}:")
            print(f"  {exp['description']}\n")

    def display_certifications(self):
        self.display_header()
        print("📜  Certifications:\n")
        for cert in self.certifications:
            print(f"- {cert}")
        print()

    def display_contact(self):
        self.display_header()
        print("📞  Contact Information:\n")
        for method, info in self.contact.items():
            print(f"{method}: {info}")
        print()

    def main_menu(self):
        while True:
            self.display_header()
            print("Select an option:")
            print("1. Introduction")
            print("2. Skills")
            print("3. Projects")
            print("4. Experience")
            print("5. Certifications")
            print("6. Contact")
            print("0. Exit")

            choice = input("\nEnter your choice: ")

            match choice:
                case'1':
                    self.display_intro()
                case '2':
                    self.display_skills()
                case '3':
                    self.display_projects()
                case '4':
                    self.display_experience()
                case '5':
                    self.display_certifications()
                case '6':
                    self.display_contact()
                case '0':
                    self.clear_screen()
                    print("\nThanks for visiting my portfolio! Goodbye. 👋")
                    break
                case _:
                    print("\nInvalid choice. Please try again.")

            input("\nPress Enter to continue...")

def main():
    portfolio = PortfolioCLI()
    portfolio.main_menu()

if __name__ == "__main__":
    main()