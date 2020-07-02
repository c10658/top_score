from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Client


# Create your tests here.

class TopTest(TestCase):
    # 初始化测试数据
    def setUp(self):
        Client.objects.create(client='客户端a', score=9)
        Client.objects.create(client='客户端b', score=18)
        Client.objects.create(client='客户端c', score=27)
        Client.objects.create(client='客户端d', score=36)
        Client.objects.create(client='客户端e', score=45)

    # 验证接口1: 上传分数
    def test_upload_view_status_code(self):
        url = reverse('upload')
        data = {
            'client': 'f',
            'score': 54,
        }
        response = self.client.get(url, data)
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response.data, 1)

    # 验证接口2: 查看排行榜
    def test_list_view_status_code(self):
        url = reverse('list')
        data = {
            'client': 'a',
            'start_st': 2,
            'end_st': 4
        }
        response = self.client.get(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[-1][1:], ('客户端a', 9))
