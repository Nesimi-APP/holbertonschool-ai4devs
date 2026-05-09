### 2. `microservices_description.md`

Bu dosya, mimarideki 8 ana servisin görevlerini ve birbirleriyle nasıl etkileşime girdiklerini detaylandırır.

# Microservices Architecture

Bu mimari, yüksek ölçeklenebilirlik ve hata toleransı sağlamak amacıyla tasarlanmış 8 temel bağımsız servisten oluşmaktadır.[cite: 1]

- **Identity & Access Service (Auth)**: Kullanıcı kayıt, giriş, şifreleme ve JWT tabanlı kimlik doğrulama süreçlerini yönetir.[cite: 1]
- **Product Catalog Service**: Ürün bilgilerini, kategorileri ve özelliklerini yönetir. Kullanıcıların ürünleri aramasını ve listelemesini sağlar.[cite: 1]
- **Order Management Service**: Sipariş oluşturma, sepet yönetimi ve sipariş durumu takibi gibi temel iş mantığını yürütür.[cite: 1]
- **Warehouse & Inventory Service**: Stok miktarlarını takip eder, sipariş sırasında ürünleri rezerve eder ve stok güncellemelerini yönetir.[cite: 1]
- **User Profile Service**: Kullanıcıların adres bilgilerini, tercihlerini ve hesap ayarlarını saklar.[cite: 1]
- **Billing & Payment Service**: Kredi kartı işlemlerini, faturalandırmayı ve ödeme onaylarını harici ödeme geçitleri üzerinden yönetir.[cite: 1]
- **Logistics & Shipping Service**: Kargo firmalarıyla entegrasyon kurar, takip numarası oluşturur ve teslimat sürecini yönetir.[cite: 1]
- **Communication Service (Notification)**: E-posta, SMS ve anlık bildirimleri gönderen merkezi bir haberleşme birimidir.[cite: 1]

## Temel Etkileşimler

- **Sipariş Akışı**: `Order Management Service`, bir sipariş alındığında önce `Inventory` servisinden stok onayı alır, ardından `Payment` servisini tetikleyerek işlemi tamamlar.[cite: 1]
- **Bilgilendirme**: `Shipping Service` kargoyu yola çıkardığında, `Communication Service` otomatik olarak kullanıcıya bir takip bildirimi gönderir.[cite: 1]
- **Veri Güvenliği**: Her servis yalnızca kendi veritabanına erişebilir; veri paylaşımı API'lar üzerinden veya asenkron olaylarla (Event-driven) gerçekleşir.[cite: 2]
