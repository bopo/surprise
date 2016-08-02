function isMobile() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}
function install() {

    // 未认证用户不可下载应用
    if (downloadOnlyForCertification && !userIsCertification) {
        alert(unableDownload);
        return false;
    }

    if (aType == 'ios') {
        if (!isMobileRequest) {
            alert(askBrowserAlert);
            return;
        }
    }

    if (aType == 'ios' && browseType == 'android') {
        alert(forIosAlert);
        return;
    } else if (aType == 'android' && browseType == 'ios') {
//        alert(forAndroidAlert);
//        return;
    }

//    if ( isWechatRequest && aType == 'android') {
    if ( isWechatRequest) {
        alert(reminderWechatContent);
        return;
    }

    if (isQQRequest && aType == 'android') {
        alert(reminderQQContent);
        return ;
    }

    if (isUCRequest) {
        alert(reminderUCContent);
        return ;
    }

    url = "/app/install/" + aKey;
    window.location.href = url;
}

function install_loading() {

    // 未认证用户不可下载应用
    if (downloadOnlyForCertification && !userIsCertification) {
        alert(unableDownload);
        return;
    }

    if (aType == 'ios') {
        if (!isMobileRequest) {
            alert(askBrowserAlert);
            return;
        }
    }

    if (aType == 'ios' && browseType == 'android') {
        alert(forIosAlert);
        return;
    } else if (aType == 'android' && browseType == 'ios') {
//        alert(forAndroidAlert);
//        return;
    }

//    if ( isWechatRequest && aType == 'android') {
    if ( isWechatRequest) {
        alert(reminderWechatContent);
        return;
    }

    if ( isWeiboRequest) {
        alert(reminderWeiboContent);
        return;
    }

    if (isQQRequest && aType == 'android') {
        alert(reminderQQContent);
        return ;
    }

    if (isUCRequest) {
        alert(reminderUCContent);
        return ;
    }

    if(aType == 'ios'){
        $("#down_load").hide();
        $(".loading").css("display","inline-block");
        setTimeout('check()',5000);
    }

    url = "/app/install/" + aKey;
    window.location.href = url;
}
 function check() {
    $(".loading").hide();
    $("#showtext").show();
 }

function saveData() {
    $.ajax({
        type : "POST",
        data : $('#form').serialize(),
        dataType: 'json',
        beforeSend: function( xhr ) {
            if (isMobileRequest) {
                $('#submitButton').text( submiting ).attr('disabled', 'disabled');
            } else {
                $('#submitButton').text( submiting ).addClass('btn-u-default').attr('disabled', 'disabled');
            }
        },
        success : function(result, textStatus, jqXHR) {
                      
            code = result.code;
            href = result.extra.href;
            if (code == 0) {
//                window.location.reload();
                window.location.href = href;
            } else {
                alert(result.message);
                $('#submitButton').text( submitText ).removeClass('btn-u-default').removeAttr('disabled');
            }
        },
        error : function(jqXHR, textStatus, errorThrown) {
            $('#submitButton').text( submitText ).removeClass('btn-u-default').removeAttr('disabled');
        }
    });
}
    
function initView() {
    $('.history_row').click(function() {
       appkey = $(this).attr('appkey');
       window.location.href = '/' + appkey;
    });

    $('.history_show_more').click(function() {
       $('.history_row').show();
       $(this).hide();
    });
}

function reditectAppStore() {
    if ( isWechatRequest) {
        alert(reminderWechatDownloadContent);
        return;
    }

    if ( isWeiboRequest) {
        alert(reminderWeiboDownloadContent);
        return;
    }

    if (isQQRequest && aType == 'android') {
        alert(reminderQQDownloadContent);
        return ;
    }

    if (isUCRequest) {
        alert(reminderUCDownloadContent);
        return ;
    }

    url = appStoreUrl;
    window.location.href = url;
}

