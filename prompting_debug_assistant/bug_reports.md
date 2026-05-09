1. Python: Məntiqi Qiymət Xətası
Summary: apply_discount funksiyasında yanlış riyazi hesablama.

Root Cause: Endirim məbləği əvəzinə faiz dərəcəsinin birbaşa qiymətdən çıxılması.

Resolution: final_price = price - discount_amount olaraq dəyişdirildi.

Lesson Learned: Hesablamalarda dəyişən adlarına diqqət yetirilməli və nəticə real test datası ilə yoxlanılmalıdır.

2. JavaScript: Null/Undefined Obyekt Xətası
Summary: displayUserBios funksiyasında runtime crash.

Root Cause: null və ya undefined olan profile obyektinin bio xüsusiyyətinə müraciət edilməsi.

Resolution: Optional Chaining (?.) və Nullish Coalescing (??) operatorları tətbiq edildi.

Lesson Learned: API-dan gələn dataların tamlığına hər zaman şübhə ilə yanaşılmalı və "default" dəyərlər təyin edilməlidir.

3. Python: Sintaksis və İndentasiya Xətası
Summary: system_diagnostic_report funksiyasının işə düşməməsi.

Root Cause: if/else bloklarında : unudulması və kod sətirlərinin düzgün qruplaşdırılmaması.

Resolution: Python sintaksis qaydalarına uyğun olaraq struktur yenidən quruldu.

Lesson Learned: Kod yazarkən Linter və ya IDE xəbərdarlıqlarına mütləq diqqət yetirilməlidir.

4. C: Massiv Sərhədinin Aşılması (Buffer Overflow risk)
Summary: Massiv indeksindən kənara çıxma (Off-by-one error).

Root Cause: Döngü şərtində <= num_elements istifadə edilərək mövcud olmayan 5-ci indeksə müraciət edilməsi.

Resolution: Döngü şərti < num_elements (maksimum 4-cü indeks) olaraq düzəldildi.

Lesson Learned: Massivlərlə işləyərkən 0-dan başlayan indeksləmə qaydası və sərhəd şərtləri ciddi yoxlanılmalıdır.

5. Bonus: Slicing Xətası (Sənin nümunən)
Summary: Slicing zamanı "off-by-one" xətası.

Root Cause: items[len(items)-n-1:] ifadəsində artıq indeks çıxılması.

Resolution: items[len(items)-n:] olaraq dəyişdirildi.

Lesson Learned: Minimal daxiletmələrlə (edge cases) künc testlərini həyata keçirmək vacibdir.
