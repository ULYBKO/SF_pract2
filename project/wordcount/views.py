from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            with uploaded_file.file.open('r') as file:
                content = file.read()
            uploaded_file.content = content
            uploaded_file.save()
            return redirect('wordcount:upload_file')
    else:
        form = FileUploadForm()
    
    return render(request, 'wordcount/upload_file.html', {'form': form})

def word_count(request, word):
    word_count = 0
    for uploaded_file in UploadedFile.objects.all():
        content = uploaded_file.content
        word_count += content.lower().count(word.lower())
    return render(request, 'wordcount/word_count.html', {'word': word, 'count': word_count})

def clear_memory(request):
    UploadedFile.objects.all().delete()
    return redirect('wordcount:upload_file')