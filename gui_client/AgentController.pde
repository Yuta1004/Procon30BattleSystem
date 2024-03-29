class AgentController{
    private gui_client parent;
    private int battleID, teamID, agentID, x, y, tileSize, teamColor;
    private GButton agentSelectButton;
    private boolean isVisible;
    private ArrayList<GButton> agentMoveSetButtons;

    AgentController(gui_client parent, int battleID, int teamID, int agentID,
                    int x, int y, int tileSize, int teamColor){
        this.parent = parent;
        this.battleID = battleID;
        this.teamID = teamID;
        this.agentID = agentID;
        this.x = x * tileSize + 3;
        this.y = y * tileSize + 3;
        this.tileSize = tileSize;
        this.teamColor = teamColor;
        this.isVisible = false;
        initButtons();
        setVisible(false);
        setEnabled(battleList.get(this.battleID).myTeamID == this.teamID);
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

    public void setPos(int boardX, int boardY){
        int newX = boardX * this.tileSize + 3;
        int newY = boardY * this.tileSize + 3;
        int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
        int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};

        // move
        this.agentSelectButton.moveTo(newX, newY);
        for(int idx = 0; idx < 8; ++ idx){
            int afterX = newX + this.tileSize * dx[idx];
            int afterY = newY + this.tileSize * dy[idx];
            this.agentMoveSetButtons.get(idx).moveTo(afterX, afterY);
        }
    }

    public void setVisible(boolean bool){
        for(int idx = 0; idx < 8; ++ idx){
            this.agentMoveSetButtons.get(idx).setVisible(bool);
        }
    }

    public void setEnabled(boolean bool){
        bool = bool && battleList.get(this.battleID).myTeamID == this.teamID;
        this.agentSelectButton.setEnabled(bool);
        for(int idx = 0; idx < 8; ++ idx){
            this.agentMoveSetButtons.get(idx).setEnabled(bool);
        }
    }

    public boolean isMoveSelectVisible(){
        return this.isVisible;
    }

    public void start(){
        this.agentSelectButton.setVisible(true);
        setEnabled(true);
    }

    public void finish(){
        this.agentSelectButton.setVisible(false);
        setEnabled(true);
        setVisible(false);
    }

    public void handleButtonEvents(GButton button, GEvent event, boolean isShiftPressing){
        String[] command = split(button.tag, ":");

        // Block clicks to not my team agent
        if(battleList.get(this.battleID).myTeamID != this.teamID){
            return;
        }

        // Agent Click
        if(command.length == 1){
            this.isVisible = !this.isVisible;
            setVisible(this.isVisible);
            setEnabled(true);
        }

        // Move Select
        if(command.length == 3){
            int dx = int(command[1]);
            int dy = int(command[2]);
            String type = isShiftPressing ? "\"remove\"" : "\"move\"";
            sendActionData(this.battleID, this.agentID, dx, dy, type);
            setVisible(false);
        }
    }
}