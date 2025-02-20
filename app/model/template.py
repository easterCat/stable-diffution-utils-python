from datetime import datetime

from app import db
from app.utils import format_datetime


class BaseTemplate(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(120), default="")
    preview = db.Column(db.Text(300), default="")
    prompt = db.Column(db.Text(3000), nullable=False)
    prompt_zh = db.Column(db.Text(3000), default="")
    n_prompt = db.Column(db.Text(3000), default="")
    n_prompt_zh = db.Column(db.Text(3000), default="")
    step = db.Column(db.String(60), default="")
    sampler = db.Column(db.String(80), default="")
    scale = db.Column(db.String(60), default="")
    seed = db.Column(db.String(60), default="")
    skip = db.Column(db.String(60), default="")
    size = db.Column(db.String(60), default="")
    model = db.Column(db.Text(300), default="")
    path = db.Column(db.Text(300), default="")
    desc = db.Column(db.Text(300), default="")
    like = db.Column(db.Integer, default=0)
    category = db.Column(db.String(80), default="")
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())
    template_from = db.Column(db.String(30), default="")
    key_word = db.Column(db.String(30), default="")
    key_word2 = db.Column(db.String(30), default="")
    images = db.Column(db.Text(3000), default="")
    file1 = db.Column(db.Text(300), default="")
    file2 = db.Column(db.Text(300), default="")
    file3 = db.Column(db.Text(300), default="")
    imgbb_url = db.Column(db.Text(300), default="")
    min_imgbb_url = db.Column(db.Text(300), default="")

    def __init__(self, *args, **kwargs):
        self.set_args(**kwargs)

    def set_args(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_json(self):
        if 'https://' not in self.preview:
            self.preview = self.preview.replace("http://", "https://")
        if "/original_i2i/" in self.preview:
            minify_preview = self.preview.replace("/original_i2i/", "/min_original_i2i/")
        elif "/hanwang_20221229/" in self.preview:
            minify_preview = self.preview.replace("/hanwang_20221229/", "/min_hanwang_20221229/")
        elif "/chi_tu/" in self.preview:
            minify_preview = self.preview.replace("/chi_tu/", "/min_chi_tu/")
        else:
            minify_preview = self.preview.replace("/original/", "/min_original/")

        json_data = {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }

        json_data["minify_preview"] = minify_preview
        json_data['create_time'] = format_datetime(json_data['create_time'])
        json_data['update_time'] = format_datetime(json_data['update_time'])
        return json_data


class TemplateHan(BaseTemplate):
    __tablename__ = "template_han"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TemplateChitu(BaseTemplate):
    __tablename__ = "template_chitu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TemplateTest(BaseTemplate):
    __tablename__ = "template_test"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TemplateStable(BaseTemplate):
    __tablename__ = "template_stable"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TemplateNoval(BaseTemplate):
    __tablename__ = "template_noval"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TemplatePersonal(BaseTemplate):
    __tablename__ = 'template_personal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
