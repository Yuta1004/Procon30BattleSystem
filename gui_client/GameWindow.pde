import java.util.Calendar;


class GameWindow implements Window{
    private gui_client parent;
    private GameState gameState;
    private int battleID, bWidth, bHeight, tileSize, xBias, yBias;
    private long periodTime, nextUpdateTime;
    private HashMap<Integer, Integer> teamColors;
    private HashMap<Integer, AgentController> agentControllers;
    private GButton gameUpdate;
    private boolean ifShiftPressing;

    GameWindow(gui_client parent, int battleID){
        // Init Variables
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

        // Init View color
        int colors[] = {
            color(255, 200, 200),
            color(200, 200, 255)
        };
        for(int idx = 0; idx < min(2, this.gameState.teams.size()); ++ idx){
            teamColors.put(this.gameState.teams.get(0).teamID, color(255, 200, 200));
            teamColors.put(this.gameState.teams.get(1).teamID, color(200, 200, 255));
        }
        teamColors.put(0, color(255));

        // Init G4P
        this.gameUpdate = new GButton(
            this.parent, 950, 550, 100, 50, "MANUAL UPDATE"
        );
        this.gameUpdate.tag = "GameUpdate";

        // Init AgentController
        initAgentControllers();

        // Auto Update Setup
        Battle battle = battleList.get(this.battleID);
        long nowTime = System.currentTimeMillis() / 1000;
        this.periodTime = (battle.turnMillis + battle.intervalMillis) / 1000;
        long nowSlipTime = (nowTime - this.gameState.startAtUnixTime) % this.periodTime;
        this.nextUpdateTime = nowTime + (periodTime - nowSlipTime);
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

        // Auto Update
        long nowTime = System.currentTimeMillis() / 1000;
        if(nowTime >= this.nextUpdateTime){
            updateBoard();
            this.nextUpdateTime += this.periodTime;
        }

        // Panel remove mode
        if(this.ifShiftPressing && this.bWidth > 0){
            fill(100, 100, 100, 200);
            rect(0, 0,
                 this.bWidth * this.tileSize + 10,
                 this.bHeight * this.tileSize - 10
            );
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
        for(int idx = 0; idx < this.gameState.teams.size(); ++ idx){
            text("ID " + str(gameState.teams.get(idx).teamID), 900, (idx + 1) * 100);
        }

        fill(0);
        textAlign(LEFT);
        textSize(25);
        for(int idx = 0; idx < this.gameState.teams.size(); ++ idx){
            text("AREA :\t " + str(this.gameState.teams.get(idx).areaPoint), 910, 130 + idx * 100);
            text("TILE :\t " + str(this.gameState.teams.get(idx).tilePoint), 910, 160 + idx * 100);
        }

        // Information(turn)
        fill(0);
        textAlign(CENTER);
        textSize(30);
        text("~Turn~", 1000, 350);
        text(gameState.turn, 1000, 390);

        // Information(update)
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(this.nextUpdateTime * 1000);
        int hour = calendar.get(Calendar.HOUR_OF_DAY);
        int minute = calendar.get(Calendar.MINUTE);
        int second = calendar.get(Calendar.SECOND);
        text("~Next Update~", 1000, 480);
        text(formatDate(hour, minute, second), 1000, 530);

        // Information(clock)
        text("~Clock~", 1000, 670);
        text(formatDate(hour(), minute(), second()), 1000, 720);

        // Exit Message
        fill(0);
        textSize(15);
        textAlign(LEFT);
        text("Press \'B\' to exit game", 1000, 785);
    }

    private void updateBoard(){
        this.gameState = getGameState(this.battleID);
        for(Team team: this.gameState.teams){
            for(Agent agent: team.agents){
                this.agentControllers.get(agent.agentID).setPos(agent.x, agent.y);
            }
        }
    }

    // Button
    public void handleButtonEvents(GButton button, GEvent event){
        if("GameUpdate".equals(button.tag)){
            updateBoard();
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