# Python-Lernprojekt

Dieses Repository begleitet mich dabei, Python Schritt für Schritt zu lernen und die wichtigsten Grundlagen zu festigen. Es enthält Notizen, kleine Skripte und Experimente, mit denen ich zentrale Konzepte der Sprache nachvollziehe.

## Ziele
- Verständnis der grundlegenden Syntax von Python aufbauen
- Mit Datentypen wie `int`, `float`, `str` und `list` sicher umgehen
- Kontrollstrukturen wie `if`-Abfragen, Schleifen und Funktionen anwenden
- Einfache Skripte schreiben, die alltägliche Aufgaben automatisieren
- Gute Entwicklungsgewohnheiten wie das Testen und Dokumentieren üben

## Voraussetzungen
- Ein Rechner mit installiertem Python (empfohlen: Python 3.11 oder aktueller)
- Ein Terminal bzw. eine Shell
- Ein Editor oder eine IDE wie VS Code, PyCharm oder ein einfacher Texteditor

## Installation
```bash
# Python-Version prüfen
python3 --version

# Virtuelle Umgebung anlegen (optional, aber empfohlen)
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# Abhängigkeiten installieren, sobald eine requirements.txt vorhanden ist
pip install -r requirements.txt
```

## Projektstruktur
- `notebooks/` – Jupyter-Notebooks für interaktive Experimente (optional)
- `scripts/` – Kleine Python-Skripte zu einzelnen Themen
- `resources/` – Spickzettel, weiterführende Links oder PDF-Material
- `tests/` – Erste Unit-Tests, um das Gelernte abzusichern

Diese Ordner werden nach Bedarf ergänzt und angepasst.

## Lerninhalte
1. **Einstieg**: Datentypen, Operatoren, Ein- und Ausgabe
2. **Kontrollfluss**: `if`, `for`, `while`, `match`
3. **Funktionen**: Parameter, Rückgabewerte, Docstrings
4. **Datenstrukturen**: Listen, Tupel, Dictionaries, Sets
5. **Module & Pakete**: Importieren, eigene Module schreiben
6. **Fehlerbehandlung**: `try`, `except`, `finally`
7. **Dateizugriff**: Lesen und Schreiben von Dateien
8. **Tests & Qualität**: `unittest`, `pytest`, Formatierung mit `black`

## Arbeitsweise
- Jede Lerneinheit endet mit einer kurzen Übung oder einem Mini-Projekt.
- Nach jedem Kapitel werden die wichtigsten Erkenntnisse im Repository dokumentiert.
- Änderungen werden regelmäßig mit klaren Commit-Nachrichten gespeichert.

## Nützliche Ressourcen
- Offizielle Dokumentation: https://docs.python.org/3/
- Python-Tutorial auf Deutsch: https://python-kurs.eu/
- Real Python (englisch): https://realpython.com/
- Kostenlose Übungsaufgaben: https://www.codewars.com/ und https://projecteuler.net/

## Nächste Schritte
- Ordnerstruktur anlegen und ein erstes "Hello, World"-Skript schreiben
- Virtuelle Umgebung einrichten und Anforderungen definieren
- Lernplan festlegen (z. B. wöchentliche Themen, Abschlussprojekt)

Viel Erfolg und Spaß beim Python-Lernen!

## Как запушить изменения на GitHub

1. Перейдите в папку проекта (если ещё не в ней):
   ```bash
   cd /путь/к/проекту
   ```

2. Проверьте текущее состояние файлов:
   ```bash
   git status
   ```

3. Добавьте все изменённые файлы в индекс (или укажите нужные файлы вместо точки):
   ```bash
   git add .
   ```

4. Создайте коммит с коротким и понятным сообщением:
   ```bash
   git commit -m "Опишите, что изменили"
   ```
   Если Git попросит имя и email, настройте их и повторите коммит:
   ```bash
   git config --global user.name "Ваше имя"
   git config --global user.email "you@example.com"
   ```

5. Убедитесь, что подключён правильный удалённый репозиторий:
   ```bash
   git remote -v
   ```
   Если репозиторий ещё не добавлен, выполните:
   ```bash
   git remote add origin https://github.com/username/repo.git
   ```

6. Отправьте изменения в нужную ветку на GitHub (чаще всего `main`):
   ```bash
   git push origin main
   ```
   Замените `main`, если используете другую ветку.

7. Если Git пишет, что ветка отстаёт, сначала подтяните изменения, решите конфликты и повторите отправку:
   ```bash
   git pull origin main
   git add .
   git commit -m "Исправил конфликты"
   git push origin main
   ```

После успешного `git push` зайдите в репозиторий на GitHub и убедитесь, что новый коммит появился в истории.
