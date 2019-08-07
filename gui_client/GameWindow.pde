class GameWindow implements Window{
    private gui_client parent;
    private GameState gameState;
    private int bWidth;
    private int bHeight;
    private int tileSize;
    private int xBias;
    private int yBias;
    private HashMap<Integer, Integer> teamColors;

    GameWindow(gui_client parent, int battleID){
        this.parent = parent;
        this.gameState = getGameState(battleID);

        this.bWidth = gameState.boardWidth;
        this.bHeight = gameState.boardHeight;
        this.tileSize = min(80, int(800 / max(bWidth, bHeight)));
        this.xBias = (800 - tileSize * bWidth) / 2;
        this.yBias = (800 - tileSize * bHeight) / 2;
        this.teamColors = new HashMap<Integer, Integer>();

        teamColors.put(0, color(255));
        teamColors.put(gameState.teams.get(0).teamID, color(255, 200, 200));
        teamColors.put(gameState.teams.get(1).teamID, color(200, 200, 255));
    }

    void start(){
        // do nothing
    }

    void finish(){
        // do nothing
    }

    void draw(){
        background(255);

        // Board
        for(int y = 0; y < this.bHeight; ++ y){
            for(int x = 0; x < this.bWidth; ++ x){
                int dX = x * this.tileSize + this.xBias;
                int dY = y * this.tileSize + this.yBias;

                // tile
                fill(teamColors.get(gameState.tiled.get(y).get(x)));
                rect(dX, dY, this.tileSize, this.tileSize);

                // score
                fill(0);
                textAlign(CENTER);
                textSize(this.tileSize / 3);
                text(this.gameState.points.get(y).get(x),
                     dX + this.tileSize / 2, dY + this.tileSize / 1.5);
            }
        }
    }
}