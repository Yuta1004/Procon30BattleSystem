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
}

class Action{
    Action(){
    
    }
}

class Team{
    Team(){
    
    }
}

class Agent{
    Agent(){
    
    }
}