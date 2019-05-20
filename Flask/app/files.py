import os,time
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = R'static\imgs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])  # 允许上传的文件后缀

# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 具有上传功能的页面
@app.route('/test/upload')
def upload_test():
    htm = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form id="form1" method="post" action="http://127.0.0.1:7777/api/upload" enctype="multipart/form-data">
    <div>
        <input id="File1" type="file" name="myfile"/>  <!--后台代码中获取文件是通过form的name来标识的-->
        <input type="submit">提交</input>
    </div>
</form>
</body>
</html>
"""
    return htm

@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])  # 拼接成合法文件夹地址
    # print(file_dir)
    if not os.path.exists(file_dir):
        # print('--->创建文件夹')
        os.makedirs(file_dir)  # 文件夹不存在就创建
    f=request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    # print('文件名称：%s'%f)
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname=f.filename
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time)+'.'+ext   # 修改文件名
        f.save(os.path.join(file_dir, new_filename))  #保存文件到upload目录

        return jsonify({"errno": 0, "errmsg": "上传成功","file_name":"%s"%(new_filename)})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})




@app.route("/download/<path:filename>")
def downloader(filename):
    # print(filename)
    dirpath = os.path.join(app.root_path, 'upload')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    # print(dirpath)    
    return send_from_directory(dirpath, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载


app.run(debug = True,port=7777,host='0.0.0.0')