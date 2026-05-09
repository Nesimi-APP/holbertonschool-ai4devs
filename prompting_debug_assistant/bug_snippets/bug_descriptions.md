Təqdim etdiyiniz kod nümunələrindəki xətaları analiz edərək, onları kateqoriyalara ayıran və izah edən bug_descriptions.md faylını aşağıda hazırladım.

🐛 Proqramlaşdırma Xətalarının Təsviri (Bug Descriptions)
Bu sənəd təqdim olunan kod nümunələrindəki məntiqi, sintaksis və icra zamanı (runtime) xətalarını sənədləşdirir.

1. Məntiqi Xəta (Python - Alış-veriş Sistemi)
Fayl: discount_system.py

Xəta Növü: Logical Error (Məntiqi xəta).

Təsviri: apply_discount funksiyası riyazi olaraq yanlış işləyir. Hesablanmış discount_amount dəyişəni kənarda qalır və proqram price-dan endirim məbləğini deyil, faiz dərəcəsinin özünü çıxır.

Nəticə: Məsələn, $1200-dan 10% çıxmaq əvəzinə, sadəcə 10 çıxılır (Nəticə: $1190).

Həlli: final_price = price - discount_amount olaraq düzəldilməlidir.

2. İcra Zamanı Xətası (JavaScript - İstifadəçi Profilləri)
Fayl: user_profiles.js

Xəta Növü: Runtime Error (TypeError).

Təsviri: Proqram mövcud olmayan və ya null olan obyektin xüsusiyyətinə (bio) müraciət etməyə çalışır. Bob üçün profile null-dur, Charlie üçün isə profile ümumiyyətlə təyin edilməyib.

Nəticə: Cannot read properties of undefined/null (reading 'bio') xətası ilə proqram çökür.

Həlli: Optional Chaining (user.profile?.bio) və ya null yoxlaması əlavə edilməlidir.

3. Sintaksis Xəta (Python - Sistem Diaqnostikası)
Fayl: diagnostics.py

Xəta Növü: SyntaxError & IndentationError.

Təsviri:

if və else ifadələrinin sonunda qoşa nöqtə (:) unudulub.

if blokundan sonrakı kod düzgün daxilə çəkilməyib (indentation).

Nəticə: Kod icra olunmur, Python interpretatoru dərhal xəta verir.

Həlli: Blok sonlarına : əlavə edilməli və tabulyasiya boşluqları düzəldilməlidir.

4. Yaddaş və İndeks Xətası (C - Qiymətləndirmə Sistemi)
Fayl: scores.c

Xəta Növü: Off-by-one Error (Buffer Overflow/Out of bounds).

Təsviri: for döngüsündəki şərt i <= num_elements kimidir. 5 elementli massivdə indekslər 0, 1, 2, 3, 4-dür. Döngü 5-ci indeksə müraciət etdikdə massiv sərhədlərini aşır.

Nəticə: Proqram yaddaşdan təsadüfi bir dəyər ("garbage value") oxuyur və ya "Segmentation Fault" xətası ilə dayanır.

Həlli: Döngü şərti i < num_elements olaraq dəyişdirilməlidir.
