function showStacks(){
    var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    // var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
    console.log(stack);
}


function call_java() { 
    Java.perform(function () {

        console.log('Hook Start ...');

        var deviceId;
        var utdid;
        Java.choose("mtopsdk.mtop.intf.Mtop",{
            onMatch: function(obj){
                var deviceId_ = obj.getDeviceId();
                deviceId = deviceId_;
                // console.log("deviceId : ", deviceId);
                var utdid_ = obj.getUtdid();
                utdid = utdid_;
                // console.log("utdid : ", utdid);
            },
            onComplete: function(){}
        });

        var DeviceUUID = Java.use("me.ele.foundation.DeviceUUID");
        var deviceUUID = DeviceUUID.getDeviceUUID("me.ele_device_id", "me.ele_device_id");
        // console.log("DeviceUUID.getDeviceUUID deviceUUID : ", deviceUUID);

        var jsonObject = Java.use('org.json.JSONObject');
        var string = Java.use("java.lang.String");

        var LinkedHashMap = Java.use('java.util.LinkedHashMap');

        var linkedHashMap = LinkedHashMap.$new();
        linkedHashMap.put("_mus_tpl", "https://g.alicdn.com/eleme-retail-shop/muise-shop/10.0.11/enr-muise-shop.mus.wlm");
        linkedHashMap.put("bizChannel", "android.default.default");
        // linkedHashMap.put("deviceId", "4a662da3-30f9-322b-a7b4-eac56d6f2fc1");
        linkedHashMap.put("deviceId", deviceUUID);
        linkedHashMap.put("ele_id", "E4590578173517708527");
        linkedHashMap.put("from", "native");
        linkedHashMap.put("lat", null);
        linkedHashMap.put("livingShowChannel", "eleme");
        linkedHashMap.put("lng", null);
        linkedHashMap.put("store_id", "545928469");

        var linkedHashMap_res = jsonObject.$new(linkedHashMap);
        var linkedHashMap_res_str = string.valueOf(linkedHashMap_res);

        // console.log("linkedHashMap_res_str : ", linkedHashMap_res_str);

        var linkedHashMap_1 = LinkedHashMap.$new();
        // linkedHashMap_1.put("deviceId", "AiZZFChkvgNP1h5Rc36XPPfba6G2LKodAsDv4caGT8dv");
        linkedHashMap_1.put("deviceId", deviceId);
        linkedHashMap_1.put("appKey", "24895413");
        // linkedHashMap_1.put("utdid", "YQeod3v1o20DAPjiF/yfp3kc");
        linkedHashMap_1.put("utdid", utdid);
        linkedHashMap_1.put("x-features", "27");
        linkedHashMap_1.put("ttid", "1608030065155@eleme_android_10.0.11");
        linkedHashMap_1.put("v", "1.3");
        linkedHashMap_1.put("sid", null);
        linkedHashMap_1.put("t", "1627898297");
        linkedHashMap_1.put("api", "mtop.venus.shopresourceservice.getshopresource");
        linkedHashMap_1.put("data", linkedHashMap_res_str);
        linkedHashMap_1.put("lng", null);
        linkedHashMap_1.put("uid", null);
        linkedHashMap_1.put("lat", null);

        var linkedHashMap_2 = LinkedHashMap.$new();
        linkedHashMap_2.put("pageName", "");
        linkedHashMap_2.put("pageId", "");

        var str = "24895413";
        var str2 = null;
        var z = false;

        // InnerSignImpl.getUnifiedSign hashMap1 :  {deviceId=AiZZFChkvgNP1h5Rc36XPPfba6G2LKodAsDv4caGT8dv, appKey=24895413, utdid=YQeod3v1o20DAPjiF/yfp3kc, x-features=27, ttid=1608030065155@eleme_android_10.0.11, v=1.3, sid=null, t=1627898297, api=mtop.venus.shopresourceservice.getshopresource, data={"_mus_tpl":"https://g.alicdn.com/eleme-retail-shop/muise-shop/10.0.11/enr-muise-shop.mus.wlm","bizChannel":"android.default.default","deviceId":"4a662da3-30f9-322b-a7b4-eac56d6f2fc1","ele_id":"E4590578173517708527","from":"native","lat":31.17115192115307,"livingShowChannel":"eleme","lng":121.40756785869598,"store_id":"545928469"}, lng=121.40756785869598, uid=null, lat=31.17115192115307}
        // InnerSignImpl.getUnifiedSign hashMap2 :  {pageName=, pageId=}
        // InnerSignImpl.getUnifiedSign str :  24895413
        // InnerSignImpl.getUnifiedSign str2 :  null
        // InnerSignImpl.getUnifiedSign z :  false
        // InnerSignImpl.getUnifiedSign result :  {"x-sign":"aznAEN002xAAKWgEQ7MeUZbDbu8rSWgJYoPof3kyh5jFOJy+h+3boIhAq17YW0pzgTgGuHU\/u0frs1xNy0gktcFFyZl4KWgJaCloCW","x-mini-wua":"HHnB_6ZjbyI0jZd1buvgFyK08pQKZgz5g2qm6TOVPTt5iTUJTxEuZDaOElaFNdx2dzgGbmadhpN7u8XH32rD3ABlV3L5\/aTxhHwypQ09Bkvz0JqySu4ucoE6+e9iduDSyc54sLzhTrRZUQhnedpRTC28s+Pf4gvAnSKMD8CuemjIISKU=","x-sgext":"JAEhfprt11NuQylSelonjH4QThFKE10QTxJPEF0UTA==","x-umt":"0x9Lfv5LOp4EnDV7BSInrpMW6xHTbTTo"}

        var miniwua;
        Java.choose("mtopsdk.security.InnerSignImpl",{
            onMatch: function(obj){
                var result = obj.getUnifiedSign(linkedHashMap_1, linkedHashMap_2, str, str2, z);
                var res = jsonObject.$new(result);
                var res_str = string.valueOf(res);
                miniwua = res_str
                // console.log("InnerSignImpl.getUnifiedSign result : ", res_str);
            },
            onComplete: function(){}
        });
        console.log("miniwua : ", miniwua);
        console.log('Hook End !!!');

    });

}

function mian(){
    call_java();
}

setImmediate(mian);




