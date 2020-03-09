
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,
                                     initial-scale=1.0,
                                     maximum-scale=1.0,
                                     user-scalable=no">　
    <script src="https://code.jquery.com/jquery-git.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.0.272/jspdf.debug.js"></script>

    <!---更加合适的一定设备命名方式-->
    <title>Hello , together~ </title>　
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入 Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link href="mycss/style.css" 　type="text/css" rel="stylesheet">

    <!-- HTML5 Shiv 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
    <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <!-- jQuery (Bootstrap 的 JavaScript 插件需要引入 jQuery) -->
    <script src="https://code.jquery.com/jquery.js"></script>
    <!-- 包括所有已编译的插件 -->
    <script src="js/bootstrap.min.js"></script>
</head>

<body>
<script type="text/javascript">
    //验证注册表单
    function checkForm(){
        // 将需要验证表单组件 提供id属性
        var username = document.getElementById("uname").value;
        if(username==null||username==""){
            alert("用户名不能为空");
            return false;
        }
        // 为其它字段添加非空校验
        var password = document.getElementById("upwd").value;
        var repassword = document.getElementById("urepwd").value;
        if(password != repassword){
            alert("两次密码必须一致！");
            document.getElementById("upwd").value = "";
            document.getElementById("uname").value = "";
            document.getElementById("urepwd").value = "";
            return false;
        }else {
            $.get('<%=request.getContextPath()%>/checkuser',
                {uname:username,upwd:password},function (result) {// alert(result);
                    if (result == "error"){
                        $.post('<%= request.getContextPath()%>/adduser',{uname:username,upwd:password},function(result){
                            var n = new Number(result);
                            // alert(n);
                            if(n!=0){
                                alert("注册成功，5s后跳转到首页");
                                setTimeout('window.location="<%=request.getContextPath()%>/index"',5000);
                            }
                        });
                    }
                });
        }

    }
    // //切换验证码
    // function change(){
    // 	document.getElementById("myimg").src = "user/verifyCode?"+new Date().getTime();
    // }
</script>
<div class="container">
        <div class="form-group">
            <label class="col-sm-2 control-label" >用户名/user</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="uname" placeholder="Email" autocomplete="off"/>
            </div>
        </div>
        <%--            <div class="form-group">--%>
        <%--                <label for="inputEmail3" class="col-sm-2 control-label">电子邮件/Email</label>--%>
        <%--                <div class="col-sm-10">--%>
        <%--                    <input type="email" class="form-control" id="inputEmail3" placeholder="Email">--%>
        <%--                </div>--%>
        <%--            </div>--%>
        <div class="form-group">
            <label for="upwd" class="col-sm-2 control-label">密码/Password</label>
            <div class="col-sm-10">
                <input type="password" class="form-control" id="upwd" placeholder="Password" autocomplete="off"/>
            </div>
        </div>
        <div class="form-group">
            <label for="urepwd" class="col-sm-2 control-label">确认密码/Comfrim</label>
            <div class="col-sm-10">
                <input type="password" class="form-control" id="urepwd" placeholder="Password" autocomplete="new-password"/>
            </div>
        </div>
        <%--            <div class="form-group">--%>
        <%--                <label for="inputPassword3" class="col-sm-2 control-label">性别</label>--%>
        <%--                <div class="col-sm-10">--%>
        <%--                        <select class="form-control">--%>
        <%--                                <option>男</option>--%>
        <%--                                <option>女</option>--%>
        <%--                         </select>--%>
        <%--                </div>--%>
        <%--            </div>--%>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <input type="button" class="btn btn-default" onclick="checkForm()" value="提交"></input>
            </div>
        </div>

</div>

</body>
</html>
