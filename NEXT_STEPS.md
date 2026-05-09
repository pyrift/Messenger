# 🚀 Web Loyihaga Qo'shish Mumkin Bo'lgan Funksiyalar

---

## 1. 🔐 Foydalanuvchi Xavfsizligi

### Faqat o'z xabarini tahrirlash
Hozir har kim har qanday xabarni o'zgartira oladi. View da tekshiruv qo'shish kerak:
```python
if instance.sender != request.user:
    return redirect('chat_messages', chat_id=instance.chat.id)
```

### Parol o'zgartirish sahifasi
Foydalanuvchi o'z parolini o'zgartira olsin.

### Email tasdiqlash
Ro'yxatdan o'tishda email yuborib, tasdiqlash orqali kirish.

---

## 2. 💬 Real-time Xabarlar (Django Channels)

Hozir yangi xabar kelganda sahifani yangilash kerak. Django Channels orqali **WebSocket** qo'shilsa, xabarlar avtomatik chiqadi.

**O'rnatish:**
```bash
pip install channels
pip install channels-redis
```

**Afzalligi:** Sahifani yangilamasdan xabarlar ko'rinadi — haqiqiy chat tajribasi.

---

## 3. 📁 Fayl va Rasm Yuborish

Foydalanuvchilar xabar bilan birga rasm yoki fayl yuborsin.

**Model ga qo'shish:**
```python
file = models.FileField(upload_to='uploads/', null=True, blank=True)
image = models.ImageField(upload_to='images/', null=True, blank=True)
```

---

## 4. ✅ Xabar Holati

- **Yuborildi** — server qabul qildi
- **O'qildi** — oluvchi ko'rdi

**Model ga qo'shish:**
```python
is_read = models.BooleanField(default=False)
read_at = models.DateTimeField(null=True, blank=True)
```

---

## 5. 🔍 Xabar Qidirish

Chat ichida yoki barcha chatlarda xabar qidirish.

```python
messages = Message.objects.filter(text__icontains=query)
```

---

## 6. 👤 Profil Sahifasi

- Avatar (profil rasmi)
- Bio (qisqa ma'lumot)
- Online / Offline holat

**Model ga qo'shish:**
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    is_online = models.BooleanField(default=False)
```

---

## 7. 🔔 Bildirishnomalar

Yangi xabar kelganda foydalanuvchiga xabar berish.

- **In-app** — sayt ichida ko'rsatish
- **Email** — elektron pochta orqali
- **Push** — brauzer bildirishnomalari

---

## 8. 😊 Emoji Reaksiyalar

Xabarga emoji bilan reaksiya berish (like, ❤️, 😂 va h.k.)

```python
class Reaction(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=10)
```

---

## 9. 📌 Xabarni Pinlash

Muhim xabarni chat tepasiga mahkamlash.

```python
is_pinned = models.BooleanField(default=False)
```

---

## 10. 🌐 Til va Mavzu Sozlamalari

- Qorong'i / Yorug' mavzu tanlash
- Uz / En / Ru til tanlash

---

## ⭐ Tavsiya: Qaysi Biri Birinchi?

| Funksiya | Qiyinlik | Foydalilik |
|---|---|---|
| Faqat o'z xabarini tahrirlash | ⭐ Oson | 🔥 Juda muhim |
| Real-time (WebSocket) | ⭐⭐⭐ Qiyin | 🔥 Juda muhim |
| Profil sahifasi | ⭐⭐ O'rta | ✅ Foydali |
| Fayl yuborish | ⭐⭐ O'rta | ✅ Foydali |
| Xabar holati | ⭐ Oson | ✅ Foydali |