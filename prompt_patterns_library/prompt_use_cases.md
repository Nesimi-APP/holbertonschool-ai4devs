1. Kod Keyfiyyəti və Refaktorinq (Code Quality & Refactoring)
Məqsəd: Mövcud kodu daha oxunaqlı, sürətli və standartlara uyğun hala gətirmək.

Kodun Optimallaşdırılması:

Giriş: Mürəkkəb dövrlər (loops) və ya ağır hesablamalar olan kod bloku.

Çıxış: Zaman və yaddaş mürəkkəbliyi (O notation) optimallaşdırılmış yeni kod.

Dizayn Patternlərinin Tətbiqi:

Giriş: "Spaghetti" kod və ya təkrar olunan funksionallıq.

Çıxış: Uyğun dizayn patterni (məsələn, Singleton, Strategy) tətbiq edilmiş struktur.

Legacy Kodun Müasirləşdirilməsi:

Giriş: Köhnə kitabxanalar və ya köhnəlmiş sintaksis (məsələn, Python 2).

Çıxış: Müasir standartlara (məsələn, Python 3.12+) uyğunlaşdırılmış kod.

2. Xətaların Tapılması və Sazlanması (Debugging & Error Handling)
Məqsəd: Koddakı gizli səhvləri aşkar etmək və həll yolları tapmaq.

Stack Trace Analizi:

Giriş: Terminaldan alınan xəta mesajı və əlaqəli kod parçası.

Çıxış: Xətanın izahı və onu aradan qaldırmaq üçün konkret addımlar.

Təhlükəsizlik Boşluqlarının Tapılması:

Giriş: Web formaları və ya verilənlər bazası sorğuları olan kod.

Çıxış: SQL Injection, XSS kimi boşluqların müəyyən edilməsi və "sanitized" edilmiş kod.

Məntiqi Səhvlərin (Logical Bugs) Təsbiti:

Giriş: İşləyən lakin yanlış nəticə verən funksiya.

Çıxış: Məntiqdəki yanlışlığın izahı və düzəliş.

3. Testləşdirmə (Testing)
Məqsəd: Proqramın dayanıqlığını təmin etmək üçün avtomatlaşdırılmış testlər yazmaq.

Unit Testlərin Yaradılması:

Giriş: Bir sinif və ya funksiya.

Çıxış: Jest, PyTest və ya JUnit formatında test ssenariləri.

Edge Case Ssenariləri:

Giriş: İstifadəçi məlumatlarını qəbul edən API endpoint.

Çıxış: Boş giriş, limitdən artıq ölçü və ya yanlış tip kimi kənar hallar üçün test siyahısı.

Mock Məlumatların Hazırlanması:

Giriş: Verilənlər bazası sxemi (Schema).

Çıxış: Testlər üçün istifadə ediləcək JSON formatında saxta (mock) məlumatlar.

4. Sənədləşdirmə və Baxım (Documentation & Maintenance)
Məqsəd: Kodun digər tərtibatçılar üçün anlaşıqlı olmasını təmin etmək.

API Sənədlərinin Yaradılması:

Giriş: Sinif və metodların mənbə kodu.

Çıxış: JSDoc, Doxygen və ya Markdown formatında sənədlər.

Commit Mesajlarının Hazırlanması:

Giriş: git diff çıxışı (dəyişikliklərin siyahısı).

Çıxış: "Conventional Commits" standartına uyğun (məsələn, feat:, fix:) mesaj.

Kod Şərhlərinin Əlavə Edilməsi:

Giriş: Sıx və mürəkkəb kod bloku.

Çıxış: Hər sətirin məqsədini izah edən daxili (inline) şərhlər.
