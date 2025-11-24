def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('school:school-home')  # змінити на вашу сторінку
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Невірний логін або пароль'
                })
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
