# Link do prezentacji na dysku google:

https://docs.google.com/presentation/d/1jDMELZqZ8FnLvyj4b6pUF6kw6lfDKYxgpbEKi9NNpwU/edit?usp=sharing

# Dokumentacja - projekt zespołowy pierwszy

### 1. Analiza i ideacja tematu projektu: Jak kontrolować jakość ćwiczeń gimnastycznych?
Interpretacja problemu: Częstym problemem podczas wykonywania ćwiczeń fizycznych jest nieprawidłowa technika oraz to, że wiele osób nie stać na trenera personalnego, a nawet jeśli, to nie jest on dostępny 24/7.
Pomysły na realizacje projektu (napisane hasłowo):
- Urządzenie sprawdzające postawę
    - Realizacja
        -	Sprawdzanie czy czujniki są w linii
        -	Mierzenie trajektorii ruchu
        -	Linki/taśmy przyczepione do siłomierza
- Liczenie ilości powtórzeń
    - Realizacja
        -	Czujniki odległości
        -	Mierzenie rozkładu siły na rękach podczas pompek i mierzenie tempa
        -	Arduino krzyczy gdy ktoś zaczyna zwalniać
- Odpowiednie odżywianie
- Szukanie tanich karnetów na siłownie
- Dobra rozgrzewka
- Nawodnienie
- Czytniki, ciśnienia pulsu
- System nagradzania
Decyzja: Zdecydowaliśmy się aby zrealizować urządzenie, które będzie badać jak użytkownik wykonuje tzw. pompki. Plan przewiduje, pomiary za pomocą czujnika odległości, dwóch żyroskopów, oraz sygnalizację za pomocą paska LED. Po udanym zrealizowanie prototypu planujemy rozszerzyć projekt o nowe funkcje. (np. dodanie przysiadów, sygnalizacja kiedy robi się wdech, a kiedy wydech, itp. zależnie od pomysłów).

### 2. Przygotowanie narzędzi
Korzystamy z Gita tworząc issues i dodając tam pliki, które uważamy za przydatne, a także uzupełniając dokumentację o ten plik oraz notatki ze spotkań z prowadzącym. Komunikujemy się za pomocą aplikacji Messenger.

### 3. Wstępne zamierzenia (z punktu widzenia użytkownika) – funkcjonalność krytyczna:
Użytkownik podaje ile pompek zamierza wykonać. Po założeniu urządzenia zaczyna wykonywać ćwiczenie. Pasek LED świeci się na czerwono, gdy nie jest zachowana odpowiednia linia ciała, na zielono po wykonaniu odpowiedniej liczby prawidłowych powtórzeń.

### 4. Analiza literatury:

- Biblioteka do obsługi żyroskopu:
    - Link do strony: https://playground.arduino.cc/Main/MPU-6050/ 
- Biblioteka do obsługi paska LED:
    - machine
    - neopixel
- Biblioteka do obsługi czujnika odległości: 
    - HCSR04
- Warunki poprawnego wykonywania pompek:
    - Warunkami poprawnej pompki są: 
        - wolne wykonywanie ćwiczenia
        - ciało ułożone w linii prostej
        - głębokie ugięcie łokci – prawie dotknięcie klatką piersiową podłogi
- Najbliższy sklep z elektroniką:
    Znajduje się pod skrzyżowaniem ulicy alei Niepodległości z ulicą wawelską przechodzącą w ulicę Alei Armii Ludowej

### 5. Krytyczne funkcjonalności i ich testy:

- Poprawne działanie żyroskopu:
Sprawdzenie czy żyroskop dobrze czyta kąty nachylenia oraz przyspieszenie po wgraniu sterowników na płytkę WEMOS

- Poprawne działanie czujnika odległości:
Sprawdzenie czy czujnik odległości dobrze odczytuje odległość po wgraniu sterowników na płytkę WEMOS

- Dobór odpowiednich żyroskopów:
Zakupiliśmy dwa żyroskopy Gy-521, na temat których jest wiele poradników w internecie, a także, które są niedrogie i znajdują się w pobliskim sklepie.

- Odpowiednie dobranie granicznej różnicy kątów dla których żyroskop sygnalizuje złe wykonanie ćwiczenia:
Mamy zamiar to wykonać za pomocą metody prób i błędów, gdyż w źródłach najczęściej pada stwierdzenie, żeby ciało tworzyło linię prostą, jednak w rzeczywistości dwa żyroskopy nie wskażą takich samych kątów odchyleń. Sprawdzenie czy dobrze „przesyła” informację do paska LED.

- Testy paska LED:
Symulacja zachowania paska dla danych zmiennych. Sprawdzenie czy pasek LED poprawnie wyświetla kolory dla odpowiednich ustawień czujnika odległości jak i żyroskopu – na początku na sucho, później już na użytkowniku.

- Testy czujnika odległości:
Sprawdzenie metodą prób i błędów jaka odległość, klatki piersiowej od ziemi powinna zostać użyta, żeby urządzenie uznało pompkę za wykonaną. Sprawdzenie czy dobrze „przesyła” do paska LED informację o  odległości.

- Testy całościowe:
Sprawdzenie czy urządzenie sygnalizuje, gdy plecy są za bardzo wygięte w górę lub w dół. Sprawdzenie czy po wykonaniu odpowiedniej liczby powtórzeń, pasek LED świeci się na zielono.