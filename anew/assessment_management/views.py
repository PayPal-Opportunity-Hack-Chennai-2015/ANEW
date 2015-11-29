from django.shortcuts import render
from django.contrib.auth import authenticate, logout as lg
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from chartjs.views.lines import BaseLineChartView
from .forms import ChooseStudentForm
from chartjs.views.columns import BaseColumnsHighChartsView
from .models import Assessment


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'error': 'Sorry! username & password mismatch'})
        else:
            auth.login(request, user)
            return HttpResponseRedirect('dashboard')
    return render(request, 'login.html', {})


@login_required
def dashboard(request):
    current_user = "{0} {1}".format(request.user.first_name, request.user.last_name)
    if request.method == 'POST':
        print Assessment.objects.filter(
            student_batch__student__user__id=int(request.POST.get('student')),
            student_batch__batch__id=int(request.POST.get('batch')))
        return render(request, 'dashboard.html', {
        'logged_in_user': current_user,
        'form': ChooseStudentForm(user=request.user),
        'report_data': True
        })
    return render(request, 'dashboard.html', {
        'logged_in_user': current_user,
        'form': ChooseStudentForm(user=request.user)
    })


def logout(request):
    lg(request)
    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
    return HttpResponseRedirect('/')


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["Theory", "Practicals", "Presentation Skills", "Punctuality",
                "Attitude", "Class Participation", "Commitment", "English Fluency"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[100, 20, 50, 76, 83, 72, 19, 65],
                [80, 60, 30, 46, 43, 100, 80, 45],
                [95, 60, 50, 66, 63, 80, 99, 100]]


class ColumnHighChartJSONView(BaseColumnsHighChartsView):
    title = 'Test'
    yUnit = '%'
    providers = ['All']
    credits = {"enabled": False}

    def get_labels(self):
        """Return 7 labels."""
        return ["Theory", "Practicals", "Presentation Skills", "Punctuality",
                "Attitude", "Class Participation", "Commitment", "English Fluency"]

    def get_data(self):
        return [[75, 44, 92, 11, 44, 95, 35, 89],]


line_chart_json = LineChartJSONView.as_view()
column_highchart_json = ColumnHighChartJSONView.as_view()