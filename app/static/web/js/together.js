// function Personal_space() {
//     window.location.href = "<%=request.getContextPath()%>/person_space";
// }

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

$(document).ready(function () {
  var trigger = $('.hamburger'),
    overlay = $('.overlay'),
    isClosed = false;

  trigger.click(function () {
    hamburger_cross();
  });

  function hamburger_cross() {

    if (isClosed == true) {
      overlay.hide();
      trigger.removeClass('is-open');
      trigger.addClass('is-closed');
      isClosed = false;
    } else {
      overlay.show();
      trigger.removeClass('is-closed');
      trigger.addClass('is-open');
      isClosed = true;
    }
  }

  $('[data-toggle="offcanvas"]').click(function () {
    $('#wrapper').toggleClass('toggled');
  });
});

/**
 * 
 * @param {*} url 请求的地址
 * @param {*} fields 提交的字段
 * @param {*} redirect_url  跳转的地址
 * jquery的语法
 */
function request(url, fields, redirect_url) {
  $("#btn-sub").click(function () {
    console.log("into btn-sub")
    //对表单进行序列化
    var data = $("#form-data").serialize();
    $.ajax({
      type: "post", //请求方式
      url: url, //请求的接口地址
      data: data,
      dataType: "json",
      success: function (res) {
        console.log(res)
        if (res.code == 1) {
          //成功跳转
          location.href = redirect_url
        } else {
          //失败信息的展示
          var error = res.data;
          for (var index in fields) {
            var key = fields[index];
            if (typeof error[key] === 'undefined') {
              $("error_" + key).empty();

            } else {
              $("#error_" + key).empty();
              $("#error_" + key).apppend(
                error[key]
              )
            }
          }
        }
      },
    });

  })
}

function  login(url, fields, redirect_url) {
  alert(typeof (fields)+fields);
  $("#btn-sub").click(function () {
    console.log("into btn-sub")
    //对表单进行序列化
    var data = $("#form-data").serialize();
    $.ajax({
      type: "post", //请求方式
      url: url, //请求的接口地址
      data: data,
      dataType: "json",
      success: function (res) {
        console.log(res)
        if(res.code == 1) {
          alert("登录成功");
          //修改显示的模块
          // $("#info_login").html("欢迎你" + res.user.mail);
          $("#user_info").html(res.user.mail);
          $("#no_login").css("display", "none");
          $("#haved_login").css("display", "block");
          // $("#id01").css("display","block");
          //成功跳转
          // location.href = redirect_url;
        } else {
          //失败信息的展示
          var error = res.data;
          // alert("error"+error)
          for (var index in fields) {
            var key = fields[index];
            if(error[key]!=undefined){
               alert("错误提示"+error[key]);
            }
          }
        }
      },
    });

  })
}
//加载file的组建

//文件上传by fucker
function file_upload(url, fields, redirect_url) {
  $("#text_file").fileinput({
    theme: 'fas',
    uploadUrl: url, // you must set a valid URL here else you will get an error
    allowedFileExtensions: ['jpg', 'png', 'gif'],
    overwriteInitial: false,
    maxFileSize: 1000,
    maxFilesNum: 10,
    //allowedFileTypes: ['image', 'video', 'flash'],
    slugCallback: function (filename) {
      return filename.replace('(', '_').replace(']', '_');
    },
    uploadExtraData: function () {
      console.log("uploadExtraData")
      return {
        _xsrf: $("input[name='_xsrf']")[0].value
      }
    }

  });
  $("#btn-data").click(function () {
    console.log("into file_upload")
    //对表单进行序列化
    var data = $("#form-file-data").serialize();
    console.log(data)
    $.ajax({
      type: "post", //请求方式
      url: url, //请求的接口地址
      data: data,
      success: function (res) {
        console.log("成功")
      }

    });
  });
}

