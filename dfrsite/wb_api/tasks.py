from celery import shared_task
import requests
from .serializer import ProductSerializer
from celery.utils.log import get_logger

logger = get_logger(__name__)

@shared_task(autoretry_for=(requests.RequestException,),
              retry_backoff=True,
              retry_jitter=True,
              retry_kwargs={'max_retries': 5})
def fetch_product_task(article):
    url = f"https://card.wb.ru/cards/detail?appType=0&regions=80,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&dest=-2133464&nm={article}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    logger.info(f"Fetching data for article: {article}")

    try:

        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            product_data = response.json()
            products = product_data.get('data', {}).get('products', [])

            print(products)

            # Убедитесь, что в products есть данные
            if not products:
                logger.error(f"No products found for article: {article}")
                return {"status": "not_found", "message": "Данного артикула на сайте Wildberries нет!"}

            product_info = products[0]

            product_data = {
                'product_id': product_info['id'],
                'brand': product_info['brand'],
                'brand_id': product_info['brandId'],
                'name': product_info['name'],
                'entity': product_info['entity'],
                'supplier': product_info['supplier'],
                'supplier_id': product_info['supplierId'],
                'supplier_rating': product_info['supplierRating'],
                'price_u': product_info['priceU'] / 100,
                'sale_price_u': product_info['salePriceU'] / 100,
                'sale': product_info['sale'],
                'rating': product_info['rating'],
                'review_rating': product_info['reviewRating'],
                'feedbacks': product_info['feedbacks'],
                'total_quantity': product_info['totalQuantity']
            }

            serializer = ProductSerializer(data=product_data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Product '{product_info.get('name')}' added successfully for article: {article}")
                return {"status": "success", "message": f"___{product_info.get('name')}___ добавлен в БД успешно!"}
            else:
                logger.error(f"Validation error for article {article}: {serializer.errors}")
                return {"status": "validation_error", "errors": serializer.errors}

    except requests.RequestException as e:
        logger.error(f"Request failed for article {article}: {str(e)}")
        return {"status": "error", "message": str(e)}
    except ValueError as e:
        logger.error(f"Validation error for article {article}: {str(e)}")
        return {"status": "error", "message": str(e)}
    except Exception as e:
        logger.error(f"Error fetching product: {str(e)}")
        return {"status": "error", "message": str(e)}
