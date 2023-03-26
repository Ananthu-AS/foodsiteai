from django.shortcuts import render
import openai, os
from dotenv import load_dotenv

from Myapp.models import Foodtype, Meals, variety

# Create your views here.
load_dotenv()
api_key=os.getenv("OPENAI_KEY",None)

def recipie(request):
    data=variety.objects.all()
    data1=Foodtype.objects.all()
    data2=Meals.objects.all()
    new_response=[]
    chatbot_response=None
    # items={}
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input1= request.POST.get('user_input1')
        user_input2= request.POST.get('user_input2')
        user_input3= request.POST.get('user_input3')
        print(user_input3)
        user_input="List of" +" " + user_input1 + " strictly " + user_input2 + " dishes for " + user_input3
        print(user_input)
        prompt = user_input
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=120,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        chatbot_response = response["choices"][0]["text"]
        print(chatbot_response)
        new_response = chatbot_response.splitlines()
        print(new_response)
        
    return render(request,'index.html',{'response':new_response,'data':data,'data1':data1,'data2':data2, })


   