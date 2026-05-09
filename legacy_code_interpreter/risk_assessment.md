Risk	Severity	Notes
Hardcoded Credentials	High	
Hassas veritabanı şifreleri config.php içerisinde açık metin olarak bulundu.  

SQL Injection Vulnerability	High	
Login modülünde kullanıcı girişleri sanitize edilmiyor; veri sızıntısı riski var.  

Deprecated API Usage	High	
Artık desteklenmeyen PHP fonksiyonları kullanılıyor; sistem güncellemelerinde çökme yaşanabilir.  

Exposure of Sensitive Error Messages	Medium	
Hata ayıklama modunda stack trace verileri son kullanıcıya gösteriliyor; iç dizin yapısı ifşa oluyor.  

Missing Unit Tests	Medium	
Kritik iş mantığı modülleri test edilmemiş; regresyon hatalarına açık bir yapı mevcut.  

Tight Coupling	Medium	
Nesneler birbirine aşırı bağımlı; modülerlik düşük olduğu için refactoring süreci zorlaşıyor.  

Insufficient Logging	Low	
Sistem hataları için olay izleme kaydı tutulmuyor; hata ayıklama süreci yavaşlıyor.
