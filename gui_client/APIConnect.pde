GameState getGameState(int battleID){
    // Get data from API
    String apiURL = HOST + "/matches/" + str(battleID);
    GetRequest get = new GetRequest(apiURL);
    get.addHeader("Authorization", TOKEN);
    get.send();

    // Parse (Basic info)
    JSONObject result = parseJSONObject(get.getContent());
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