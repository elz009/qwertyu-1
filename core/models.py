from django.db import models

class ModelMajor(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_kg = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru

class ModelUser(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    major = models.ForeignKey(ModelMajor, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True, null=True)
    scores = models.FloatField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ModelCity(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_kg = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru

class ModelAddress(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('apt', 'Apartment'),
        ('house', 'House'),
    ]

    address = models.TextField()
    user = models.ForeignKey(ModelUser, on_delete=models.CASCADE)
    city = models.ForeignKey(ModelCity, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=ADDRESS_TYPE_CHOICES)
    floor = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.address

class ModelStore(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_kg = models.CharField(max_length=255)
    logo = models.URLField(blank=True, null=True)
    gif = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    address_link = models.URLField(blank=True, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    desc_ru = models.TextField()
    desc_en = models.TextField()
    desc_kg = models.TextField()
    iiko_id = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_ru

class ModelCategory(models.Model):
    name_ru = models.CharField(max_length=255)
    name_kg = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    icon = models.URLField(blank=True, null=True)
    stores = models.ManyToManyField(ModelStore)
    priority = models.IntegerField()
    iiko_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name_ru

class ModelItem(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_kg = models.CharField(max_length=255)
    photo = models.URLField(blank=True, null=True)
    gif = models.URLField(blank=True, null=True)
    desc_ru = models.TextField()
    desc_en = models.TextField()
    desc_kg = models.TextField()
    category = models.ForeignKey(ModelCategory, on_delete=models.CASCADE)
    cost = models.FloatField()
    is_sale = models.BooleanField(default=False)
    sale_cost = models.FloatField(blank=True, null=True)
    store = models.ForeignKey(ModelStore, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    is_hit = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    iiko_id = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(default=0)  # Добавлено значение по умолчанию
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_ru


class ModelAdditional(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_kg = models.CharField(max_length=255)
    item = models.ForeignKey(ModelItem, on_delete=models.CASCADE)
    cost = models.FloatField()

    def __str__(self):
        return self.name_ru

class ModelWorkingHours(models.Model):
    store = models.ForeignKey(ModelStore, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f"{self.store.name_ru} ({self.start} - {self.end})"

class ModelStory(models.Model):
    photo = models.URLField()
    priority = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Story {self.id}"

class ModelNews(models.Model):
    photo = models.URLField()
    title = models.CharField(max_length=255)
    desc = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ModelOrder(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('cooking', 'Cooking'),
        ('ready', 'Ready'),
        ('finished', 'Finished'),
        ('cancelled', 'Cancelled'),
    ]

    TYPE_CHOICES = [
        ('togo', 'To Go'),
        ('delivery', 'Delivery'),
    ]

    user = models.ForeignKey(ModelUser, on_delete=models.CASCADE)
    store = models.ForeignKey(ModelStore, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    items = models.ManyToManyField('ModelCartItem')
    total_cost = models.FloatField()
    paid_with_score = models.FloatField()
    total_to_pay = models.FloatField()
    is_paid = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.ForeignKey(ModelAddress, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # Добавление поля для загрузки файла
    file_from_api = models.FileField(upload_to='uploads/', blank=True, null=True)  # Файл из Жүктөгон API

    def __str__(self):
        return f"Order {self.id}"

class ModelCartItem(models.Model):
    item = models.ForeignKey(ModelItem, on_delete=models.CASCADE)
    count = models.FloatField()
    sold_cost_one = models.FloatField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"CartItem {self.id}"
