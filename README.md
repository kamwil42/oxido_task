# Zadanie rekrutacyjne Junior AI Developer

## Opis projektu
Aplikacja jest prostym narzędziem, które automatyzuje proces przekształcania artykułu w formacie tekstowym na semantyczny i dobrze zorganizowany kod HTML. Dzięki integracji z API OpenAI aplikacja generuje kod HTML, który spełnia określone wymagania, takie jak odpowiednia struktura nagłówków, akapitów i miejsc na obrazy.

## Struktura projektu
.env - plik zawierający klucz do API
.gitignore - plik określający jakie pliki mają być ignorowane przez repozytorium git
requirements.txt - plik określajacy biblioteki wymagane do uruchomienia aplikacji
src/artykul.html - plik wyjściowy z wygenerowanym kodem HTML
src/main.py - główny plik aplikacji
src/podglad.html - plik do podglądu przykładowo wygenerowanego kodu
src/szablon.html - szablon do podglądu wstawionego kodu HTML
src/assets/tresc_artykulu.txt - plik z treścią artykułu do przetworzenia

## Działanie aplikacji:
Aplikacja odczytuje treść artykułu z pliku tresc_artykulu.txt, następnie wysyła zapytanie do OpenAI z prośbą o wygenerowanie kodu HTML z odpowiednią strukturą i miejscami na obrazy. Na koniec zapisuje wynik do pliku artykul.html.

Parametry zapytania:
1. Wybrany model to "gpt-4o", czyli zoptymalizowana wersja modelu "gpt-4".
2. Parametr temperature został ustawiony na poziomie 0.2, aby odpowiedzi były mniej losowe. Dzięki temu wygenerowany kod będzie bardziej precyzyjny i przewidywalny.
3. Parametr messages zawierający dwa obiekty o różnych rolach:
a) Rola "system", która określa zadanie AI oraz definiuje podstawową konstrukcję wyników.
b) Rola "user", która określa samo zapytanie i podaje treść artykułu wczytaną z pliku.

Wyjaśnienie funkcji:
1. Funkcja read_article wczytuje artykuł z podanego pliku tekstowego i zwraca jego zawartość. Parametrem wejściowym jest ścieżka do pliku z artykułem.
2. Funkcja process_article tworzy odpowiednie zapytanie dla modelu OpenAI, wysyła je i zwraca odpowiedź z kodem HTML. Parametrem wejściowyjm jest treść artykułu do obrobienia.
3. Funkcja save_to_file zapisuje wygenerowany kod HTML do pliku artykul.html. Parametrami wejściowymi są wygenerowany kod HTML (html_content) oraz ścieżka zapisu pliku artykul.html (file_path).
4. Funkcja main to główna funkcja, która łączy wszystkie kroki i wykonuje skrypt.

## Wymagania wstępne
1. Python 3.8+
2. Biblioteki openai oraz python-dotenv
3. Klucz do API OpenAI

## Instalacja
1. Sklonuj repozytorium za pomocą komendy

    git clone https://github.com/kamwil42/oxido_task.git
    
lub pobierz je jako plik .zip i rozpakuj na komputerze. Przejdź do głownego folderu i otwórz w nim wiersz poleceń.

2. Zainstaluj odpowiednie biblioteki

    pip install -r requirements.txt
    

3. Wklej swój klucz API do pliku .env w formacie: OPENAI_API_KEY = twoj_klucz (zastąp komentarz w pliku swoim kluczem)

4. Przejdź do folderu /src - to w nim znajduje się plik ze skryptem. Uruchom go

    python main.py
    

Wygenerowany plik artykul.html znajdzie się w folderze src (na tym samym poziomie co plik main.py). Aby go podejrzeć, można przenieść jego zawartość do sekcji <body> w pliku szablon.html, a żeby zobaczyć przykładowy artykuł można otworzyć plik podglad.html.