// 文件上传
//初始化fileinput
var FileInput = function () {
  var oFile = new Object();

  //初始化fileinput控件（第一次初始化）
  oFile.Init = function (ctrlName, fields, uploadUrl) {
    console.log($("input[name='_xsrf']")[0].value + "fucker")
    var control = $('#' + ctrlName);

    //初始化上传控件的样式
    control.fileinput({
      language: 'zh', //设置语言
      uploadUrl: uploadUrl, //上传的地址
      allowedFileExtensions: ['jpg', 'gif', 'png'],//接收的文件后缀
      showUpload: true, //是否显示上传按钮
      showCaption: false,//是否显示标题
      browseClass: "btn btn-primary", //按钮样式     
      //dropZoneEnabled: false,//是否显示拖拽区域
      //minImageWidth: 50, //图片的最小宽度
      //minImageHeight: 50,//图片的最小高度
      //maxImageWidth: 1000,//图片的最大宽度
      //maxImageHeight: 1000,//图片的最大高度
      //maxFileSize: 0,//单位为kb，如果为0表示不限制文件大小
      //minFileCount: 0,
      maxFileCount: 10, //表示允许同时上传的最大文件个数
      enctype: 'multipart/form-data',
      validateInitialCount: true,
      // previewFileIcon: "<i class='glyphicon glyphicon-king'></i>",
      msgFilesTooMany: "选择上传的文件数量({n}) 超过允许的最大数值{m}！",
      uploadExtraData: function () {
        return {
          _xsrf: document.getElementsByName('_xsrf')[0].value,
        }
      }
    });

    //导入文件上传完成之后的事件
    $("#txt_file").on("fileuploaded", function (event, data, previewId, index) {
      $("#myModal").modal("hide");
      var data = data.response.lstOrderImport;
      if (data == undefined) {
        toastr.error('文件格式类型不正确');
        return;
      }
      //1.初始化表格
      var oTable = new TableInit();
      oTable.Init(data);
      $("#div_startimport").show();
    });
  }
  return oFile;
};
// $('#file-fr').fileinput({
//   theme: 'fas',
//   language: 'fr',
//   uploadUrl: '#',
//   allowedFileExtensions: ['jpg', 'png', 'gif']
// });
// $('#file-es').fileinput({
//   theme: 'fas',
//   language: 'es',
//   uploadUrl: '#',
//   allowedFileExtensions: ['jpg', 'png', 'gif']
// });
// $("#file-0").fileinput({q
//   theme: 'fas',
//   uploadUrl: '/data/upload/'
// }).on('filepreupload', function (event, data, previewId, index) {
//   alert('The description entered is:\n\n' + ($('#description').val() || ' NULL'));
// });
// $("#file-1").fileinput({
//   theme: 'fas',
//   uploadUrl: '#', // you must set a valid URL here else you will get an error
//   allowedFileExtensions: ['jpg', 'png', 'gif'],
//   overwriteInitial: false,
//   maxFileSize: 1000,
//   maxFilesNum: 10,
//   //allowedFileTypes: ['image', 'video', 'flash'],
//   slugCallback: function (filename) {
//     return filename.replace('(', '_').replace(']', '_');
//   }
// });
// /*
// $(".file").on('fileselect', function(event, n, l) {
// alert('File Selected. Name: ' + l + ', Num: ' + n);
// });
// */
// $("#file-3").fileinput({
//   theme: 'fas',
//   showUpload: false,
//   showCaption: false,
//   browseClass: "btn btn-primary btn-lg",
//   fileType: "any",
//   previewFileIcon: "<i class='glyphicon glyphicon-king'></i>",
//   overwriteInitial: false,
//   initialPreviewAsData: true,
//   initialPreview: [
//     "http://lorempixel.com/1920/1080/transport/1",
//     "http://lorempixel.com/1920/1080/transport/2",
//     "http://lorempixel.com/1920/1080/transport/3"
//   ],
//   initialPreviewConfig: [
//     { caption: "transport-1.jpg", size: 329892, width: "120px", url: "{$url}", key: 1 },
//     { caption: "transport-2.jpg", size: 872378, width: "120px", url: "{$url}", key: 2 },
//     { caption: "transport-3.jpg", size: 632762, width: "120px", url: "{$url}", key: 3 }
//   ]
// });
// $("#file-4").fileinput({
//   theme: 'fas',
//   uploadExtraData: { kvId: '10' }
// });
// $(".btn-warning").on('click', function () {
//   var $el = $("#file-4");
//   if ($el.attr('disabled')) {
//     $el.fileinput('enable');
//   } else {
//     $el.fileinput('disable');
//   }
// });
// $(".btn-info").on('click', function () {
//   $("#file-4").fileinput('refresh', { previewClass: 'bg-info' });
// });
// /*
// $('#file-4').on('fileselectnone', function() {
// alert('Huh! You selected no files.');
// });
// $('#file-4').on('filebrowse', function() {
// alert('File browse clicked for #file-4');
// });
// */
// $(document).ready(function () {
//   $("#test-upload").fileinput({
//     'theme': 'fas',
//     'showPreview': false,
//     'allowedFileExtensions': ['jpg', 'png', 'gif'],
//     'elErrorContainer': '#errorBlock'
//   });
//   $("#kv-explorer").fileinput({
//     'theme': 'explorer-fas',
//     'uploadUrl': '#',
//     overwriteInitial: false,
//     initialPreviewAsData: true,
//     initialPreview: [
//       "http://lorempixel.com/1920/1080/nature/1",
//       "http://lorempixel.com/1920/1080/nature/2",
//       "http://lorempixel.com/1920/1080/nature/3"
//     ],
//     initialPreviewConfig: [
//       { caption: "nature-1.jpg", size: 329892, width: "120px", url: "{$url}", key: 1 },
//       { caption: "nature-2.jpg", size: 872378, width: "120px", url: "{$url}", key: 2 },
//       { caption: "nature-3.jpg", size: 632762, width: "120px", url: "{$url}", key: 3 }
//     ]
//   });
//   /*
//    $("#test-upload").on('fileloaded', function(event, file, previewId, index) {
//    alert('i = ' + index + ', id = ' + previewId + ', file = ' + file.name);
//    });
//    */
// });
