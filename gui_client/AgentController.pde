class AgentController{
    private gui_client parent;
    private int teamID, agentID, x, y, tileSize, teamColor;
    private GButton agentSelectButton;
    private boolean isVisible;
    private ArrayList<GButton> agentMoveSetButtons;

    AgentController(gui_client parent, int teamID, int agentID, int x, int y, int tileSize, int teamColor){
        this.parent = parent;
        this.teamID = teamID;
        this.agentID = agentID;
        this.x = x * tileSize + 3;
        this.y = y * tileSize + 3;
        this.tileSize = tileSize;
        this.teamColor = teamColor;
        this.isVisible = false;
        initButtons();
        setVisible(false);
    }

    private void initButtons(){
        /* Agent Select Button */
        this.agentSelectButton = new GButton(
            this.parent, this.x, this.y,
            this.tileSize, this.tileSize, ""
        );
        this.agentSelectButton.tag = str(agentID);

        // Set Button Color
        if(this.teamColor == 0){
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

        /* Move Set Buttons */
        this.agentMoveSetButtons = new ArrayList<GButton>();
        int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
        int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};
        for(int idx = 0; idx < 8; ++ idx){
            GButton button = new GButton(
                this.parent,
                this.x + dx[idx] * this.tileSize,
                this.y + dy[idx] * this.tileSize,
                this.tileSize,
                this.tileSize, ""
            );
            button.tag = str(this.agentID) + ":" + str(dx[idx]) + ":" + str(dy[idx]);
            button.setLocalColor(3, color(0));
            button.setLocalColor(4, color(255, 255, 0, 40));
            button.setLocalColor(6, color(255, 255, 0, 80));
            button.setLocalColor(14, color(255, 255, 0, 120));
            this.agentMoveSetButtons.add(button);
        }
    }

    public void setPos(int x, int y){
        this.x = x;
        this.y = y;
    }

    public void setVisible(boolean bool){
        for(int idx = 0; idx < 8; ++ idx){
            this.agentMoveSetButtons.get(idx).setVisible(bool);
        }
    }

    public void finish(){
        this.agentSelectButton.setVisible(false);
    }

    public void handleButtonEvents(GButton button, GEvent event, boolean isShiftPressing){
        this.isVisible = !this.isVisible;
        setVisible(this.isVisible);
    }
}