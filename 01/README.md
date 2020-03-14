# 第1章 初识Flask

搭建开发环境，编写一个最小的Flask程序并运行它，了解 Flask基本知识

这一切开始于2010年4月1日，Armin Ronacher在网上发布了一篇关 于“下一代Python微框架”的介绍文章，文章里称这个Denied框架不依赖 Python标准库，只需要复制一份deny.py放到你的项目文件夹就可以开始 编程。伴随着一本正经的介绍、名人推荐语、示例代码和演示视频，这 个“虚假”的项目让不少人都信以为真。

5天后， [Flask](http://flask.pocoo.org/)就从这么一个愚人节玩笑诞生了。

Flask是使用Python编写的Web微框架。Web框架可以让我们不用关 心底层的请求响应处理，更方便高效地编写Web程序。因为Flask核心简 单且易于扩展，所以被称作微框架（micro framework）。Flask有两个主 要依赖，一个是[WSGI（Web Server Gateway Interface，Web服务器网关 接口）工具集——Werkzeug](http://werkzeug.pocoo.org/)，另一个是 [Jinja2模板引擎](http://jinja.pocoo.org/)。Flask只保留了Web开发的核 心功能，其他的功能都由外部扩展来实现，比如数据库集成、表单认 证、文件上传等。如果没有合适的扩展，你甚至可以自己动手开发。 Flask不会替你做决定，也不会限制你的选择。总之，Flask可以变成任 何你想要的东西，一切都由你做主。

Flask（瓶子，烧瓶）的命名据说是对另一个Python Web框架—— Bottle的双关语/调侃，即另一种容器（另一个Python Web框架）。 Werkzeug是德语单词“工具（tool）”，而Jinja指日本神社，因为神社 （庙）的英文temple与template（模板）相近而得名。

WSGI（Web Server Gateway Interface）是Python中用来规定Web服 务器如何与Python Web程序进行沟通的标准，在本书的第三部分将进行 详细介绍。

