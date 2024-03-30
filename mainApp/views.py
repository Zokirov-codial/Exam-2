from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def talabalar_royxati(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar
    }
    return render(request, 'talaba_royxati.html', context)

def loyihalar_royxati(request):
    loyihalar = Loyiha.objects.all()
    context = {
        'loyiha': loyihalar
    }
    return render(request, 'loyiha_royxati.html', context)

def tugallanmagan_loyihalar(request):
    tugallanmagan = Loyiha.objects.filter(tugallangan=False)
    context = {
        'tugallanmagan': tugallanmagan
    }
    return render(request, 'tugallanmagan_loyihalar.html', context)

def uchinchi_kurs_talabalar(request):
    uchinchi_kurs = Talaba.objects.filter(kurs=3)
    context = {
        'uchinchi_kurs': uchinchi_kurs
    }
    return render(request, 'uchinchi_kurs.html', context)

def tanlangan_rejani_ochirib_yuborish(request, pk):
    reja = get_object_or_404(Loyiha, id=pk)
    reja.delete()
    message = "Reja muvaffaqiyatli o'chirildi."
    context = {
        'message': message
    }
    return render(request, 'message.html', context)

def talaba_rejalari(request, son):
    talaba = get_object_or_404(Talaba, id=son)
    rejalar = talaba.rejalar.all()
    context = {
        'talaba': talaba,
        'rejalar': rejalar
    }
    return render(request, 'talaba_rejalari.html', context)

def yangi_reja_qoshish(request):
    form = YangiRejaForm.objects.all()
    context = {
        'form': form
    }
    return render(request, 'yangi_reja_form.html', context)

def yoshi_kattalar(request):
    talabalar = Talaba.objects.filter(yosh__gt=20)
    context = {
        'talabalar': talabalar
    }
    return render(request, 'yoshi_kattalar.html', context)

def bitiruvchilar_rejalari(request):
    bitiruvchilar = Talaba.objects.filter(kurs=4)
    context = {
        'bitiruvchilar': bitiruvchilar
    }
    return render(request, 'bitiruvchilar_rejalari.html', context)


