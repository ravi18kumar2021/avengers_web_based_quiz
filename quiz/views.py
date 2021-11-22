from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def check_answer(request):
    data = {
        'first' : ['Tony', 'Iron'],
        'second' : ['Thor',],
        'third' : ['Captain America', 'Capt America'],
        'forth' : ['Hulk',],
        'fifth' : ['Antman', 'Ant Man']
    }
    right = 0
    wrong = 0
    null = 0
    score = 0

    if request.method == 'POST':
        one = request.POST.get('1')
        two = request.POST.get('2')
        three = request.POST.get('3')
        four = request.POST.get('4')
        five = request.POST.get('5')
        
        if one != None:
            if one in data['first']:
                right += 1
                score += 10
            else:
                wrong += 1
                if score >= 5:
                    score -= 5
        else:
            null += 1

        if two != None:
            if two in data['second']:
                right += 1
                score += 10
            else:
                wrong += 1
                if score >= 5:
                    score -= 5
        else:
            null += 1

        if three != None:
            if three in data['third']:
                right += 1
                score += 10
            else:
                wrong += 1
                if score >= 5:
                    score -= 5
        else:
            null += 1

        if four != None:
            if four in data['forth']:
                right += 1
                score += 10
            else:
                wrong += 1
                if score >= 5:
                    score -= 5
        else:
            null += 1

        if five != None:
            if five in data['fifth']:
                right += 1
                score += 10
            else:
                wrong += 1
                if score >= 5:
                    score -= 5
        else:
            null += 1

        context = {
            'data' : data, 
            'right' : right, 
            'wrong' : wrong, 
            'null' : null,
            'score' : score}

    return render(request, 'result.html', context)