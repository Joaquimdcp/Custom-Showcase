from django.shortcuts import render
from django.template  import Template, Context, RequestContext
from django.shortcuts import render, render_to_response, redirect, get_object_or_404




def index(request):

    products_images = ["https://images.primark.com/productsimages/D35397143367554-large.jpg",
                       "https://d21vejvoh8fjtd.cloudfront.net/catalog/product/cache/all/640x640/da172be1e8bff2b08ca2554e2735c834/k/e/keepsake_remind_me_dress_1267-000028-0002-21.jpg",
                       "http://www.forever21.com/images/default_750/00176989-04.jpg",
                       "https://d21vejvoh8fjtd.cloudfront.net/catalog/product/cache/all/640x640/da172be1e8bff2b08ca2554e2735c834/r/u/rut_jessica_open_shoulder__cream-31193.jpg",
                       "https://d21vejvoh8fjtd.cloudfront.net/catalog/product/cache/1/small_image/800x1200/b8d43025c92f73f5eef1e8ee77bbc00a/r/o/roser_v-neck_romper_1276-100044-0146-8031-2_2_1.jpg",
                       "http://www.forever21.com/images/default_750/00250202-04.jpg"]

    return render_to_response('thumbs.html', {'product_images': products_images})