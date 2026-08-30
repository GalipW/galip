# İkinci Beyin (Second Brain) — Obsidian Vault

Bu klasör, PARA yöntemi (Projeler / Alanlar / Kaynaklar / Arşiv) ile
Zettelkasten tarzı kalıcı notların birleştiği bir kişisel bilgi yönetim
sistemidir. Amaç: aklına gelen her şeyi hızlıca yakalamak, düzenli olarak
işlemek ve ileride kolayca bulup yeniden bağlantı kurmak.

## Obsidian'da açma

1. Obsidian'ı aç → **Open folder as vault** → bu `ikinci-beyin/` klasörünü seç.
2. Ayarlar → **Community plugins** → şu eklentileri kurman önerilir:
   - **Templater** — şablonları (`Şablonlar/`) hızlıca kullanmak için.
   - **Periodic Notes** veya çekirdek **Daily notes** eklentisi — günlük
     notları `Günlük Notlar/` klasörüne, şablonu `Şablonlar/Günlük Not.md`
     olacak şekilde ayarla.
   - **Dataview** (opsiyonel) — projeler/notlar arasında sorgu/liste
     görünümleri oluşturmak için.

## Klasör yapısı

| Klasör | Ne için |
|---|---|
| `00-Gelen Kutusu` | Her şeyin ilk durağı. Hızlı yakala, sonra işle. |
| `01-Projeler` | Bitiş tarihi/net sonucu olan işler. |
| `02-Alanlar` | Süregelen sorumluluk alanları (sağlık, finans, kariyer...). |
| `03-Kaynaklar` | Konu bazlı referans bilgi ve ilgi alanları. |
| `04-Arşiv` | Artık aktif olmayan her şey. |
| `Günlük Notlar` | Günlük kayıtlar / hızlı yakalama. |
| `Şablonlar` | Not şablonları (proje, kaynak, zettelkasten, günlük). |

Her klasörün içinde neyin nereye ait olduğunu açıklayan bir
`_klasör hakkında.md` dosyası var.

## Günlük akış (öneri)

1. Gün içinde her şeyi **Gelen Kutusu**'na veya günlük nota at.
2. Günde/haftada bir "işleme" seansı yap: her notu ait olduğu yere
   (Proje / Alan / Kaynak) taşı ya da sil.
3. Bir kaynaktan çıkardığın kalıcı bir fikri kendi cümlelerinle ayrı bir
   Zettelkasten notuna yaz ve ilgili diğer notlarla `[[bağlantı]]` kur.
4. Projeler bittiğinde Arşiv'e taşı.

## Notlar

- Bu vault, bu git reposunun (`galip`) geri kalanından bağımsızdır — sadece
  aynı repoda birlikte versiyonlanır.
- `.obsidian/` konfigürasyon klasörü kasıtlı olarak eklenmedi; Obsidian'ı ilk
  açtığında kendisi oluşturacak (cihaza özel ayarlar, eklenti listesi vb.
  genelde git'e eklenmez).
