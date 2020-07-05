$(function () {
        h = screen.height
        $(".tcbg,.shx").css("height", h - 150)
        $(".fwql li").click(function () {
            var num = $(".fwql li").index($(this))
            $(this).addClass("now")
            $(this).siblings("li").removeClass("now")
            $(".fwqrm").eq(num).show()
            $(".fwqrm").eq(num).siblings(".fwqrm").hide()
            if ($(this).data('type') == 1)
            {
                $('input[name=fwq]').val('混服');
                $('.fwq2').html('混服');
                get()
                //2.23增加 解决点击混服后页面无法拖动的问题
                $('.flt').removeClass("now")
                $("body").css("position","relative")
            }
        })
        $(".flt").bind("mousedown touchstart", function (event) {
            event.stopPropagation();
            event.preventDefault();
            var num2 = $(".flt").index($(this))
            $(this).toggleClass("now")
            $(this).siblings(".flt").removeClass("now")
            //flb为弹出窗的class，以下代码弹出对应当前flt的窗口（通过num2获取li所在的位置）。
            $(".flb").eq(num2).toggle()
            $(".flb").eq(num2).siblings(".flb").hide()
            if ($(".flt").hasClass("now")) {
                $(".tcbg").show()
             //当.flt有now类（即点开）时，将背景设置成固定定位禁止滑动
$("body").css("position","fixed")
//$("body").css("height",h - 150)
            } else {
                $(".tcbg").hide()
                //当所有flt都没有now类时（说明窗口已经被关闭），body归位。但是只有在flt被点击时才会生效，所以在后面服务器的点击事件中也需要加上。
$("body").css("position","relative")
            }


        })

        $('.top').click(function () {
            $('body,html').stop().animate({
                'scrollTop': 0,
                'duration': 100,
                'easing': 'ease-in'
            })
        });
    });
