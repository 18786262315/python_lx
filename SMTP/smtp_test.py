from email.mime.text import MIMEText
import smtplib
import yagmail

# 链接邮箱服务器
host = 'smtp.qq.com'  # 设置服务器
mail_user = "ycc843092012@gmail.com"  # 用户名
mail_pwd = "zlamhlqmvtbybcgb"  # 口令
# 此处的password是授权码
sender = '*******@163.com'
receivers = '843092012@qq.com'


yag = yagmail.SMTP(user="843092012@qq.com",
                   password="zlamhlqmvtbybcgb", host='smtp.qq.com')

# 邮箱正文

contents = [
    '''
    <div>
        <h2>The Iveria (D09)</h2>
    </div>

            <div id="container" style="height: 300px"></div>



    
    <div>
        <h2>#UNITS BY TYPE</h2>
        <table border="0" class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1' align="center">
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>

    <div>
        <h2>#PRICE BY TYPE(AVAIL)</h2>
        <table class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1' align="center">
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>

    <div>
        <h2>#UNITS BY BLOCK/PHASE</h2>
        <table class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1' align="center">
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>

    <div>
        <h2>#PRICE BY BLOCK/PHASE(AVAIL)</h2>
        <table class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1' align="center">
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>

    <div>
        <h2>#UNITS BY FLOOR PLAN</h2>
        <table class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1' align="center">
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>

    <div>
        <h2>#UNITS BY BEDROOMS</h2>
        <table class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1' align="center">
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>
    <div>
        <h2>#PRICE BY BEDROOM(AVAIL)</h2>
        <table class="table_1" bgcolor="#f1f1f2" cellpadding="10" cellspacing='1'>
            <tr bgcolor="#fff">
                <th>Type</th>
                <th>Reserved</th>
                <th>Sold</th>
                <th>Available</th>
                <th>Total</th>

            </tr>
            <tr align="center">
                <td>3bremer</td>
                <td></td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
            <tr align="center">
                <td></td>
                <td>0</td>
                <td>9</td>
                <td>45</td>
                <td>54</td>
            </tr>
        </table>
    </div>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>

    <style>
        table{
    font-size: 40px;
    width: 95%
}
</style>
    <script type="text/javascript" >
        var dom = document.getElementById("container");
        var myChart = echarts.init(dom);
        var data_1 = ['Sold: 16.67%(30)', 'Available: 83.33%(45)', 'Reserved: 0%(0)']
        var data_2 = [
                        { value: 30, name: 'Sold: 16.67%(30)' },
                        { value: 40, name: 'Available: 83.33%(45)' },
                        { value: 0, name: 'Reserved: 0%(0)' }

                    ]
        option = null;
        option = {
            textStyle: {
                        fontSize: '30',
                        fontWeight: 'bold'
                    },
            legend: {
                orient: 'vertical',
                right: 100,
                top: 'middle',
                data: ['Sold: 16.67%(30)', 'Available: 83.33%(45)', 'Reserved: 0%(0)']
            },
            series: [
                
                {
                    name: '访问来源',
                    type: 'pie',
                    right: 200,
                    radius: ['50%', '75%'],
                    data: [
                        { value: 30, name: 'Sold: 16.67%(30)' },
                        { value: 40, name: 'Available: 83.33%(45)' },
                        { value: 0, name: 'Reserved: 0%(0)' }

                    ]
                }
            ]
        };

        if (option && typeof option === "object") {
            myChart.setOption(option, true);
        }
    </script>


    ''']
# 发送邮件

# yag.send('843092012@qq.com','test 邮件发送', contents)

# 四行代码完工，简单吧

# 给多个用户发送邮件

# yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'],'subject', contents)

# # 发送邮件带附件

yag.send('843092012@qq.com', '发送附件', contents, [
         "E:\新联国际\地产项目\web页面\邮件模板\summary.html"])
