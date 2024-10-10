
# Övning: Utforska filer och sök i innehåll

### Instruktioner:

1. Skapa en ny katalog som heter `övning` och navigera in i den.
   ```bash
   mkdir övning
   cd övning
   ```

2. Skapa en ny textfil som heter `info.txt` och skriv in följande information i den:
   ```bash
   echo "Detta är en testfil. Här kan du söka efter mönster." > info.txt
   echo "Detta är en rad med ett Error-meddelande." >> info.txt
   echo "Detta är ytterligare en rad med ett varningsmeddelande." >> info.txt
   ```

3. Visa innehållet i filen med `cat`.
   ```bash
   cat info.txt
   ```

4. Använd `grep` för att hitta alla rader som innehåller ordet "Error".
   ```bash
   grep "Error" info.txt
   ```

5. Räkna antalet rader i `info.txt` med `wc`.
   ```bash
   wc -l info.txt
   ```

6. Skapa en ny fil som heter `filtered.txt` och spara alla rader som innehåller ordet "rad" från `info.txt`.
   ```bash
   grep "rad" info.txt > filtered.txt
   ```

7. Lägg till ytterligare en rad till `filtered.txt` med hjälp av `echo`.
   ```bash
   echo "Detta är en extra rad." >> filtered.txt
   ```

8. Använd `cat` och `wc` för att visa och räkna antalet rader i `filtered.txt`.
   ```bash
   cat filtered.txt
   wc -l filtered.txt
   ```

---

### Resultat:
Genom att följa stegen ovan får du träna på att:
- Skapa och navigera i kataloger.
- Skriva till och läsa från filer.
- Använda `grep` för att söka i filer.
- Använda `wc` för att räkna rader.
- Omdirigera utdata till filer med `>` och `>>`.
