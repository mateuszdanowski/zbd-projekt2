# zbd-projekt2

Uruchamianie:

1. psql -f init-fdw.sql
2. psql -f init-functions.sql
3. python3 ./executor.py


init-fdw: Tworzy rozszerzenia file_fdw oraz cstore_fdw

init-functions: Tworzy funkcje pozwalające dodawać odpowiednie kolumny do tabel oraz kopiować do nich pliki csv

executor: Tworzy pliki csv, a następnie uruchamia zapytania na trzech tabelach dla różnych danych
