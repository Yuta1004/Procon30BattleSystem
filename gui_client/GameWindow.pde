class GameWindow implements Window{
    private gui_client parent;
    private GameState gameState;
    private int battleID, bWidth, bHeight, tileSize, xBias, yBias;
    private HashMap<Integer, Integer> teamColors;
    private HashMap<Integer, AgentController> agentControllers;
    private GButton gameUpdate;
    private boolean ifShiftPressing;

    GameWindow(gui_client parent, int battleID){
        this.parent = parent;
        this.battleID = battleID;
        this.gameState = getGameState(battleID);

        this.bWidth = gameState.boardWidth;
        this.bHeight = gameState.boardHeight;
        this.tileSize = min(80, int(800 / max(bWidth, bHeight)));
        this.xBias = (800 - tileSize * bWidth) / 2;
        this.yBias = (800 - tileSize * bHeight) / 2;
        this.teamColors = new HashMap<Integer, Integer>();
        this.ifShiftPressing = false;

        teamColors.put(0, color(255));
        teamColors.put(gameState.teams.get(0).teamID, color(255, 200, 200));
        teamColors.put(gameState.teams.get(1).teamID, color(200, 200, 255));

        this.gameUpdate = new GButton(
            this.parent, 950, 500, 100, 50, "UPDATE"
        );
        this.gameUpdate.tag = "GameUpdate";

        initAgentControllers();
    }

    void start(){
        for(AgentController controller: this.agentControllers.values()){
            controller.start();
        }
        this.gameUpdate.setVisible(true);

    }

    void finish(){
        for(AgentController controller: this.agentControllers.values()){
            controller.finish();
        }
        this.gameUpdate.setVisible(false);
        this.ifShiftPressing = false;
    }

    void initAgentControllers(){
        this.agentControllers = new HashMap<Integer, AgentController>();
        for(int idxT = 0; idxT < this.gameState.teams.size(); ++ idxT){
            Team team = this.gameState.teams.get(idxT);
            for(int idxA = 0; idxA < team.agents.size(); ++ idxA){
                Agent agent = team.agents.get(idxA);
                AgentController controller = new AgentController(
                    this.parent,    // gui_client
                    this.battleID,  // battleID
                    team.teamID,    // teamID
                    agent.agentID,  // agentID
                    agent.x,        // x
                    agent.y,        // y
                    this.tileSize,  // tileSize
                    idxT            // teamcolor
                );
                this.agentControllers.put(agent.agentID, controller);
            }
        }
    }

    void draw(){
        background(255);

        // Panel remove mode
        if(this.ifShiftPressing){
            fill(100, 100, 100, 200);
            rect(0, 0, 810, 790);
        }

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

        // Information(score)
        fill(255, 200, 200);
        rect(850, 70, 300, 100);
        fill(200, 200, 255);
        rect(850, 170, 300, 100);

        fill(0);
        textAlign(CENTER);
        textSize(30);
        text("~Score~", 1000, 50);
        text("ID " + str(gameState.teams.get(0).teamID), 900, 100);
        text("ID " + str(gameState.teams.get(1).teamID), 900, 200);

        fill(0);
        textAlign(LEFT);
        textSize(25);
        text("AREA :\t " + str(gameState.teams.get(0).areaPoint), 910, 130);
        text("TILE :\t " + str(gameState.teams.get(0).tilePoint), 910, 160);
        text("AREA :\t " + str(gameState.teams.get(1).areaPoint), 910, 230);
        text("TILE :\t " + str(gameState.teams.get(1).tilePoint), 910, 260);

        // Information(turn)
        fill(0);
        textAlign(CENTER);
        textSize(30);
        text("~Turn~", 1000, 350);
        text(gameState.turn, 1000, 390);

        // Information(update)
        text("~Game Update~", 1000, 470);

        // Information(clock)
        text("~Clock~", 1000, 620);
        text(getNowTime(), 1000, 670);

        // Exit Message
        fill(0);
        textSize(15);
        textAlign(LEFT);
        text("Press \'B\' to exit game", 1000, 785);
    }

    // Button
    public void handleButtonEvents(GButton button, GEvent event){
        if("GameUpdate".equals(button.tag)){
            this.gameState = getGameState(this.battleID);
        }else{
            int agentID = int(split(button.tag, ":")[0]);
            this.agentControllers.get(agentID).handleButtonEvents(button, event, this.ifShiftPressing);
        }
    }

    // TextFieled
    public void handleTextEvents(GEditableTextControl textcontrol, GEvent event){}

    // Key Events
    void keyPressed(){
        if(key == CODED){
            if(keyCode == SHIFT) this.ifShiftPressing = true;
        }else if(key == 'B'){
            switchWindow("BattleSelect");
        }
    }

    void keyReleased(){
        if(key == CODED){
            if(keyCode == SHIFT) this.ifShiftPressing = false;
        }
    }
}