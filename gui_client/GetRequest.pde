import java.util.Iterator;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;


public class GetRequest{
    String url;
    String content;
    HttpResponse response;
    ArrayList<BasicNameValuePair> headerPairs;

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

            if( entity != null ) EntityUtils.consume(entity);
            httpClient.getConnectionManager().shutdown();
        } catch( Exception e ) {
            e.printStackTrace();
        }
    }

    public String getContent(){
        return this.content;
    }
}