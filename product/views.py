from django.shortcuts import render

def shop(request):
    return render(request, "product/shop.html")

def compare(request):
    return render(request, "product/compare.html")

def product_detail(request, id):
    return render(request, "product/product.html")

def blog(request):
    return render(request, "product/blog.html")

def blog_single(request):
    return render(request, "product/blog-single.html")