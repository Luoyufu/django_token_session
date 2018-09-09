# django_token_session

像使用django的web session一样使用token对客户端进行会话管理


### 简述

web开发时，通常使用cookie来实现浏览器的会话管理，django已经对session提供了很好的支持。  
当需要对不支持cookie的客户端进行会话管理时，我们通常可以在客户端和服务端之间通过token来实现。  
在服务端基于django session可以非常方便的实现token会话管理，功能完备且与django session的使用方式一样。


### 使用  

将token_middleware配置到django settings.py中。  
客户端每次请求在header的Access-Token字段中带上token。  
token_middleware会更加token_session的状态自动保存所做的修改。

- 为客户端分配token:

```
def insert_session_view(request):  
    request.token_session.create_token()
    ...
    
    return JsonResponse({'token': request.token_session.token})
```

- 在view中为token session添加内容：

```
def insert_session_view(request):  
    request.token_session['my_session_key'] = 'my_session_value'
    ...
```    

- 在view中获取token session中的内容：  

```
def get_session_view(request):  
    my_session_value = request.token_session['my_session_key']
    ...
```

- 在view中删除token session中的内容：  

```
def delete_session_view(request):  
    del request.token_session['my_session_key']
    ...
```
