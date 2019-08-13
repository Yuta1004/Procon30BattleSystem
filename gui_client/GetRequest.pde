import java.util.Iterator;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;


public class GetRequest{
    private String url;
    private String content;
    private int statusCode;
    private HttpResponse response;
    private ArrayList<BasicNameValuePair> headerPairs;

    public GetRequest(String url){
        this.url = url;
        headerPairs = new ArrayList<BasicNameValuePair>();
    }

    public void addHeader(String key,String value) {
        BasicNameValuePair nvp = new BasicNameValuePair(key,value);
        headerPairs.add(nvp);
    }

    public void send(){
        try {
            DefaultHttpClient httpClient = new DefaultHttpClient();
            HttpGet httpGet = new HttpGet(url);

            Iterator<BasicNameValuePair> headerIterator = headerPairs.iterator();
            while (headerIterator.hasNext()) {
                BasicNameValuePair headerPair = headerIterator.next();
                httpGet.addHeader(headerPair.getName(),headerPair.getValue());
            }

            response = httpClient.execute( httpGet );
            HttpEntity entity = response.getEntity();
            this.content = EntityUtils.toString(response.getEntity());
            this.statusCode = response.getStatusLine().getStatusCode();

            if( entity != null ) EntityUtils.consume(entity);
            httpClient.getConnectionManager().shutdown();
        } catch( Exception e ) {
            println("[Error] Network Error!! (", e, ")");
        }
    }

    public int getStatusCode(){
        return this.statusCode;
    }

    public String getContent(){
        return this.content;
    }
}