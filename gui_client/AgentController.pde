class AgentController{
    private gui_client parent;
    private int teamID;
    private int agentID;
    private int x;
    private int y;
    private int tileSize;
    private GButton agentSelectButton;

    AgentController(gui_client parent, int teamID, int agentID, int x, int y, int tileSize, int teamColor){
        this.parent = parent;
        this.teamID = teamID;
        this.agentID = agentID;
        this.x = x * tileSize + 3;
        this.y = y * tileSize + 3;
        this.tileSize = tileSize;

        this.agentSelectButton = new GButton(
            this.parent, this.x, this.y,
            this.tileSize, this.tileSize, ""
        );
        this.agentSelectButton.tag = str(agentID);

        // Set Button Color
        if(teamColor == 0){
            this.agentSelectButton.setLocalColor(3, color(255, 0, 0));
            this.agentSelectButton.setLocalColor(4, color(255, 100, 100, 100));
            this.agentSelectButton.setLocalColor(6, color(230, 100, 100, 150));
            this.agentSelectButton.setLocalColor(14, color(200, 100, 100, 200));
        }else{
            this.agentSelectButton.setLocalColor(3, color(0, 0, 255));
            this.agentSelectButton.setLocalColor(4, color(100, 100, 255, 100));
            this.agentSelectButton.setLocalColor(6, color(100, 100, 230, 150));
            this.agentSelectButton.setLocalColor(14, color(100, 100, 200, 200));
        }
    }

    public void setPos(int x, int y){
        this.x = x;
        this.y = y;
    }

    public void finish(){
        this.agentSelectButton.setVisible(false);
    }

    public void handleButtonEvents(GButton button, GEvent event){
    }
}