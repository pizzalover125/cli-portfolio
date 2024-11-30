import sys
import os
import platform

class PortfolioCLI:
    def __init__(self):
        self.name = "pizzalover125"
        self.skills = {
            "Frontend Frameworks": ["HTML", "Flask", "Svelte"],
            "Frontend Styling": ["CSS", "Bootstrap", "Tailwind"],
            "Backend": ["Python", "JavaScript", "jQuery"],
            "Databases": ["SQLite", "Supabase"],
            "AI/ML": ["OpenCV", "TensorFlow"],
            "Tooling": ["GitHub", "VSCode", "Linux", "Windows", "Raspberry Pi"]
        }
        
        self.projects = [
            {
                "name": "Cognified",
                "description": "Mobile-friendly application to enhance cognitive abilities through interactive games.",
                "technologies": ["HTML", "CSS", "JavaScript", "Capacitor.js"],
                "links": {
                    "Website": "https://pizzalover125.github.io/cognified/build/index.html",
                    "GitHub": "https://github.com/pizzalover125/cognified"
                }
            },
            {
                "name": "SkimVid",
                "description": "YouTube video summarization tool supporting multiple languages.",
                "technologies": ["Flask", "Python", "HTML", "CSS", "Gemini API"],
                "links": {
                    "Website": "https://video-summary-zayq.onrender.com/",
                    "GitHub": "https://github.com/pizzalover125/video-summary"
                }
            },
            {
                "name": "Digit Predictor",
                "description": "Convolutional Neural Network for classifying handwritten digits.",
                "technologies": ["HTML", "CSS", "JavaScript", "TensorFlow.js"],
                "links": {
                    "Website": "https://supercoolai.netlify.app/",
                    "GitHub": "https://github.com/pizzalover125/digitPredictor"
                }
            }
        ]
        
        self.experience = [
            {
                "title": "CyberSeniors Mentor",
                "description": "Contributed over 40 hours assisting seniors with technology training, helping bridge the digital divide."
            },
            {
                "title": "Hackathon Organizer",
                "description": "Hosted 'Counterspell Phoenix,' a game jam for middle/high schoolers in November 2024. I organizer a venue, locked in sponsors, made a website, made a budget, and completed outreach to local high schools. "
            }
        ]
        
        self.certifications = [
            "FreeCodeCamp: Web Development", 
            "FreeCodeCamp: Frontend Development", 
            "FreeCodeCamp: Data Analysis", 
            "FreeCodeCamp: Scientific Computing with Python", 
            "Coursera Project Network: Microsoft Excel", 
            "Coursera Project Network: WordPress", 
            "Coursera Project Network: Figma"
        ]
        
        self.contact = {
            "Email": "chessthinker600@gmail.com",
            "GitHub": "https://github.com/pizzalover125"
        }

    @staticmethod
    def clear_screen():
        """
        Cross-platform screen clearing method.
        Works on Windows, macOS, and Linux.
        """
        system = platform.system().lower()
        
        if system == 'windows':
            os.system('cls')
        else:
            os.system('clear')

    def display_header(self):
        self.clear_screen()
        print("\n" + "="*50)
        print(f"🍕 {self.name}'s Portfolio".center(50))
        print("="*50 + "\n")

    def display_intro(self):
        self.display_header()
        print("Hey! I'm pizzalover125. I'm an aspiring programmer")
        print("looking to change the world with code, one line at")
        print("a time. Each project, skill, and experience brings me")
        print("closer to my goal of making a meaningful impact.\n")

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
        print("💻 Projects:\n")
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
        print("🏆 Experience:\n")
        for exp in self.experience:
            print(f"{exp['title']}:")
            print(f"  {exp['description']}\n")

    def display_certifications(self):
        self.display_header()
        print("📜 Certifications:\n")
        for cert in self.certifications:
            print(f"- {cert}")
        print()

    def display_contact(self):
        self.display_header()
        print("📞 Contact Information:\n")
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

            if choice == '1':
                self.display_intro()
            elif choice == '2':
                self.display_skills()
            elif choice == '3':
                self.display_projects()
            elif choice == '4':
                self.display_experience()
            elif choice == '5':
                self.display_certifications()
            elif choice == '6':
                self.display_contact()
            elif choice == '0':
                self.clear_screen()
                print("\nThanks for visiting my portfolio! Goodbye. 👋")
                break
            else:
                print("\nInvalid choice. Please try again.")

            input("\nPress Enter to continue...")

def main():
    portfolio = PortfolioCLI()
    portfolio.main_menu()

if __name__ == "__main__":
    main()