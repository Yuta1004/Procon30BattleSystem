class AgentController{
    private gui_client parent;
    private int teamID;
    private int agentID;
    private int x;
    private int y;
    private int tileSize;
    private GButton agentSelectButton;

    AgentController(gui_client parent, int teamID, int agentID, int x, int y, int tileSize){
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
        this.agentSelectButton.tag = "Agent" + str(agentID);
    }

    public void setPos(int x, int y){
        this.x = x;
        this.y = y;
    }

    public void finish(){
        this.agentSelectButton.setVisible(false);
    }
}