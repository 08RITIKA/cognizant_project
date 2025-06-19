def search_products(product_list, query):
    result = []
    for product in product_list:
        if query.lower() in product.lower():
            result.append(product)
    return result

# Example
products = ['iPhone 14', 'Samsung S22', 'MacBook Air', 'Dell Inspiron']
print(search_products(products, 'mac'))  # Output: ['MacBook Air']