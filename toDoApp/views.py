from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToDoModelForm
from .models import ToDoModel
# Create your views here.


# class ToDoView(View):
#     model = ToDoModel
#
#     def get(self, request, *args, **kwargs):
#         form = ToDoModelForm()
#         queryset = ToDoModel.objects.all()
#         context = {
#             'object_list': queryset,
#             'form': form
#         }
#         return render(self.request, 'main_page.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = ToDoModelForm(request.POST or None)
#         print("here 1 -------------- ")
#         if form.is_valid():
#             form.save()
#             return redirect('./')
#         context = {
#             'form': form
#         }
#         return render(self.request, 'main_page.html', context)
#
#     def post(self, request, pk, *args, **kwargs):
#         obj = get_object_or_404(ToDoModel, id=pk)
#         form = ToDoModelForm(request.POST, instance=obj)
#         print("We are here 2 ------- " + pk)
#         if form.is_valid():
#             form.save()
#             return redirect('./')
#         context = {
#             'form': form
#         }
#         return render(self.request, 'main_page.html', context)


def main_view(request, *args, **kwargs):
    form = ToDoModelForm()
    queryset = ToDoModel.objects.all()
    if request.method == 'POST':
        form = ToDoModelForm(request.POST)
        if form.is_valid():
            form.save()
            # form = ToDoModelForm()
        return redirect('./')

    return render(request, 'main_page.html', {'object_list': queryset, 'form': form})


def update_view(request, pk):
    obj = get_object_or_404(ToDoModel, id=pk)
    obj.is_done = True
    obj.save()
    return redirect('../')


def delete_view(request, pk):
    obj = get_object_or_404(ToDoModel, id=pk)
    obj.delete()
    return redirect('../')
