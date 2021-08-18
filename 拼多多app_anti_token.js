// com.xunmeng.pinduoduo_5.44.1.apk

function call_java(){
    Java.perform(function(){
        console.log('Hook CALL Start ！');

        var currentApplication = Java.use('android.app.ActivityThread').currentApplication();
        var context = currentApplication.getApplicationContext();

        // anti_token 
        var DeviceNative = Java.use('com.xunmeng.pinduoduo.secure.DeviceNative');
        var timestamp = new Date().getTime();
        var anti_token = DeviceNative.info2(context, timestamp);
        console.log("anti_token result : ", anti_token);


        console.log('Hook CALL End ！');
    })
}

function main(){
    call_java();
}

setImmediate(main);

