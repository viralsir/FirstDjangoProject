from django.shortcuts import render,redirect

# Create your views here.
tasklist=['Pay Power Bill',"Recharge Mobile","Purchase Radio","Review Code"]

def home(request):
    return render(request,"task/home.html",{"tasklist":tasklist})

def addTask(request):
    if request.method == "POST":
        task = request.POST["task"]
        tasklist.append(task)
        return redirect("task-home")
    else :
        return render(request,"task/addTask.html")