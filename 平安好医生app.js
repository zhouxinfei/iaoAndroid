function call_java(){
    Java.perform(function () {


        var MobileApiConfig = Java.use('com.pajk.bricksandroid.basicsupport.Config.MobileApiConfig');
        var getDeviceToken = MobileApiConfig.GetInstant().getDeviceToken();
        console.log("getDeviceToken : ", getDeviceToken);

        var Long = Java.use("java.lang.Long");
        var TTSignature = Java.use('com.pajk.bricksandroid.basicsupport.MobileApi.TotpAPI.TTSignature');
        var MobileApiConfig = Java.use('com.pajk.bricksandroid.basicsupport.Config.MobileApiConfig');
        var sortMap = '_aid=1_chl=YYB_ct=1614592946500_dtk=Ly/4WjYKFOqZuYtY739Svv+BUMR5dpvDTVQxpPpkcWhCMO4HCMOiccEOKalfpuhs_ft=json_mt=skydive.compositeSearchV5_og=nt_rv=zk_a_n16695_7.25.0_pd_20_sm=tp_tk=BK0IYn6P5CTBc5y769JBeXAJUy8PQ3bKRIg878G2HVdXdqh4cZgSNuoAYQUm1+c9Yfmrg/R0qogB+7cKrNh3zAHP+qZKjOlQ0kIGgIi572Q=_uid=151580900307_vc=72500inquiryRequestParam={"keyword":"水痘","maxAge":-1,"minAge":-1,"monthAge":-1,"pageNo":0,"pageSize":10,"showAd":true,"showAgg":true,"symptoms":[]}isFilter=1keyword=水痘mapType=BAIDUrefreshTab=falseserverVersion=V5sourcePosition=20001tabCode=17000';
        var bArr = MobileApiConfig.GetInstant().GetDSeedKey();
        var _sig = TTSignature.a(sortMap, bArr, Long.valueOf("1614592946500").longValue());
        console.log("_sig : ", _sig);
        
    });
}
