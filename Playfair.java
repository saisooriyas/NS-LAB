public class PlayFari_Cipher
{
    public static void enc(char[][] mat,char[] key)
    {
        int s=0,e=1,i,i1,j,j1,row1=0,col1=0,row2=0,col2=0,k,f=1;
        char t=' ';
        while(e<key.length)
        {
            for(i=0;i<5;i++)
            {
                for(j=0;j<5;j++)
                {
                    if(mat[i][j]==key[s])
                    {
                    row1=i;
                    col1=j;
                    }
                    for(i1=0;i1<5;i1++)
                    {
                        for(j1=0;j1<5;j1++)
                        {
                            if(mat[i1][j1]==key[e])
                            {
                                row2=i1;
                                col2=j1;
                            }
                            if(row1>row2)
                            {
                                for(k=row2;k<5;k++)
                                {
                                if(k==row1)
                                t=mat[k][col2];
                                }
                            }
                            else if(row1==row2)
                            {
                                if(col1+1>4)
                                t=mat[row1][(col1+1)-5];
                                else 
                                t=mat[row1][col1+1];
                            }
                            else if(col1==col2)
                            {
                            if(row1+1>4)
                            t=mat[(row1+1)-5][col1];
                            else
                                t=mat[row1+1][col1];
                            }
                            else
                            {
                                for(k=row2;k>=0;k--)
                                {
                                    if(k==row1)
                                    t=mat[k][col2];
                                }
                            }
                            
                        }
                    }
                }
            }
            System.out.print(t+" ");
            if(f%2!=0)
            {
                int yt=s;
                s=e;
                e=yt;
                f++;
                
            }
            else 
            {
                s++;
                e+=3;
                f++;
            }
        
        }
    }
	public static void main(String[] args) {
	    char a[][]={{'m','o','n','a','r'},{'c','h','y','b','d'},{'e','f','g','i','k'},{'l','p','q','s','t'},{'u','v','w','x','z'}};
		char b[]={'i','n','s','t','r','u','m','e','n','t'};
		enc(a,b);
	}
}
