# 1、创建logger实例
import logging

logger = logging.getLogger('simple_example')
# 2、设置日志级别
logger.setLevel(logging.DEBUG)
# 3、使用流处理器输出
ch = logging.StreamHandler()  # StreamHandler() 用于将日志消息以标准输出流的格式(sys.stdout)输出
ch.setLevel(logging.DEBUG)
# 4、设置日志打印格式： 打印日志时间--当前模块名--日志级别--日志信息
formatter = logging.Formatter \
    ('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# 5、添加格式配置
ch.setFormatter(formatter)
# 6、添加日志配置
logger.addHandler(ch)
