# https://zhuanlan.zhihu.com/p/113312256
# 导入WordCloud及配置模块
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# 添加词频数据
words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
]

# WordCloud模块，链式调用配置，最终生成html文件
c = (
    WordCloud().add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND).set_global_opts(
        title_opts=opts.TitleOpts(title="WordCloud-shape-diamond")).render("wordcloud_diamond.html")
)
