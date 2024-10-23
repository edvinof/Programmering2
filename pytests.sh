# Kör alla tester i projektets katalog och alla dess undermappar
pytest

# Kör alla tester i en specifik fil
pytest tests/test_example.py

# Kör en specifik testfunktion i en fil
pytest tests/test_example.py::test_function_name

# Kör alla tester i en specifik katalog
pytest tests/

# Kör tester med ökad detaljrikedom (verbositet) för att se mer information om varje test
pytest -v

# Inkludera tidsmätning för att se hur lång tid varje test tar
pytest --durations=0

# Kör tester och visa en kodtäckningsrapport med pytest-cov (förutsatt att pytest-cov är installerat)
pytest --cov=app_directory --cov-report=term

# Kör en specifik testfil och visa kodtäckningsrapport
pytest tests/test_example.py --cov=app_directory --cov-report=term

# Kör tester och generera en detaljerad HTML-rapport över kodtäckningen
pytest --cov=app_directory --cov-report=html

# Kör tester och inkludera kodtäckning för att visa både rapport i terminalen och som en HTML-fil
pytest --cov=app_directory --cov-report=term --cov-report=html

# Ignorera warnings under testkörningen
pytest -p no:warnings

# Endast köra tester som matchar en specifik marker, t.ex., tester som är markerade som "slow"
pytest -m "slow"

# Kör tester i en specifik fil och stoppa direkt om ett test misslyckas (bra för snabbare felupptäckt)
pytest tests/test_example.py -x

# Använd verbositet och kodtäckningsrapport samtidigt
pytest -v --cov=app_directory --cov-report=term
