Risk	Severity	Notes
Plaintext Credential Storage	High	
Veritabanı bağlantı dizesi config.php dosyasında şifrelenmemiş halde duruyor; dosya erişimi tüm yetkileri ifşa eder.  

Unsanitized User Inputs (SQLi)	High	
Login formundaki POST verileri doğrudan sorguya dahil ediliyor; yetkisiz veri erişimi ve tablo silme riski mevcut.  

Broken Access Control	High	
/admin dizini için session kontrolü eksik; URL'i bilen her kullanıcı yönetici paneline erişebiliyor.  

Insecure Error Handling	Medium	
Uygulama hatalarında sunucu yolu ve PHP sürümü kullanıcıya gösteriliyor; bu durum saldırganlara sistem haritası sağlar.  

Legacy Library Dependency	Medium	
PHP 5.6 döneminden kalan ve artık güvenlik yaması almayan kütüphaneler kullanılıyor; sistem modern sunucularda çalışmayabilir.  

High Code Complexity (Spaghetti Code)	Medium	
İş mantığı ve UI katmanı iç içe geçmiş durumda; bu karmaşıklık güvenlik yamalarının uygulanmasını engelliyor.  

Lack of Audit Trails	Low	
Kritik sistem değişiklikleri (kullanıcı silme, yetki değiştirme) loglanmıyor; bir ihlal sonrası geriye dönük inceleme yapılamaz.
