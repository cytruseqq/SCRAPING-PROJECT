# 🕸️ Web Scraper Project (Distributed System)

> System rozproszonego scrapera stron internetowych z interfejsem webowym i architekturą kontenerową.

## 📌 Opis projektu

Celem projektu było stworzenie systemu do scrapowania stron WWW, działającego w architekturze rozproszonej. Użytkownik, za pomocą prostego interfejsu webowego, wprowadza adresy URL, które następnie są asynchronicznie przetwarzane przez silnik scrapujący. Wyniki zapisywane są do bazy danych MongoDB.

## 🛠 Architektura systemu

Projekt składa się z trzech niezależnych modułów, uruchamianych w kontenerach Docker:

1. **Frontend (Flask + HTML/CSS)** – formularz do wprowadzania adresów URL.
2. **Silnik scrapujący (Python asyncio + multiprocessing)** – przetwarza równolegle strony internetowe.
3. **Baza danych (MongoDB)** – przechowuje artykuły w formacie dokumentowym.

📦 Całość zarządzana jest przez `Docker Compose`.

## 🧰 Technologie

- **Python 3** (Flask, `aiohttp`, `BeautifulSoup`, `multiprocessing`)
- **HTML/CSS** (prosty frontend)
- **MongoDB**
- **Docker + Docker Compose**

## 🚀 Uruchomienie projektu

1. **Klonowanie repozytorium:**

```bash
git clone https://github.com/cytruseqq/SCRAPING_PROJECT.git
cd SCRAPING_PROJECT/web-scraper-project
```

2. **Uruchomienie aplikacji:**

```bash
docker-compose up --build
```

3. **Dostęp do aplikacji:**

Otwórz w przeglądarce: [http://localhost:5001](http://localhost:5001)

## 📋 Instrukcja użytkowania

1. Wprowadź jeden lub więcej adresów URL w formularzu.
2. Kliknij **"Start Scraping"**.
3. Aplikacja rozpocznie pobieranie danych, a komunikat **"OK – scraping started"** potwierdzi działanie.
4. Dane zostaną zapisane w kolekcji `articles` w MongoDB.

## 🧪 Testowanie

- System był testowany lokalnie na Windows z Docker Desktop.
- Poprawność zapisu w MongoDB została potwierdzona przez **MongoDB Compass**.
- Scrapowanie przebiegało równolegle bez błędów dla wielu adresów.

## 🔮 Możliwości rozwoju

- 🖥️ Wyświetlanie wyników w panelu webowym
- 🕒 Automatyczne scrapowanie w zadanych odstępach (scheduler)
- 📬 Kolejka zadań (np. Redis + Celery)
- 🎨 Usprawnienia UI/UX

## 🧑‍💻 Autorzy

- **Adrian Witów** – 21319
- **Magdalena Czyżewska** – 21227  
Grupa: 3

## 🔗 Repozytorium

[https://github.com/cytruseqq/SCRAPING_PROJECT/tree/main/web-scraper-project](https://github.com/cytruseqq/SCRAPING_PROJECT/tree/main/web-scraper-project)

---

📅 **Data utworzenia raportu:** 11.05.2025