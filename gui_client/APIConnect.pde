void sendActionData(int battleID, int agentID, int dx, int dy, String type){
    // Make actions JSON
    String actionData = "{\"actions\" : [{ \"agentID\": AGENTID, \"dx\": DX, \"dy\": DY, \"type\": TYPE }]}";
    actionData = actionData.replace("AGENTID", str(agentID));
    actionData = actionData.replace("DX", str(dx));
    actionData = actionData.replace("DY", str(dy));
    actionData = actionData.replace("TYPE", type);

    // Post send
    String apiURL = HOST + "/matches/" + str(battleID) + "/action";
    PostRequest post = new PostRequest(apiURL);
    post.addHeader("Authorization", TOKEN);
    post.addHeader("Content-Type", "application/json");
    post.setData(actionData);
    post.send();

    // Error Handling
    try{
        parseJSONObject(post.getContent());
    }catch(Exception e){
        displayErrorDialog("Cannot send action data.<br>Please check connection.");
        return;
    }
}

void getBattleList(){
    // Get data from API
    String apiURL = HOST + "/matches";
    GetRequest get = new GetRequest(apiURL);
    get.addHeader("Authorization", TOKEN);
    get.send();

    // Error Handling
    JSONArray battleJSONArray = new JSONArray();
    try{
        battleJSONArray = parseJSONArray(get.getContent());
    }catch (Exception e){
        displayErrorDialog("Cannot get battle data from api.<br>Please check token or connection.");
        battleList = new HashMap<Integer, Battle>();
        return;
    }

    // Parse
    for(int idx = 0; idx < battleJSONArray.size(); ++ idx){
        JSONObject battle = battleJSONArray.getJSONObject(idx);
        battleList.put(battle.getInt("id"),
            new Battle(
                battle.getInt("id"),
                battle.getInt("teamID"),
                battle.getInt("turns"),
                battle.getInt("turnMillis"),
                battle.getInt("intervalMillis"),
                battle.getString("matchTo")
            )
        );
    }
}

GameState getGameState(int battleID){
    // Get data from API
    String apiURL = HOST + "/matches/" + str(battleID);
    GetRequest get = new GetRequest(apiURL);
    get.addHeader("Authorization", TOKEN);
    get.send();

    // Parse (Basic info)
    JSONObject result = new JSONObject();
    try{
        result = parseJSONObject(get.getContent());
    }catch (Exception e){
        displayErrorDialog("Cannot get game data from API.<br>Please check connection.");
        return new GameState();
    }
    int boardWidth = result.getInt("width");
    int boardHeight = result.getInt("height");
    int startAtUnixTime = result.getInt("startedAtUnixTime");
    int turn = result.getInt("turn");

    // Parse (points, tiled)
    ArrayList<ArrayList<Integer>> tiled =
        convertJSONArray2d(result.getJSONArray("tiled"));
    ArrayList<ArrayList<Integer>> points =
        convertJSONArray2d(result.getJSONArray("points"));

    // Parse (actions)
    JSONArray actions = result.getJSONArray("actions");
    ArrayList<Action> actionsArray = new ArrayList<Action>();
    for(int idx = 0; idx < actions.size(); ++ idx){
        // action
        JSONObject action = actions.getJSONObject(idx);

        // More info
        int agentID = action.getInt("agentID");
        int dx = action.getInt("dx");
        int dy = action.getInt("dy");
        String type = action.getString("type");
        int apply = action.getInt("apply");
        int turnAction = action.getInt("turn");

        // add
        actionsArray.add(
            new Action(agentID, dx, dy, type, apply, turnAction)
        );
    }

    // Parse (teams)
    ArrayList<Team> teamsArray = new ArrayList<Team>();
    JSONArray teams = result.getJSONArray("teams");
    for(int idx = 0; idx < teams.size(); ++ idx){
        // team
        JSONObject team = teams.getJSONObject(idx);

        // Agents
        ArrayList<Agent> agentsArray = new ArrayList<Agent>();
        JSONArray agents = team.getJSONArray("agents");
        for(int agentIdx = 0; agentIdx < agents.size(); ++ agentIdx){
            JSONObject agent = agents.getJSONObject(agentIdx);
            int agentID = agent.getInt("agentID");
            int x = agent.getInt("x");
            int y = agent.getInt("y");
            agentsArray.add(
                new Agent(agentID, x, y)
            );
        }

        // More info
        int tilePoint = team.getInt("tilePoint");
        int areaPoint = team.getInt("areaPoint");
        int teamID = team.getInt("teamID");

        // add
        teamsArray.add(
            new Team(agentsArray, areaPoint, tilePoint, teamID)
        );
    }

    return new GameState(
        boardWidth, boardHeight, startAtUnixTime, turn,
        points, tiled, actionsArray, teamsArray
    );
}