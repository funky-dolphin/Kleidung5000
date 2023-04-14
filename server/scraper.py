from bs4 import BeautifulSoup
import requests


url = 'https://www.ssense.com/en-us/men/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
}

response = requests.get(url, headers=headers)

#find product containers
if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')
    product_containers = soup.find_all('figure', class_= 'browsing-product-card')

    for product in product_containers:
        product_name = product.find('span', class_='browsing-product-card__name').text.strip()
        product_brand = product.find('span', class_='browsing-product-card__brand').text.strip()
        product_price = product.find('span', class_='browsing-product-card__price').text.strip()
        image_url = product.find('img', class_='product-tile__image')['src']

        print(f'Product Name: {product_name}')
        print(f'Product Brand: {product_brand}')
        print(f'Product Price: {product_price}')
        print(f'Product Image: {image_url}')

else:
    print(f'Failed to retrieve the website. HTTP status code: {response.status_code}')
        



# headers =  {'user-agent': 'my-app/0.0.1'}
# html = requests.get('https://www.ssense.com/en-us/men/jeans', headers=headers)

# doc = BeautifulSoup(html.text, 'html.parser')

# print(doc)



