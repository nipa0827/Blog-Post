from PIL import Image
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
import imutils
import pytesseract
# Create your views here.
'''
tesseract_cmd = "C:\\Users\\Leads\\Anaconda3\\pkgs\\pytesseract-0.1.7-py36_0"
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Leads\\Anaconda3\\pkgs\\pytesseract-0.1.7-py36_0"
TESSDATA_PREFIX= "C:\\Users\\Leads\\Anaconda3\\pkgs"
tessdata_dir_config = '--tessdata-dir "C:\\Users\\Leads\\Anaconda3\\pkgs\\pytesseract-0.1.7-py36_0\\tessdata"'
print(pytesseract.image_to_string(Image.open('C:\\djangoProject\\banglaidj\\blog_post\\thres.png'), lang='eng', config=tessdata_dir_config))
'''
def home(request):
    return render(request,'index.html',{'all_post_lists':"Suravi",'disctrict':"Kishoreganj"})

def contact(request):
    return render(request,'contact.html')

def all_posts(request):
    posts = Post.objects.all()
    return render(request,'all_post.html',{'all_post_lists':posts})

def single_post(request,post_id):
    post = Post.objects.get(pk=post_id)

    return render(request,'single_post.html',{'post':post})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'all_post.html'
    success_url = reverse_lazy('all_posts')