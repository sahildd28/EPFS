from gettext import find
from selenium import webdriver
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from selenium import webdriver


def home(request):
    return render(request,"home.html")

    
def button_click(request):
    options=webdriver.ChromeOptions()
    options.add_argument('headless') 
    browser=webdriver.Chrome(options=options)
    browser.get("https://www.amazon.in/")
    browser.implicitly_wait(5)
    browser.maximize_window()
    m_input=request.POST.get('main_input') 
    main_input=m_input 
    search1=browser.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
    if m_input:
        search1.send_keys(m_input)
    else:
        search1.send_keys(main_input)
    submit1=browser.find_element_by_css_selector("#nav-search-submit-button")
    submit1.submit()  
    item_name=browser.find_element_by_css_selector(".a-size-medium.a-color-base.a-text-normal").text
    item_price_discount=browser.find_element_by_css_selector(".a-row.a-size-base.a-color-base").text
    item_star=browser.find_element_by_class_name("a-icon-alt").text
    item_ratings=browser.find_element_by_css_selector(".a-size-base.s-underline-text").text+" Reviews"
    item_offer=browser.find_element_by_css_selector(".a-color-base.a-text-bold").text
    item_delivery="FREE Delivery by Amazon for PRIME MEMBERS"
    item_image=browser.find_element_by_class_name("s-image")
    item_image_final=item_image.get_attribute('src')
    item_information_submit=browser.find_element_by_css_selector(".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    item_information_submit_final=item_information_submit.get_attribute('href')
    # item_link=browser.current_url
    context = {
        "main_input" : "Results for: "+m_input,
        "item_name":item_name,
        "item_price_discount":item_price_discount,
        "item_star":item_star,
        "item_ratings":item_ratings,
        "item_offer":item_offer,
        "item_delivery":item_delivery,
        "item_image":item_image_final,
        "item_link":item_information_submit_final,
    }
    return render(request,"base.html",context)
    
  

def about(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone , desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your information has been sent!')

    return render(request,'index.html')

def base(request):
    def dosomething():
        print("Hello world")
    return render(request,"base.html")