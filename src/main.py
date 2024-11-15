import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def read_article(article_file):
    with open(article_file, 'r', encoding='utf-8') as file:
        article_content = file.read()
    return article_content

def process_article(article_content):
    response = client.chat.completions.create(
        model = "gpt-4o",
        temperature = 0.2,
        messages = [
            {
                "role": "system",
                "content": (
                    "Jesteś sztuczną inteligencją specjalizującą się w przekształcaniu artykułów na kod HTML.\n"
                    "Używasz odpowiednich tagów HTML do strukturyzacji artykułu: nagłówków, akapitów itp.\n"
                    "Przy dodawaniu obrazków używasz tagów <figure> i <img>, a dla ich podpisów tagu <figcaption>.\n"
                    "Zwracasz tylko kod wewnątrz tagów <body> i </body>, nie dołączając ich.\n"
                    "Do kodu dodajesz wolne linijki tak, aby kod był bardziej czytelny.\n"
                    "Używasz języka polskiego.\n"
                    "Ważne: wynik będzie tylko zwykłym tekstem. Zabronione jest używanie składni markdown, formatowania i innych oznaczeń."
                )
            },
            {
                "role": "user",
                "content": (
                    "Przekształć proszę cały poniższy tekst artykułu na kod HTML, który spełnia następujące wytyczne:\n"
                    "1. Dodaj obrazki tam, gdzie mogą być przydatne z atrybutem src='image_placeholder.jpg';\n"
                    "2. Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który można użyć do wygenerowania grafiki;\n"
                    "3. Pod każdym obrazkiem dodaj podpis z krótkim opisem obrazka.\n\n"
                    "Treść artykułu:\n" + article_content
                )
            }
        ]
    )

    html_content = response.choices[0].message.content
    return html_content

def save_to_file(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    current_directory = os.path.dirname(__file__)
    article_file = os.path.join(current_directory, "assets\\tresc_artykulu.txt")
    
    article_content = read_article(article_file)
    
    html_content = process_article(article_content)
    
    save_to_file(html_content, os.path.join(current_directory, "artykul.html"))
 

if __name__ == "__main__":
    main()
