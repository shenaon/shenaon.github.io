import pandas as pd

data = [
    [45939, 21574, 2876, 1815, 1646, 89, 555],
    [60423, 29990, 4708, 2568, 2366, 1411, 733],
    [64721, 32510, 5230, 2695, 2526, 1546, 773],
    [68484, 35218, 6662, 2845, 2691, 1663, 836],
    [71799, 37598, 6856, 3000, 2868, 1769, 911],
    [76036, 40341, 8220, 3145, 3054, 1905, 1008],
    [79831, 43173, 9053, 3338, 3224, 2005, 1076],
]

data = pd.DataFrame(
    data=data,
    index=[1951, 1956, 1957, 1958, 1959, 1960, 1961],
    columns=["N.Amer", "Europe", "Asia", "S.Amer", "Oceania", "Africa", "Mid.Amer"],
)

data

import io, base64
from flask import Markup

images = {}
for col in data.columns:
    img = io.BytesIO()
    data.plot.bar(y=col).get_figure().savefig(img, format='png');
    img.seek(0)
    image_decode = base64.b64encode(img.getvalue()).decode()
    images[col] = Markup('<img src="data:image/png;base64,{}">'.format(image_decode))


from jinja2 import Template

str = open("templates/index.html", "r").read()
template = Template(str)
str = template.render(region_names=data.columns, images=images)
open("index.html", "w").write(str);