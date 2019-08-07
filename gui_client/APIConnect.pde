import http.requests.*;

GameState getGameState(String url){
    // Get data from API
    String apiURL = HOST + url;
    GetRequest get = new GetRequest(apiURL);
    get.send();
    
    // Parse (Basic info)
    JSONObject result = parseJSONObject(get.getContent());
    int boardWidth = result.getInt("width");
    int boardHeight = result.getInt("height");
    int startAtUnixTime = result.getInt("startedAtUnixTime");
    int turn = result.getInt("turn");
    
    // Parse (points, tiled)
    
}