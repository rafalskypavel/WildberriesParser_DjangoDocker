# serializer.py

from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def save(self, **kwargs):
        """
        Сохраняет объект, создавая его или обновляя существующий.
        """
        try:
            # Проверяем наличие обязательного поля product_id
            product_id = self.validated_data.get('product_id')
            if not product_id:
                raise serializers.ValidationError("Поле 'product_id' обязательно.")

            # Используем update_or_create для обновления или создания записи
            product, created = Product.objects.update_or_create(
                product_id=product_id,
                defaults=self.validated_data
            )
            return product

        except Exception as e:
            # Логируем ошибку или обрабатываем по своему усмотрению
            raise serializers.ValidationError(f"Ошибка при сохранении продукта: {str(e)}")


# из БД будем брать определ. записи, представлять их в json формате и отправлять их в ответ на запрос пользователя
# для выполнения конвертирование произвольных объектов языка Python в формат JSON - И НАОБОРОТ.
