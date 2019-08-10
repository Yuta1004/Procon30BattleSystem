class BattleSelectWindow implements Window{
    private gui_client parent;
    private ArrayList<GButton> joinButtons;
    private ArrayList<Battle> battleList;

    BattleSelectWindow(gui_client parent){
        this.parent = parent;
        this.battleList = new ArrayList<Battle>();
        this.joinButtons = new ArrayList<GButton>();

        // Init Button
        for(int idx = 0; idx < 7; idx ++){
            int baseY = 200 + idx * 110;
            this.joinButtons.add(new GButton(
                this.parent, 900, baseY + 40, 70, 30, "JOIN"
            ));
            this.joinButtons.get(idx).setVisible(false);
        }
    }

    void start(){
        this.battleList = getBattleList();
        for(int idx = 0; idx < min(7, this.battleList.size()); ++ idx){
            this.joinButtons.get(idx).tag = str(battleList.get(idx).battleID);
            this.joinButtons.get(idx).setVisible(true);
        }
    }

    void finish(){
        for(int idx = 0; idx < 7; ++ idx){
            this.joinButtons.get(idx).setVisible(false);
        }
    }

    void draw(){
        background(255);

        // Window Title
        fill(0);
        textSize(40);
        textAlign(CENTER);
        text("Battle Select", 600, 120);

        // View Battle List
        for(int idx = 0; idx < this.battleList.size(); ++ idx) {
            Battle battle = this.battleList.get(idx);

            // Background
            int baseY = 200 + idx * 110;
            fill(255, 255, 100, 150);
            rect(200, baseY, 800, 80);

            // BattleID
            fill(0);
            textSize(20);
            textAlign(LEFT);
            text("BattleID", 230, baseY + 25);
            textSize(35);
            text(str(battle.battleID), 230, baseY + 65);

            // MatchTo
            fill(0);
            textSize(20);
            textAlign(LEFT);
            text("MatchTo", 370, baseY + 25);
            textSize(35);
            text(battle.matchTo, 370, baseY + 65);

            // Turns
            fill(0);
            textSize(20);
            textAlign(LEFT);
            text("Turns", 760, baseY + 25);
            textSize(35);
            text(battle.turns, 760, baseY + 65);

            // Join Button
            fill(0);
            textSize(20);
            textAlign(LEFT);
            text("Join", 900, baseY + 25);
        }
    }

    /* G4P functions */
    void handleButtonEvents(GButton button, GEvent event){
        int battleID = int(button.tag);
        if(!windows.containsKey("Game" + button.tag)){
            windows.put("Game" + button.tag, new GameWindow(this.parent, battleID));
        }
        switchWindow("Game" + button.tag);
    }

    void handleTextEvents(GEditableTextControl textcontrol, GEvent event){}

    /* Key events */
    void keyPressed(){}
    void keyReleased(){}
}