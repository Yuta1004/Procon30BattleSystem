import java.util.Iterator;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;


public class PostRequest{
    private String url;
    private String content;
    private String encoding;
    private HttpResponse response;
    private StringEntity postData;
    private ArrayList<BasicNameValuePair> headerPairs;

    public PostRequest(String url){
        this(url, "ISO-8859-1");
    }

    public PostRequest(String url, String encoding){
        this.url = url;
        this.encoding = encoding;
        this.headerPairs = new ArrayList<BasicNameValuePair>();
    }

    public void addHeader(String key,String value) {
        BasicNameValuePair nvp = new BasicNameValuePair(key,value);
        headerPairs.add(nvp);
    }

    public void setData(String postData){
        try{
            StringEntity strEntity = new StringEntity(postData);
            strEntity.setContentType("application/json");
            this.postData = strEntity;
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public void send(){
        try {
            DefaultHttpClient httpClient = new DefaultHttpClient();
            HttpPost httpPost = new HttpPost(url);

            Iterator<BasicNameValuePair> headerIterator = headerPairs.iterator();
            while (headerIterator.hasNext()) {
                BasicNameValuePair headerPair = headerIterator.next();
                httpPost.addHeader(headerPair.getName(),headerPair.getValue());
            }
            httpPost.setEntity(this.postData);

            response = httpClient.execute(httpPost);
            HttpEntity entity = response.getEntity();
            this.content = EntityUtils.toString(response.getEntity());
            if(entity != null) EntityUtils.consume(entity);
            httpClient.getConnectionManager().shutdown();
            headerPairs.clear();
        } catch( Exception e ) {
            println("[Error] Network Error! (", e, ")");
        }
    }

    public String getContent(){
        return this.content;
    }
}