class GameState{
    public int boardWidth;
    public int boardHeight;
    public int startAtUnixTime;
    public int turn;
    public ArrayList<ArrayList<Integer>> points;
    public ArrayList<ArrayList<Integer>> tiled;
    public ArrayList<Action> actions;
    public ArrayList<Team> teams;

    GameState(int boardWidth, int boardHeight, int startAtUnixTime, int turn,
              ArrayList<ArrayList<Integer>> points,
              ArrayList<ArrayList<Integer>> tiled,
              ArrayList<Action> actions,
              ArrayList<Team> teams){
        this.boardWidth = boardWidth;
        this.boardHeight = boardHeight;
        this.startAtUnixTime = startAtUnixTime;
        this.turn = turn;
        this.points = points;
        this.tiled = tiled;
        this.actions = actions;
        this.teams = teams;
    }

    GameState(){
        this.boardWidth = -1;
        this.boardHeight = -1;
        this.startAtUnixTime = -1;
        this.turn = -1;
        this.points = new ArrayList<ArrayList<Integer>>();
        this.tiled = new ArrayList<ArrayList<Integer>>();
        this.actions = new ArrayList<Action>();
        this.teams = new ArrayList<Team>();
    }
}

class Action{
    public int agentID;
    public int dx;
    public int dy;
    public String type;
    public int apply;
    public int turn;

    Action(int agentID, int dx, int dy, String type, int apply, int turn){
        this.agentID = agentID;
        this.dx = dx;
        this.dy = dy;
        this.type = type;
        this.apply = apply;
        this.turn = turn;
    }
}

class Team{
    public ArrayList<Agent> agents;
    public int areaPoint;
    public int tilePoint;
    public int teamID;

    Team(ArrayList<Agent> agents, int areaPoint, int tilePoint, int teamID){
        this.agents = agents;
        this.areaPoint = areaPoint;
        this.tilePoint = tilePoint;
        this.teamID = teamID;
    }
}

class Agent{
    public int agentID;
    public int x;
    public int y;

    Agent(int agentID, int x, int y){
        this.agentID = agentID;
        this.x = x;
        this.y = y;
    }
}

class Battle{
    public int battleID;
    public int myTeamID;
    public int turns;
    public int turnMillis;
    public int intervalMillis;
    public String matchTo;

    Battle(int battleID, int myTeamID, int turns, int turnMillis, int intervalMillis, String matchTo){
        this.battleID = battleID;
        this.myTeamID = myTeamID;
        this.turns = turns;
        this.turnMillis = turnMillis;
        this.intervalMillis = intervalMillis;
        this.matchTo = matchTo;
    }
}