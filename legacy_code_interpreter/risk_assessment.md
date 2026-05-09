Risk	Severity	Notes
Hardcoded credentials	High	
config.php faylında tapılan şifrələr və API açarları birbaşa koda yazılmışdır. Bu, repozitoriyaya giriş əldə edən hər kəsin verilənlər bazasına tam daxil olmasına şərait yaradır.  

Missing unit tests	Medium	
Kritik modullar üçün testlərin olmaması proqramda edilən hər hansı dəyişikliyin digər hissələri sıradan çıxarması (regression) riskini artırır və proqramın keyfiyyətini aşağı salır.  

Deprecated API usage	High	
Sistemin köhnəlmiş PHP funksiyalarından asılılığı var. Növbəti server yenilənməsində bu funksiyalar tamamilə silinəcəyi üçün tətbiqin fəaliyyəti tam dayana bilər.  

Tight coupling	Medium	
Modullar arasındakı həddindən artıq asılılıq kodun strukturunu mürəkkəbləşdirir. Bir hissədə dəyişiklik etmək digər bir çox hissənin yenidən yazılmasını tələb edir, bu da texniki borcu artırır.  

No logging	Low	
Sistem xətaları qeydə almır. Bu, sistemdə baş verən nasazlıqların səbəbini tapmağı çətinləşdirir, lakin birbaşa funksionallığa mane olmur.  

SQL Injection Vulnerability	High	
Giriş modullarında istifadəçi məlumatları (input) təmizlənmir. Hücumçu bazaya zərərli sorğular göndərərək məlumatları oğurlaya, silə və ya dəyişdirə bilər.  

Insecure File Permissions	Medium	
Serverdəki konfiqurasiya faylları "world-readable" statusundadır. Bu o deməkdir ki, eyni serverdəki digər istifadəçilər sizin həssas mühit dəyişənlərinizi oxuya bilər.
