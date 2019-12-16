from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.globals import SymbolType
import os,json
import math
import random
from pyecharts.faker import Faker
def polar_scatter0():
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = (
        Polar()
        .add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter0"))
    )
    return c

polar_scatter0().render()



