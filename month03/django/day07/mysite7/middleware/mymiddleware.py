from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMW(MiddlewareMixin):
    visit_times = {}

    # def process_request(self, request):
    # print('process_request do')

    # def process_view(self,request,callback,callback_args,callback_kwargs):
    #     print('process_view do')
    #
    def process_response(self, request, response):
        ip = request.META['REMOTE_ADDR']
        path = request.path_info

        if not path.startswith('/test'):
            return response

        time = MyMW.visit_times.get(ip, 0)
        if time >= 5:
            return HttpResponse(f'{ip}访问/test超过5次！')
        self.visit_times[ip] = time+1
        print(f'{ip}第{self.visit_times[ip]}次请求访问/test')

        return HttpResponse(f'{ip}第{self.visit_times[ip]}次请求访问/test')


class MyMW2(MiddlewareMixin):
    pass
#     def process_request(self,request):
#         print('process_request2 do')
#
#
#     def process_view(self,request,callback,callback_args,callback_kwargs):
#         print('process_view2 do')
#
#     def process_response(self,request,response):
#         print('process_response2 do')
#         return response
