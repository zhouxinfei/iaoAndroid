function showStacks(){
    var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    // var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
    console.log(stack);
}

function call_java(){
    Java.perform(function(){
        console.log('Hook CALL Start ！');


        var WTSign = Java.use("com.meituan.android.common.mtguard.wtscore.plugin.sign.core.WTSign");
        var WTSign_MODE = Java.use("com.meituan.android.common.mtguard.wtscore.plugin.sign.core.WTSign$MODE");
        var StrCls = Java.use('java.lang.String');
        var arg1 = "POST /mtapi/v11/search/globalpage __reqTraceID=ad9444aa-4dcc-4415-a982-60fefdce45d6&activity_filter_codes=&app=0&category_type=0&ci=10&entrance_id=0&f=android&gaoda_id=0&is_fix_keyword=false&keyword=%E9%BA%BB%E8%BE%A3%E9%A6%99%E9%94%85&msid=8672411529331251623401709047&page_index=0&page_size=10&partner=4&platform=4&poilist_mt_cityid=10&poilist_wm_cityid=310100&product_card_page_index=0&product_tag_id=&push_token=dpsh1beb7f7e5a2b7af1dbde1f548b383083atpu&query_type=12002&req_time=1623403392363&search_cursor=0&search_global_id=4033931851035836032&search_latitude=0&search_longitude=0&search_page_type=0&search_source=0&slider_select_data=&sort_type=0&sub_category_type=0&userid=-1&utm_campaign=AgroupBgroupC0E0&utm_content=867241152933125&utm_medium=android&utm_source=xiaomi&utm_term=1100070402&uuid=0000000000000BE50E6959E834263AD97AAA5FE2AAF45A162336497793950199&version=11.7.402&version_name=11.7.402&waimai_sign=lHm%2FnRIn%2FtydJ62Cxi0ZAbNCs9BHZPQxj8Fix1lSLeU3l%2Fe7G8xCaSJ26CQVqr62txlip6AD2RP1%0APYBPLxbWUXtiykBcQwI7RS0XZEiu1PaCkKAJ6NIMMu%2BiiUqzcwVLboXEZtofjDzB7C99H%2BBFE9je%0A8Zp9Wn8UXwxc6rrqWRc%3D%0A&weien_id=0&wm_actual_latitude=31222418&wm_actual_longitude=121481166&wm_appversion=11.7.402&wm_ctype=mtandroid&wm_did=867241152933125&wm_dtype=VOG-AL00&wm_dversion=25_7.1.2&wm_latitude=31222418&wm_longitude=121481166&wm_mac=98%3A33%3Abd%3A2b%3Abd%3Acb&wm_seq=140&wm_uuid=0000000000000BE50E6959E834263AD97AAA5FE2AAF45A162336497793950199&wm_visitid=0a1d808c-6742-4d17-991a-fbc332280c9e&word_source="
        var OutStr = StrCls.$new(arg1);
        var arg1Bytes = OutStr.getBytes("UTF-8");
        var mtgsig = WTSign.makeHeader(arg1Bytes, WTSign_MODE.FAST.value);
        console.log("mtgsig result : ", mtgsig);

        console.log('Hook CALL End ！');
    })
}

function mian(){
    call_java();
}

setImmediate(mian);


