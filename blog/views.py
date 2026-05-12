from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Chat, Message
from user.models import User
# class ChatAPI(generics.ListCreateAPIView):
#     serializer_class = ChatSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return Chat.objects.filter(participants=self.request.user)
#
#     def perform_create(self, serializer):
#         chat = serializer.save()
#         chat.participants.add(self.request.user)
#
# class MessageAPI(generics.ListCreateAPIView):
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return Message.objects.filter(chat_id=self.kwargs['chat_id'], chat__participants=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(sender=self.request.user, chat_id=self.kwargs['chat_id'])

#
# class ChatListView(LoginRequiredMixin, ListView):
#     model = Chat
#     template_name = 'chats/chat_list.html'
#     context_object_name = 'chats'
#     def get_queryset(self):
#         return Chat.objects.filter(participants=self.request.user)
#
# class MessageListView(LoginRequiredMixin, ListView):
#     model = Message
#     template_name = 'chats/message_list.html'
#     context_object_name = 'messages'
#     def get_queryset(self):
#         return Message.objects.filter(chat_id=self.kwargs['chat_id'], chat__participants=self.request.user)

def chat_list(request):
    # Login qilmagan user chatlarni ko'rmasin.
    if not request.user.is_authenticated:
        return redirect('login')

    # Hozirgi user qatnashgan chatlarni olamiz.
    chats = Chat.objects.filter(participants=request.user)
    context = {'chats': chats}

    # Formadan username kelsa, yangi chat ochamiz yoki eski chatga o'tkazamiz.
    if request.method == "POST":
        # Template ichidagi name="username" qiymatini olamiz.
        username = request.POST.get('username')

        # Username orqali ikkinchi userni topamiz.
        other_user = get_object_or_404(User, username=username)

        # User o'ziga o'zi chat ochmasin.
        if other_user == request.user:
            return redirect('chat_list')

        # Shu ikki user orasida oldin chat bor-yo'qligini tekshiramiz.
        chat = Chat.objects.filter(participants=request.user).filter(participants=other_user).first()

        # Eski chat bor bo'lsa, yangi chat yaratmaymiz.
        if chat:
            return redirect('chat_messages', chat_id=chat.id)

        # Eski chat yo'q bo'lsa, yangi chat yaratamiz.
        chat = Chat.objects.create(name=f'{request.user.username}-{other_user.username}')

        # Yangi chat ichiga ikkala userni qo'shamiz.
        chat.participants.add(request.user, other_user)

        # Yangi chat sahifasiga o'tkazamiz.

        return redirect('chat_messages', chat_id=chat.id)

    # POST bo'lmasa, oddiy chatlar ro'yxatini ko'rsatamiz.
    return render(request, 'chat_list.html', context,)

def message(request, chat_id):
    if not request.user.is_authenticated:
        return redirect('login')

    # Chatni faqat shu chatda qatnashgan user ochishi mumkin.
    chat = get_object_or_404(Chat, id=chat_id, participants=request.user)

    # Xabar yuborilganda POST ishlaydi.
    if request.method == 'POST':
        # Formadan textni olib, bosh/oxiridagi bo'sh joylarni olib tashlaymiz.
        text = request.POST.get('text', '').strip()

        # Text bo'sh bo'lmasa va user login qilgan bo'lsa, xabar saqlanadi.
        if text and request.user.is_authenticated:
            Message.objects.create(chat=chat, sender=request.user, text=text)
            return redirect('chat_messages', chat_id=chat.id)

    # Shu chatdagi xabarlarni sender bilan birga olamiz.
    messages = chat.messages.all().select_related('sender')
    context = {'chat': chat, 'messages': messages}
    if request.method == "POST":
        chat = get_object_or_404(Chat, id=chat_id)
        chat.delete()
        return redirect('chat_list')

    # Chat xabarlari sahifasini ko'rsatamiz.
    return render(request, 'message_list.html', context)

def update(request, chat_id):
    if not request.user.is_authenticated:
        return redirect('login')
    #bunyerda shu id ga teng bolgan malumotni oladi
    instance = Message.objects.get(id=chat_id)

    if instance.sender == request.user:
        if request.method == "POST":
            #tugma boliganda malumotni oladi yani forontdan kelgan malumot
            text = request.POST.get('text', '').strip()
            #
            instance.text = text
            instance.save()
            return redirect('chat_messages', chat_id=instance.chat.id)

        if request.method == "POST":
            instance = Message.objects.get(id=chat_id)
            instance.delete()
            return redirect('chat_messages', chat_id=instance.chat.id)
    else:
        return redirect('chat_messages', chat_id=instance.chat.id)
    return render(request, 'edit.html', {'message': instance})

def porofil(request, chat_id):
    if not request.user.is_authenticated:
        return redirect('login')

    userdatab = get_object_or_404(User, id=chat_id)
    context = {
        'userdatab': userdatab,
    }
    return render(request, 'porofil.html',context)

def porfiledit(request ,chat_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'ProfilEdit.html')

def logout_page(request):
    logout(request)
    return redirect('login')
