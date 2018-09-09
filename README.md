# django_token_session
像使用django的web session一样使用token对客户端进行会话管理

## 简述
web开发时，通常使用cookie来实现浏览器的会话管理，django已经对session提供了很好的支持。  
当需要对不支持cookie的客户端进行会话管理时，我们通常可以在客户端和服务端之间通过token来实现。  
在服务端基于django session可以非常方便的实现token会话管理，功能完备且与django session的使用方式一样。
