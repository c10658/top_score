from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer


@api_view(['GET', 'POST'])
def my_upload(request):
    """
    接口1: 上传分数
    """
    if request.method == 'GET':
        # 获取请求参数
        client_no = '客户端' + request.GET.get('client')
        score = request.GET.get('score')
        data = {'client': client_no, 'score': score}

        # 判断是否新客户端并保存分数
        client = Client.objects.filter(client=client_no)
        if client:
            ser = ClientSerializer(client[0], data=data)
        else:
            ser = ClientSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'code': 200, 'msg': 'ok', 'data': ser.data})
    else:
        return Response({'code': 400, 'msg': 'fail', 'data': ''})


@api_view(['GET', 'POST'])
def my_list(request):
    """
    接口2: 查看排行榜
    """
    if request.method == 'GET':
        # 获取请求参数
        client_no = '客户端' + request.GET.get('client')
        start_st = request.GET.get('start_st')
        end_st = request.GET.get('end_st')

        # 计算当前完整排行榜,格式[(排名,客户端,分数),(),...]
        res_ = []
        clients = Client.objects.order_by('-score')
        for i in range(len(clients)):
            res_.append((i + 1, clients[i].client, clients[i].score))

        # 截取出需要的结果集,最后拼接当前的客户端
        res = (res_[int(start_st) - 1:int(end_st)])
        for i in res_:
            if i[1] == client_no:
                res.append(i)
                break
        return Response(res)
    else:
        return Response('请求有误')
