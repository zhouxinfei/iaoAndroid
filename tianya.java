package com.jeb;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;

// 天涯社区app 版本号 7.0.1
public class tianya {

    public static void main(String[] args) {
        String arg3 = "tianyaiphone and android";
        String arg4 = "123456";
        String dPassword = encrypt(arg3, arg4);
        System.out.println("dPassword : " + dPassword);
        // dPassword : DEF410FD8D3D687C
    }

    public static String encrypt(String arg3, String arg4) {
        String v1 = null;
        if(arg4 != null && arg3 != null) {
            byte[] v0 = a1(arg3, arg4.getBytes());
            if(v0 != null) {
                v1 = a3(v0);
            }
        }

        return v1;
    }
    public static byte[] a1(String arg2, byte[] arg3) {
        return a2(arg2.getBytes(), arg3);
    }

    public static byte[] a2(byte[] arg6, byte[] arg7) {
        try {
            SecretKeySpec v1 = new SecretKeySpec(arg6, "DESede");
            Cipher v0 = Cipher.getInstance("DESede");
            v0.init(1, ((Key)v1));
            byte[] v5 = v0.doFinal(arg7);
            return v5;
        }
        catch(Exception v4) {
            v4.printStackTrace();
        }
        return null;
    }
    public static String a3(byte[] arg5) {
        String v0 = "";
        int v1;
        for(v1 = 0; v1 < arg5.length; ++v1) {
            String v2 = Integer.toHexString(arg5[v1] & 255);
            v0 = v2.length() == 1 ? v0 + "0" + v2 : v0 + v2;
        }

        return v0.toUpperCase();
    }
}
