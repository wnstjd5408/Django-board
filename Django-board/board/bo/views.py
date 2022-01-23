
from pyexpat.errors import messages
from django.http import request
from django.shortcuts import get_object_or_404
from .models import Board
# Create your views here.
from django.views import generic
from django.utils import timezone
from .forms import BoardForm
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# def index(request):
#     """
#     게시판 목록 출력
#     """
#     page = request.GET.get('page', '1') #페이지

#     #조회
#     board_list = Board.objects.order_by('-id')

#     #페이징처리
#     paginator = Paginator(board_list, 10) #페이지당 10개씩 보여주기

#     page_obj = Paginator.get_page(page)


#     context = {'page_obj': page_obj}
#     return render(request, 'bo/board_list.html', context)

# 메인 화면 리스트


class IndexView(generic.ListView):
    template_name = 'bo/board_list.html'
    context_object_name = 'board_list'
    model = Board
    paginate_by = 10  # 10개씩 리스트에 표시

    def get_queryset(self):
        return Board.objects.order_by('-id')


# def detail(request, board_id):
#     board = get_object_or_404(Board, pk=board_id)
#     context = {'board': board}
#     return render(request, 'bo/board_detail.html', context)


# Detail view
class DetailView(HitCountDetailView):

    model = Board
    template_name = 'bo/board_detail.html'
    count_hit = True
    context_object_name = 'my_board'

    def get_queryset(self):
        return Board.objects.filter(creation_date__lte=timezone.now())

    def get_context_data(self, **kwargs):

        context = super(DetailView, self).get_context_data(**kwargs)
        return context


@method_decorator(login_required, name="dispatch")
class BoardCreateView(generic.CreateView):

    form_class = BoardForm
    template_name = 'bo/board_create.html'
    success_url = '/'

    def form_valid(self, form):
        board = form.save(commit=False)
        board.author = self.request.user
        board.creation_date = timezone.now()
        board.ip = self.request.META['REMOTE_ADDR']
        board.save()
        messages.success(self.request, "포스팅을 완료했습니다.")
        return super(BoardCreateView, self).form_valid(form)


# def board_create(request):
#     """
#     게시글
#     글등록
#     """
#     if request.method == 'POST':
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             board = form.save(commit=False)
#             board.userid = request.user
#             board.creation_date = timezone.now()
#             board.ip = request.META['REMOTE_ADDR']
#             board.save()
#             return redirect('bo:index')
#     else:
#         form = BoardForm()
#     context = {'form': form}
#     return render(request, 'bo/board_create.html', context)

# 글 수정

@method_decorator(login_required, name="dispatch")
class BoardUpdateView(generic.UpdateView):
    model = Board
    context_object_name = 'board'
    form_class = BoardForm
    template_name = 'bo/board_update.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, "포스팅을 수정했습니다")
        return super().form_valid(form)

    def get_object(self):
        board = get_object_or_404(Board, pk=self.kwargs['pk'])
        return board

# def board_edit(request, pk):
#     board = Board.objects.get(id=pk)
#     if request.method == "POST":
#         form = BoardForm(request.POST)
#         board = form.save(commit=False)
#         board.modified_date = timezone.now()
#         board.title = request.POST['title']
#         board.comment = request.POST['comment']
#         board.save()
#         return redirect('bo:detail')
#     else:
#         boardForm = BoardForm
#     return render(request, 'bo/board_update.html', {'boardForm': boardForm})


@method_decorator(login_required, name="dispatch")
class BoardDeleteView(generic.DeleteView):
    model = Board
    context_object_name = 'board'
    success_url = reverse_lazy('bo:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
