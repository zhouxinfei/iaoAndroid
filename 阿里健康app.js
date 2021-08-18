function yiluHook(data, api){
    var result;
    Java.perform(function(){
        console.log('Hook Start ！');

        var XState = Java.use('mtopsdk.xstate.XState');
        var umtResutl = XState.getValue('INNER', 'umt');
        // console.log("umtResutl结果 : ", umtResutl)

        var deviceId;
        var utdid;
        Java.choose("mtopsdk.mtop.intf.Mtop",{
            onMatch: function(obj){
                var DeviceId = obj.getDeviceId();
                deviceId = DeviceId;
                // console.log('DeviceId : ', DeviceId);
                
                var Utdid = obj.getUtdid();
                utdid = Utdid;
                // console.log('Utdid : ', Utdid);

            },
            onComplete: function(){
    
            }
        });

        var timeStamp = new Date().getTime();
        timeStamp = timeStamp + ''

        var t = timeStamp.substring(0,10);

        var LinkedHashMap = Java.use('java.util.LinkedHashMap');
        // console.log("data", data)
        var map = LinkedHashMap.$new();
        map.put("data", data);
        map.put("utdid", utdid);
        map.put("ttid", "alijk");
        map.put("deviceId", deviceId);
        map.put("sid", null);
        map.put("uid", null);
        map.put("x-features", "27");
        map.put("t", t);
        map.put("v", "4.0");
        map.put("appKey", "23211311");
        map.put("api", api);

        var appKey = "23211311";
        var signResult;
        Java.choose("mtopsdk.security.InnerSignImpl",{
            onMatch: function(obj){

                var sign = obj.getSign(map, appKey);
                signResult= sign;
                // console.log('sign : ', sign);
            },
            onComplete: function(){

            }
        });
        // console.log('signResult : ', signResult);

        var map1 = map;
        // map1.put("sign", "ab2231001054ac7f53e8ed35cfdbd6a4285397644eacf6c66d");
        map1.put("sign", signResult);
        // console.log('map1 : ', map1);
    
        var map2 = LinkedHashMap.$new()
        map2.put("pageId", "");
        map2.put("pageName", "");
        // console.log('map2 : ', map2);
    
        var MiniWuaResult ='';
        Java.choose("mtopsdk.security.InnerSignImpl",{
            onMatch: function(obj){
                var MiniWua = obj.getMiniWua(map1, map2);
                MiniWuaResult= MiniWua;
                // console.log('MiniWua : ', MiniWua);
            },
            onComplete: function(){
    
            }
        });
        // console.log('MiniWuaResult : ', MiniWuaResult);

        var randomNum= 1000000 + Math.round(Math.random()*100000) + '';
        // console.log(randomNum);
        var traceid = utdid + timeStamp + '00' + randomNum
        result = '{"x-umt": "'+umtResutl+'","x-devid": "'+deviceId+'","x-utdid": "'+utdid+'","x-sign": "'+signResult
        +'","x-mini-wua": "'+MiniWuaResult+'","x-c-traceid": "'+traceid+'","x-t": "'+t+'"}';
        // console.log(result);
        console.log('Success！');

    });
    return result;
}
// rpc.exports = {
//     qiaodongfang: yiluHook
// };
var data = '{"doctorId":"351343","hospitalId":"null","channelCode":"null"}';
var api = 'mtop.alihealth.alidoc.doctor.getdetail';
var result = yiluHook(data, api);
console.log(result);
