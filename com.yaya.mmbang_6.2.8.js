// 妈妈帮 官方版本号：v6.2.8

function showStacks(){
    var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    // var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
    console.log(stack);
}


function hook_java(){
    Java.perform(function(){
        console.log('Hook Start ！');

        
        var cgz = Java.use('cgz');

        cgz.b.overload('java.lang.String').implementation = function(args1){
            showStacks();
            console.log("cgz args1 : ", args1)
            var sign = this.b(args1);
            console.log("cgz sign : ", sign)
            return sign;
        };

    
    })
}

setImmediate(hook_java);


