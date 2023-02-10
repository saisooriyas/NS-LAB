import java.security.*;
import java.util.Base64;
public class DSS
{
    public static void main(String[] arg)throws Exception
    {
        KeyPairGenerator keygen=KeyPairGenerator.getInstance("DSA");
        SecureRandom random=SecureRandom.getInstanceStrong();
        keygen.initialize(2048,random);
        KeyPair pair=keygen.generateKeyPair();
        PrivateKey pr=pair.getPrivate();
        PublicKey pu=pair.getPublic();
        
        Signature s=Signature.getInstance("SHA256withDSA");
        s.initSign(pr);
        byte[] msg="Hello World".getBytes("UTF-8");
        s.update(msg);
        byte[] signature=s.sign();
        String encodedsignature=Base64.getEncoder().encodeToString(signature);
        System.out.print("Encoded Signature:"+encodedsignature);
        
        Signature v=Signature.getInstance("SHA256withDSA");
        v.initVerify(pu);
        v.update(msg);
        boolean result=v.verify(Base64.getDecoder().decode(encodedsignature));
        System.out.print("Signature Verification: "+result);
    }
}