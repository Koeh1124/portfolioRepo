import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;

public class Encryption {
    // key generation
    public static SecretKey getKey(String seed) throws NoSuchAlgorithmException {
        KeyGenerator kg = KeyGenerator.getInstance("DES");
        SecureRandom secRand = new SecureRandom();
        secRand.setSeed(seed.getBytes());
        kg.init(secRand);
        SecretKey key = kg.generateKey();
        return key;
    }

    // return encrypted string
    public static String encryptString(SecretKey key, String string) {
        Cipher cipher;
        try {
            cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, key);
            byte[] encText;
            encText = cipher.doFinal(string.getBytes());
            return new String(encText);
        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException | IllegalBlockSizeException
                | BadPaddingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return "not good";
    }

    // decrypt string
    public static String decrypString(SecretKey key, String encString) {
        Cipher cipher;
        try {
            cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key);
            byte[] text;
            text = cipher.doFinal(encString.getBytes());
            return new String(text);
        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException | IllegalBlockSizeException
                | BadPaddingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return "not good";
    }
}
